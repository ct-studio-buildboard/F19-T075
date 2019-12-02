# [START functions_slack_setup]
import json

import apiclient
from flask import jsonify
from DAL import get_friends, user_exists

import logging

with open('config.json', 'r') as f:
    data = f.read()
config = json.loads(data)


# [END functions_slack_setup]


def verify_web_hook(form):
    if not form or form.get('token') != config['SLACK_TOKEN']:
        raise ValueError('Invalid request/credentials.')


def format_slack_message(friends):
    entity = None

    friends = [f'@{f}' for f in friends]
    message = {
        'response_type': 'in_channel',
        'text': 'Your friend recomendations: {}'.format(friends),
    }
    return message

def make_search_request(username):
    if not user_exists(username):
        return "please fill the form by calling /myData"
        
    friends = get_friends(username)
    return format_slack_message(friends)

def friend_search(request):
    if request.method != 'POST':
        return 'Only POST requests are accepted', 405
    
    logging.info(request.form)
    
    verify_web_hook(request.form)
    friend_search_response = make_search_request(request.form['user_name'])
    return jsonify(friend_search_response)
    
    