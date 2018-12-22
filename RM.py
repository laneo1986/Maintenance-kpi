#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import os.path


#Choose file to open
filename = input("select file name: ")
while not os.path.exists(filename):
    print("Error - file '%s' does not exist" % filename)
    filenname = input("select file name: ")
      
df = pd.read_excel(filename)
        
    

df_work = df.loc[:, ['Work Order', 'WorkType', 'AST','AFT']]
        


#convert column to datetime

df_work.loc[:,'AFT'] = pd.to_datetime(df_work.loc
           [:,'AFT'], format='%H:%M:%S', errors='coerce')
df_work.loc[:,'AST'] = pd.to_datetime(df_work.loc
           [:,'AST'], format='%H:%M:%S', errors='coerce')

#Choose filter 

while True:
    usr = input("select work type: ")
    if usr not in ["RM", "PM"]:
        usr = input("uknown file, hit enter to select file name")
        continue
    else:
        worktable = df_work[df_work.WorkType == 'RM']
    break
    
  

# Column selction calculation
worktable.loc[:,'comp_time'] = (worktable.loc[:,'AFT'] - worktable.loc[:,'AST']) * 24

worktable = worktable.loc[worktable.comp_time >= pd.Timedelta(0)]  #Remove negative time

tl_hrrm = worktable.loc[:, 'comp_time'].sum()

print(tl_hrrm)



