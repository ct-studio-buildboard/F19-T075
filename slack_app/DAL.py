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
    

def get_df():
    client = get_gspread_client()
    sheet = client.open(const.SHEET_NAME).sheet1
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
    
    logging.info('formated data frame to numeric space')
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
    
    friends = df.iloc[user_index_list[0]]['cosine_top_n']
    
    logging.info(f'found friends: {friends}')
    return friends

def get_friends(username):
    logging.info(f'searching friends for {username}')
    df = get_df()
    df = format_df(df)
    df = compute_cosine_top_n(df, const.TOPN)
    return get_topn_for_user(df, username)
    
def user_exists(username):
    logging.info(f'checking existence of {username}')
    df = get_df()
    idx = get_user_index_list(df, username)
    u_exists = len(idx) > 0
    
    logging.info(f'user {username} exists: {u_exists}')
    return u_exists