# Author: Robby Marver
# Contact: rmarver12@gmail.com
# 
# This file simply combines different csv files.

import glob

# This method accepts the league of teams as an argument and combines all csv
# files in the directory of that league into a single csv file.
def combine(league):
    csvs = glob.glob(league + '/*.csv')

    header_saved = False

    with open('output_' + league + '.csv', 'wb') as fout:
        for filename in csvs:
            with open(filename) as fin:
                header = next(fin)
                if not header_saved:
                    fout.write(header)
                    header_saved = True
                for line in fin:
                    fout.write(line)