# Author: Robby Marver
# Contact: rmarver12@gmail.com
#
# Parser that manages handles previously found
# of players

import pandas as pd

class CSVParser(object):
    def __init__(self, league, config):
        self.player_handles = dict()
        filename = config['compiled_dir'] + league + '.csv'
        data = pd.read_csv(filename, error_bad_lines=False)
        for i, name in enumerate(data['Fullname']):
            self.player_handles[name] = (data['Handle'][i],
                                         data['TwitterID'][i],
                                         data['Confidence'][i])

    def get_twitter_from_name(self, name):
        if name in self.player_handles:
            return self.player_handles[name]
        else:
            return None
