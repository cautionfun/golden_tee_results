##compile results
##MAKE SURE TO RUN THIS IN THE RELEVANT DIRECTORY
##check working directory after importing os with print("Current working directory: {0}".format(os.getcwd()))
import os
import glob
import pandas as pd
##tell it to go through each file in the chosen directory and pick out every one with the csv file extension
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
##read and combine all relevant files into one variable
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
##spit that out into a csv file located in a folder to be read by filter_sort_results.py
combined_csv.to_csv( "final/combined_csv.csv", index=False, encoding='utf-8-sig')
