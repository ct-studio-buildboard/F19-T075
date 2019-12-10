# [START functions_slack_setup]
import json
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
    gsclient = _get_gspread_client()
    friends = get_friends(username, )
    if len(friends) == 0:
        return "please fill the full form by calling /addme"
        
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
    # if user_exists(userid):
        # msg = f'<@{userid}>, ' + "we have already successfully onboarded you!\nIf you'd like to check whether we have new matches for you, type `/friends`"
        # return msg
        
    view = views.pl_view # test_view

    trigger = request.form['trigger_id']
    client.views_open(
        trigger_id=trigger,
        view = view
    )
    
    msg = f'<@{userid}>!' + ", if you clicked `Submit`, Good Job!"  + "\n*Even though it may seem like it didn't work, it most likely did!* (this is still in beta)\nnow try typing `/friends` to find friend recommendations."
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
        logging.info("not a submission, skipping")
        return 
        
    userid = payload['user']['id']
    logging.info(f'userid is {userid}')
    if user_exists(userid):
        logging.info(f'user {userid} already exists')
        return ''
        
    logging.info(f'adding user {userid}')
    add_user(payload)
    return ''

def _get_gspread_client():
    # note that adding the second scope is necesary
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    gc = gspread.authorize(creds)

    logging.info('created gspread client')
    return gc
    
    
