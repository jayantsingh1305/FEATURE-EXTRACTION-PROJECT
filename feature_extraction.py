import pandas as pd 
import numpy as np

df = pd.read_csv('anime.csv')

#EPISODE EXTRACTION
def extract_episodes(txt):
    check = False
    data = ""
    for i in txt :
        if i == ")":
            check = False 
            return data
        if check == True:
            data = data + i
        if i =='(':
            check = True

df["Episodes"] = df["Title"].apply(extract_episodes)
df["Episodes"] = df["Episodes"].str.replace("eps","")
df["Episodes"] = df["Episodes"].astype(int)

#TIME STAMP EXTRACTION
def extraction_time(txt):
    check = False
    data = ""
    for i in range(len(txt)):
        if txt[i] == ')':
            for j in range(i+1, i+20):
                data += txt[j]

            return data
        
df['Total Time'] = df['Title'].apply(extraction_time)

print(df)