TOPN = 3
SHEET_NAME = "SlackApp_Test1"
ROW_LEN = 16
DELIM = ", "

#define column names
USER_ID = 'user_id'
NAME = 'user_name'
AGE = 'age'
CUISINE = 'cuisine'
LIKE_CT = 'like_CT'
CT_FAVE_PART = 'CT_fave_part'
CT_UNFAVE_PART = 'CT_unfave_part'
MOVIE = 'movie'
TALKATIVE = 'talkative' #1 to 5 = {listen --- talk}         consider flip
INTRO_EXTRO = 'intro_extro' #{intro, extro, In between}     consider flip
P_ACTIVIST = 'p_activist'                                  #consider flip
VACA = 'vaca'
NEW_THINGS = 'new_things'
DOG_CAT = 'dog_cat' # Neither
BEER_WINE = 'beer_wine' # Pref Not to drink
TEA_COFFEE = 'tea_coffee' # Neither  - i don't need caffine
VOLUNTEER = 'volunteer'

#multiple choice options
HB = 'What do you like to do outside of class?'
WB = 'What are you doing for winter break?'

HB_SLEEP = 'Nothing but sleep'
HB_WO = 'Workout'
HB_FRIENDS = 'See friends'
HB_DRINK ='Drink'
HB_NYC = 'Explore NYC'
HB_STUDY = 'Study'

WB_TREK ='One of the Treks!'
WB_TRAVEL = 'Traveling the world'
WB_HOME = 'Going home to see family'
WB_NYC = 'staying in NYC and relaxing'
WB_SPORT = 'winter sport activities'


#define maps
age_map = {'20-23': 20, '24-27': 24, '28-31': 28, '31+': 31}
cuisine_map = {'American':1, 'Italian':2, 'Japanese':3,
               'Chinese':4, 'Thai':5, 'Mexican': 6, 'French': 7,
               'Mediterranean': 8, 'Variety of cuisines.':9}
like_ct_map = {'Yes': 1, 'No': -1}
movie_map = {'Comedy':1, 'Romance':2, 'Horror':3, 'Indie':4, 'Foreign':5, 'Drama':6, 'Suspense':7, 'Action':8}
intro_map = {'Introverted': -11, 'In between': 0, 'Extroverted':1}
activist_map =  {'Yes': -1, 'No':2, 'Not Really': 1, 'Prefer not to answer': 0}
vaca_map = {'Relaxing on the beach': 1, 'Exploring new countries and cultures': 2,
           'Visiting with friends and family': 3, 'Active Adventure': 4,
           'Sporty (hiking, skiing)': 5}
new_things_map = {'Culture Related': 1, 'Food Related': 2, 'Sports Related': 3, 'Travel Related': 4}
dogcat_map = {'Cats': -1, 'Dogs': 1, 'Neither': 0}
beer_wine_map = {'Beer':1 , 'Wine': -1, 'Pref Not to drink':0}
volunteer_map = {'Always - whenever I have free time': 1, 'I try but time is limited': 2, 'No - not really my thing': 3}
tea_coffee_map = {'Coffee':1, 'Tea': 2, 'Both': 3, 'Neither - I don\'t need caffine': -4}