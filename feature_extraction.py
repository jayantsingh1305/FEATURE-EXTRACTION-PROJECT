import pandas as pd 
import numpy as np

df = pd.read_csv('anime.csv')

#make a new column for episode count
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

#make a new column for the time stamp
def extraction_time(txt):
    check = False
    data = ""
    for i in range(len(txt)):
        if txt[i] == ')':
            for j in range(i+1, i+20):
                data += txt[j]

            return data
        
df['Total Time'] = df['Title'].apply(extraction_time)

#which anime has the highest score 
df["score"] = pd.to_numeric(df["Score"])
df = df.dropna(subset=["Score"])
max_score = df["Score"].max()
top_rows = df[df["Score"] == max_score][["Rank","Title","Score"]]
print("Max Score:", max_score)
print(top_rows)

#give me top 5 highesr scoring anime
df_sorted = df.sort_values(by="Score", ascending=False)
top5 = df_sorted.head(5)[["Rank","Title","Score"]]
print(top5)

#which anime has the highest episode count
df["Episodes"] = pd.to_numeric(df["Episodes"],errors="coerce")
df = df.dropna(subset=["Episodes"])

top = df.loc[df["Episodes"].idxmax(),["Rank","Title","Score","Episodes"]]
print(top)

#animes with top 5 episode count
top5_eps = (
    df.sort_values(by=["Episodes", "Title"], ascending=[False, True])
      .head(5)[["Rank", "Title", "Score", "Episodes"]]
)
print(top5_eps)

#which is the longest running anime
max_ep = df["Episodes"].max()
longest_running = df[df["Episodes"] == max_ep][["Title", "Episodes", "Rank", "Score"]]
print("Max Episodes:", max_ep)
print(longest_running)

print(df)

