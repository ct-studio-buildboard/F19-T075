import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import logging

import my_slack_app_constants as const

def get_gspread_client():
    # note that adding the second scope is necesary
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    gc = gspread.authorize(creds)

    logging.info('created gspread client')
    return gc
    
def get_sheet():    
    client = get_gspread_client()
    sheet = client.open(const.SHEET_NAME).sheet1
    return sheet

def get_df():
    sheet = get_sheet()
    data = sheet.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)

    logging.debug(f'dataframe columns: {headers}')
    logging.info(f'successfully read data frame from {const.SHEET_NAME}')
    return df
    
def map_1to1_mappings(df):
    df[const.AGE] = df[const.AGE].map(const.age_map)
    df[const.CUISINE] = df[const.CUISINE].map(const.cuisine_map)
    df[const.LIKE_CT] = df[const.LIKE_CT].map(const.like_ct_map)
    df[const.MOVIE] = df[const.MOVIE].map(const.movie_map)
    df[const.INTRO_EXTRO] = df[const.INTRO_EXTRO].map(const.intro_map)
    df[const.P_ACTIVIST] = df[const.P_ACTIVIST].map(const.activist_map)
    df[const.VACA] = df[const.VACA].map(const.vaca_map)
    df[const.NEW_THINGS] = df[const.NEW_THINGS].map(const.new_things_map)
    df[const.DOG_CAT] = df[const.DOG_CAT].map(const.dogcat_map)
    df[const.BEER_WINE] = df[const.BEER_WINE].map(const.beer_wine_map)
    df[const.VOLUNTEER] = df[const.VOLUNTEER].map(const.volunteer_map)
    df[const.TEA_COFFEE] = df[const.TEA_COFFEE].map(const.tea_coffee_map)
    return df
    
def map_multiple_choice(df):
    df['hb_sleep'] = df[const.HB].map(lambda x: 1 if const.HB_SLEEP in x else 0)
    df['hb_wo'] = df[const.HB].map(lambda x: 1 if const.HB_WO in x else 0)
    df['hb_friends'] = df[const.HB].map(lambda x: 1 if const.HB_FRIENDS in x else 0)
    df['hb_drink'] = df[const.HB].map(lambda x: 1 if const.HB_DRINK in x else 0)
    df['hb_nyc'] = df[const.HB].map(lambda x: 1 if const.HB_NYC in x else 0)

    df['wb_trek'] = df[const.WB].map(lambda x: 1 if const.WB_TREK in x else 0)
    df['wb_travel'] = df[const.WB].map(lambda x: 1 if const.WB_TRAVEL in x else 0)
    df['wb_home'] = df[const.WB].map(lambda x: 1 if const.WB_HOME in x else 0)
    df['wb_nyc'] = df[const.WB].map(lambda x: 1 if const.WB_NYC in x else 0)
    df['wb_sport'] = df[const.WB].map(lambda x: 1 if const.WB_SPORT in x else 0)
    
    df = df.drop([const.WB], axis=1)
    df = df.drop([const.HB], axis=1)
    return df

def format_df(df):
    df = map_1to1_mappings(df)
    df = map_multiple_choice(df)
    df = df.drop(['cosine_top_n'], axis=1)
    
    logging.info('formated data frame to numeric space')
    nans =  df.isna().sum()
    logging.info(f'found NaNs: {nans}')
    return df
    
def get_sort_indexes(l, reverse=False):
    return sorted(range(len(l)), key=lambda k: l[k], reverse=reverse)

# assumes n a positive integer  
def compute_cosine_top_n(df, n):
    cosine_df = df.copy()
    cosine_df = cosine_df.drop([const.USER_ID], axis=1)

    cosine = cosine_similarity(cosine_df)
    cosine_df['cosine'] = list(cosine)
    
    # removal of self ocurs by range exclusion of 0
    l = range(1, n+1)
    cosine_df['top_n'] = cosine_df.apply(lambda row: [df.iloc[get_sort_indexes(row.cosine, True)[x]][const.USER_ID] for x in l] , axis=1)
    df['cosine_top_n'] = cosine_df['top_n']
    
    logging.info(f'successfully computed the top {n} cosine matches')
    return df

def get_user_index_list(df, user):
    return df.index[df[const.USER_ID] == user].tolist()

# assumes df has column named cosine_top_n
# assumes user is in df only once
def get_topn_for_user(df, user):
    user_index_list = get_user_index_list(df, user)

    err = ""
    if len(user_index_list) == 0:
        err = f'user {user} was not found'
    elif len(user_index_list) > 1:
        err = f'user {user} exists multiple times'
    if err:
        raise Exception(err)
    
    u_idx = user_index_list[0]
    friends = df.iloc[u_idx]['cosine_top_n'].split(const.DELIM)
    
    logging.info(f'found friends: {friends}')
    return friends

