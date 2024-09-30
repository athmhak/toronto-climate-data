#!/usr/bin/python3

import pandas as pd
import glob
import os

input_path = os.environ.get('INPUT_FOLDER')
output_path = os.environ.get('OUT_FOLDER')
filename = 'all_years.csv'
csvs = sorted(glob.glob(os.path.join(input_path,"*.csv"))) #get list of files, sort them yearly

#df_concat = pd.concat([pd.read_csv(f, index_col=None, header=0) for f in csvs], )

li = []
for f in csvs:
    df = pd.read_csv(f,index_col=None,header=0)
    li.append(df)

df_concat = pd.concat(li,axis=0,ignore_index=True)

df_concat.to_csv(output_path+"/"+filename)



