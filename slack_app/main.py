# [START functions_slack_setup]
import json

import slack

import apiclient
from flask import jsonify
from DAL import get_friends, user_exists

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
    message = {
        'response_type': 'in_channel',
        'text': f'Hi <@{username}>!\nYour top {const.TOPN} friend recomendations are: {sep.join(friends)}',
    }
    return message

def make_search_request(username):
    if not user_exists(username):
        return "please fill the form by calling /myData"
        
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

    logging.info(f'request: {request}')
    logging.info(f'form: {request.form}')
    

    
    view = views.pl_view # test_view 
    logging.info(f'using view: {view}')
    
    trigger = request.form['trigger_id']
    client.views_open(
        trigger_id=trigger,
        view = view
    )
    
    return "what happened?"
    
    
def get_input(request):
    if request.method != 'POST':
        return 'Only POST requests are accepted', 405

    verify_web_hook(request.form)

    logging.info(f'got input request: {request}')
    logging.info(f'request form: {request.form}')

    
    return "nothing";
    