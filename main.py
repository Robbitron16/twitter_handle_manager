# Author: Robby Marver
# Contact: rmarver12@gmail.com
#
# This file runs the main program to collect Twitter handles from a given csv
# file that represents a roster of players.

import os
import sys
import tweepy
import twitter
from csv_parser import CSVParser
from get_our_lads import write_team_csv
from combine_csvs import combine
from clean_up_low_confidence import clean_up_file


# Defines a dictionary that stores configuration options. See config.py
# for more details.
config = {}
execfile('config.py', config)

# This method prints the correct usage of this program to the console
# if this program is executed incorrectly, if the league does not exist,
# or if the previous output file does not exist or is invalid.
def usage():
    print 'Usage: python <league> <--use-previous-files>'
    print 'Example: python ncaa'
    print 'Example: python nfl'
    sys.exit(1)


# Main method
#
# This method generates an output csv file with the members of a league and their
# twitter handles (as well as other information that pertains to each player).
# If the program is invoked incorrectly, a usage message will appear instead.
# The user may abort this method with the guarantee that progress will be saved
# on the granularity of a team (in that, all teams that were completed before the
# program was aborted will be saved correctly).
def main():
    if len(sys.argv) == 1:
        usage()

    league = sys.argv[1].lower()
    ## TODO: Simple check to make sure the league is NCAA or NFL. This should
    #        be checked against a set of leagues that we are interested in.
    #        Update config.py to create the URLs for other leagues correctly.
    if league != 'ncaa' and league != 'nfl':
        usage()

    ## TODO: Make the --use-previous-files flag functional. Currently, the program
    #        will assume that a file exists with the twitter handles from a
    #        previous run and check the file to make sure it doesn't have to re-find
    #        a Twitter handle for a certain player. If the flag is not present
    #        in the command arguments, then the file should not be checked.
    parser = CSVParser(league, config)
    
    # Create a twapi instance that is tied to the developer account.
    api = twitter.Twitter(
        auth = twitter.OAuth(
            config['access_key'],
            config['access_secret'],
            config['consumer_key'],
            config['consumer_secret']))
    twauth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
    twauth.set_access_token(config['access_key'], config['access_secret'])
    twapi = tweepy.API(twauth)

    # For each team in the given league, find the Twitter handle of each team
    # member.
    for team in config[league + '_team_codes']:
        res = team.split(':')
        team_code = res[0]
        team_name = res[1]
        print 'Starting %s' % team_name.strip()
        player_list = None
        if len(res) > 2:
            list_owner = res[2]
            list_name = res[3]
            player_list = {}
            for member in tweepy.Cursor(twapi.list_members, list_owner, list_name).items():
                user_dict = member.__dict__
                player_list[user_dict['screen_name']] = user_dict['id_str']
                player_list[user_dict['name']] = (user_dict['screen_name'], user_dict['id_str'])

        # Write the twitter handles of the team to the output csv file.
        # The handle might be taken from the previous output file if it is present.
        write_team_csv(api, team_code.strip(), team_name.strip(), league, player_list, parsed=parser)
        print 'Finished %s' % team_name.strip()

    # Go through the csv file, manually prompt the user to look at the handles
    # that were rated as low confidence (i.e. not sure if the handle is correct).
    ## TODO: Might want to make this optional, this part can take a while as you
    #        must manually interact with the program.
    clean_up_file(league, config, twapi)

    # Combine all of the team csv output files into a single league file.
    combine(league)
    os.system('cut -d, -f2 --complement output_%s.csv > %s.csv' % (league, league))
    os.system('rm output_%s.csv' % league)
    print 'See output in %s' % (league + '.csv')

if __name__ == '__main__':
    main()