def write_topn_to_sheet(ds):
    sheet = get_sheet()
    rows = len(ds)
    cell_list = sheet.range(f'Q2:Q{rows+1}')
    
    logging.info(f'series length: {len(ds)}, rows length: {rows}, cell_list length: {len(cell_list)}')

    for i in range(len(cell_list)):
        cell_list[i].value = const.DELIM.join(ds[i])
    res = sheet.update_cells(cell_list)
    logging.info(f'sheet cell update result: {res}')

def compute_friends():
    logging.info('recomputing friends')
    df = get_df()
    df = format_df(df)
    df = compute_cosine_top_n(df, const.TOPN)
    write_topn_to_sheet(df['cosine_top_n'])

def get_friends(username):
    logging.info(f'searching friends for {username}')
    return get_topn_for_user(df, username)
    
def user_exists(username):
    logging.info(f'checking existence of {username}')
    df = get_df()
    idx = get_user_index_list(df, username)
    u_exists = len(idx) > 0
    
    logging.info(f'user {username} exists: {u_exists}')
    return u_exists
    
def user_count():
    logging.info('user_count')
    df = get_df()
    count = df.count()[0]

    logging.info(f'have counted {count} users')
    return count

def get_blocks_dic(blocks):
    dic = {}
    for block in blocks:
        try:
            id = block['block_id']
            label = block['label']['text']
            action_id = block['element']['action_id']
            
            if 'age' in label:
                dic['age'] = (id, action_id)
            elif 'cuisine' in label:
                dic['cuisine'] = (id, action_id)
            elif 'outside of class' in label:
                dic['free_time'] = (id, action_id)
            elif 'winter' in label:
                dic['winter_break'] = (id, action_id)
            elif 'movie' in label:
                dic['movie'] = (id, action_id)
            elif 'enjoyed CT ' in label:
                dic['like_ct'] = (id, action_id)
            elif 'talkative' in label:
                dic['talkative'] = (id, action_id)
            elif 'introverted' in label:
                dic['intro_extro'] = (id, action_id)
            elif 'politics' in label:
                dic['activist'] = (id, action_id)
            elif 'vacation' in label:
                dic['vaca'] = (id, action_id)
            elif 'new things' in label:
                dic['new_things'] = (id, action_id)
            elif 'Dogs' in label:
                dic['dogcat'] = (id, action_id)
            elif 'Beer' in label:
                dic['beer_wine'] = (id, action_id)
            elif 'volunteer' in label:
                dic['volunteer'] = (id, action_id)
            elif 'Coffee' in label:
                dic['tea_coffee'] = (id, action_id)
        except Exception as e:
            logging.error(e)

    logging.info(f'computed dictionary: {dic}')
    return dic    

def get_user_row(payload):
    userID = payload['user']['id']
    blocks = payload['view']['blocks']
    values = payload['view']['state']['values']

    dic = get_blocks_dic(blocks)
    logging.info(f'values: {values}')
    
    age = values[dic['age'][0]][dic['age'][1]]['selected_option']['value']
    cuisine = values[dic['cuisine'][0]][dic['cuisine'][1]]['selected_option']['value']
    free_time = ",".join([opt['value'] for opt in values[dic['free_time'][0]][dic['free_time'][1]]['selected_options']])
    winter_break = ",".join([opt['value'] for opt in values[dic['winter_break'][0]][dic['winter_break'][1]]['selected_options']])
    like_ct = values[dic['like_ct'][0]][dic['like_ct'][1]]['selected_option']['value']
    movie = values[dic['movie'][0]][dic['movie'][1]]['selected_option']['value']
    talkative = values[dic['talkative'][0]][dic['talkative'][1]]['selected_option']['value']
    intro_extro = values[dic['intro_extro'][0]][dic['intro_extro'][1]]['selected_option']['value']
    activist = values[dic['activist'][0]][dic['activist'][1]]['selected_option']['value']
    vaca = values[dic['vaca'][0]][dic['vaca'][1]]['selected_option']['value']
    new_things = values[dic['new_things'][0]][dic['new_things'][1]]['selected_option']['value']
    dogcat = values[dic['dogcat'][0]][dic['dogcat'][1]]['selected_option']['value']
    beer_wine = values[dic['beer_wine'][0]][dic['beer_wine'][1]]['selected_option']['value']
    volunteer = values[dic['volunteer'][0]][dic['volunteer'][1]]['selected_option']['value']
    tea_coffee = values[dic['tea_coffee'][0]][dic['tea_coffee'][1]]['selected_option']['value']

    userRow = [userID, #16 entries!
        age,
        cuisine,
        free_time,
        winter_break,
        like_ct,
        movie,
        talkative,
        intro_extro,
        activist,
        vaca,
        new_things,
        dogcat,
        beer_wine,
        volunteer,
        tea_coffee
        ]
        
    logging.info(f'extracted row: {userRow}')
    return userRow

    
def add_row(user_row):
    sheet = get_sheet()
    ret = sheet.append_row(user_row)
    return ret
    
def add_user(payload):
    row = get_user_row(payload)
    res = add_row(row)
    
    compute_friends()
    
    return res