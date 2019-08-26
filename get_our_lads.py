# Author: Robby Marver
# Contact: rmarver12@gmail.com
#
# This file defines the methods that are used to scrape Twitter and other sources
# to get player information and their potential Twitter handles.

import requests
import pandas as pd
from fuzzywuzzy import process, fuzz

config = {}
execfile('config.py', config)

# This method goes through each player on the team and attempts to find each
# of their Twitter handles. If parsed is not None, then this method will
# search a previous output file for the twitter handle of a player.
def write_team_csv(api, team_code, team_name, org, player_list, parsed=None):
    # Get the dataframe from the website
    team_data = get_team_data(team_code, org)

    fullnames = ['']  # Full names of the players (First Last)
    twitter_handles = ['']  # Twitter handles of the players, N/A if not found
    twitter_ids = ['']  # Twitter IDs of the players, N/A if not found
    confidence = ['']  # Confidence in search hit: High - Medium - Low (if not found)
    player_names = team_data['Player']

    for i in range(1, len(player_names)):
        # Get the player's real name
        real_name = get_real_name(player_names[i])
        if real_name == False:
            team_data = team_data.drop(team_data.index[i])
            continue
            
        fullnames.append(real_name)
        if parsed != None:
            res = parsed.get_twitter_from_name(real_name)
            if res != None:
                twitter_handles.append(res[0])
                twitter_ids.append(res[1])
                confidence.append(res[2])
                continue

        if player_list != None:
            res = process.extractOne(real_name, player_list.keys(), scorer=fuzz.token_set_ratio)
            if res[1] > 70:
                if '@' in res[0]:
                    twitter_handles.append(res[0])
                    twitter_ids.append(player_list[res[1]])
                else:
                    twitter_handles.append(player_list[res[0]][0])
                    twitter_ids.append(player_list[res[0]][1])
                confidence.append('High')
                continue

        # Search for the user
        users = api.users.search(q = real_name)
        results = find_user(api, real_name, team_name, users, org)
        twitter_handles.append(results[0])
        twitter_ids.append(results[1])
        confidence.append(results[2])


    # Add the Twitter data as new columns
    team_data['Fullname'] = fullnames
    team_data['Handle'] = twitter_handles
    team_data['TwitterID'] = twitter_ids
    team_data['Confidence'] = confidence
    team_data = team_data.drop(team_data.index[0])
    res = team_data.to_csv(config['%s_root_dir' % org] + team_name + '.csv', encoding='utf-8-sig')

# This method attempts to find the user's twitter handle by looking through their
# Twitter description and multiple tweets (as defined by max_search) and assigns
# a confidence level to that user with a given twitter handle.
# Low confidence: A handle was found, and that handle mentioned something useful
#                 about the player.
# Medium confidence: A verified handle was found.
# High confidence: A verified handle was found and the handle mentioned something useful
#                  about the player.
def find_user(api, real_name, team_name, users, org, max_search=10):
    result = ('N/A', 'N/A', 'Low')
    for i in range(0, min(len(users), max_search)):
        user = users[i]
        to_compare = user['description'].upper()
        if user['verified']:
            # Going to assume verified users are probable matches
            result = (user['screen_name'], user['id'], 'Medium')

            # If the description matches, this is a good sign
            if user_heuristic(team_name, user['description'].upper(), org):
                result = (result[0], result[1], 'High')
            elif search_tweets(api, user, team_name, org):
                result = (result[0], result[1], 'High')
        elif search_tweets(api, user, team_name, org):
            if result[2] == 'Low':
                result = (user['screen_name'], user['id'], 'Low')
        
        if result[2] == 'High':
            return result

    return result

# Searches through a tweet of the given user, returns True if the tweet gives an
# indication that this is the player we are looking for.
def search_tweets(api, user, team_name, org):
    try:
        res = api.statuses.user_timeline(screen_name = user['screen_name'])
        for status in res:
            if user_heuristic(team_name, status["text"].encode("ascii", "ignore").upper(), org):
                return True
    except Exception:
        # Do nothing, probably a private user
        return False

    return False

# Returns True if there is an indication that this player can be matched to the
# Twitter handle we are looking at, False otherwise.
def user_heuristic(team_name, to_search, org):
    words = team_name.split()
    for word in words:
        if word.strip() in to_search:
            return True

    for word in config['%s_team_codes' % org]:
        name = word.split(':')[1].strip()
        if name in to_search:
            return True

    return ('@%s' % org) in to_search or ('#%s' % org) in to_search or (' %s ' % org) in to_search

# Get the name of the player we are searching for.
## TODO: This method is specific to OurLads, but might have to change depending
#        on the website that you use to get team rosters.
def get_real_name(name):
    try:
        name = name.split(',')
    except Exception:
        return False

    if len(name) != 2:
        return False

    return name[1].strip() + ' ' + name[0].strip()

# Gets the roster of players from a reputable site, as defined in config.py, for
# the specific organization (league, like NFL) and team code, which is how the
# url defines the team. See config.py for more details.
def get_team_data(team_code, org):
    url = config['%s_root_url' % org] + team_code
    html = requests.get(url).content
    df_list = pd.read_html(html)
    return df_list[-1]