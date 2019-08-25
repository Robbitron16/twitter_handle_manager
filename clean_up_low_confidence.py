# Author: Robby Marver
# Contact: rmarver12@gmail.com
#
# This file defines the method that cleans up the output files of low confidence
# matches of players to their Twitter handles.

import pandas as pd
import math

# This method cleans up each team file team by team and attempts to clarify whether
# any low-confidence twitter handles are actually correct. The user manually
# enters 'y' for yes, anything else for no, and tallies how many of the low-confidence
# matches were actually correct. If the twitter handle is determined to be incorrect,
# the handle for that player is deemed N/A.
def clean_up_file(league, config, twapi):
    for itm in config[league + '_team_codes']:
        filename = league + '/' + itm.split(':')[1].strip()
        data = pd.read_csv(filename + '.csv')

        twitter_handles = []
        twitter_ids = []
        confidence = []
        total = 0
        yesses = 0
        for i in range(0, len(data['Confidence'])):
            # Found a possible candidate
            if data['Confidence'][i] == 'Low' and type(data['Handle'][i]) != float:
                user = twapi.get_user(screen_name=data['Handle'][i])
                resp = raw_input('%s for player %s of the %s? Description: %s (y/n) ' % (data['Handle'][i], data['Fullname'][i], itm.split(':')[1].strip(), user.description.encode('utf-8').strip()))
                total += 1
                if resp == 'y':
                    confidence.append('High')
                    twitter_handles.append(data['Handle'][i])
                    twitter_ids.append(data['TwitterID'][i])
                    yesses += 1
                else:
                    confidence.append('Low')
                    twitter_handles.append('N/A')
                    twitter_ids.append('N/A')
            else:
                confidence.append(data['Confidence'][i])
                twitter_handles.append(data['Handle'][i])
                twitter_ids.append(data['TwitterID'][i])

        data['Handle'] = twitter_handles
        data['TwitterID'] = twitter_ids
        data['Confidence'] = confidence
        data.to_csv(filename + '.csv', encoding='utf-8-sig')
        print '%d / %d for %s' % (yesses, total, itm.split(':')[1].strip())

