# [START functions_slack_setup]
import json
import asyncio
import slack
import apiclient
from flask import jsonify

from DAL import get_friends, user_exists, user_count, add_user
import my_slack_app_constants as const
import views

import logging

with open('config.json', 'r') as f:
    data = f.read()
config = json.loads(data)


# [END functions_slack_setup]


def verify_web_hook(form):
    if not form or form.get('token') != config['SLACK_TOKEN']:
        raise ValueError('Invalid request/credentials.')


def format_slack_message(username, friends):
    entity = None

    sep = ", "
    friends = [f'<@{f}>' for f in friends]
    userCount = user_count()

    msg = f'Hi <@{username}>!\nOf the {userCount} users that have responded, we think your top {const.TOPN} friend recomendations are: {sep.join(friends)}'
    message = {
        'response_type': 'in_channel',
        'text': msg
    }
    return message

def make_search_request(username):
    if not user_exists(username):
        return "please fill the full form by calling /addme"
        
    friends = get_friends(username)
    return format_slack_message(username, friends)

def friend_search(request):
    if request.method != 'POST':
        return 'Only POST requests are accepted', 405
    
    verify_web_hook(request.form)

    logging.info(request.form)
    
    username = request.form['user_id']
    friend_search_response = make_search_request(username)
    return jsonify(friend_search_response)
    
def modal(request):
    if request.method != 'POST':
        return 'Only POST requests are accepted', 405

    verify_web_hook(request.form)
    
    client = slack.WebClient(token=config['SLACK_OAUTH'])

  
    userid = request.form['user_id']
    if user_exists(userid):
        msg = f'<@{userid}>, ' + "we have already successfully onboarded you!\nIf you'd like to check whether we have new matches for you, type `/friends`"
        return msg
        
    view = views.pl_view # test_view

    trigger = request.form['trigger_id']
    client.views_open(
        trigger_id=trigger,
        view = view
    )
    
    msg = "If you clicked `Submit`, Good Job " + f'<@{userid}>!' + "\nnow try typing `/friends` to find friend recommendations."
    return msg
    
    
def get_input(request):
    if request.method != 'POST':
        return 'Only POST requests are accepted', 405

    # verify_web_hook(request.form) # payload['api_app_id'] == AR00ULSNR

    payload = json.loads(request.form['payload'])
    logging.info(f'request form payload: {payload}')
    
    req_type = payload['type']
    # change this if you want to do input verification
    if req_type != "view_submission":
        return 
        
    # state = payload['view']['state']
    # logging.info(f'state: {state}')

    
    loop = asyncio.get_event_loop()
    loop.create_task(add_user(payload))
    return ''
    
    
    
def route(request):
    if request.method != 'POST':
        return 'Only POST requests are accepted', 405
    
    arg = request.form['text']
    
    if arg == 'addme':
        return modal(request)
    elif arg == 'find':
        return get_friends(request)