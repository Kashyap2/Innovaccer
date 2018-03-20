import re
import pandas as pd
import numpy as np
import datetime as dt
df = pd.read_csv('dp.csv')
#df.head()

# primary key

df['primary_key'] = '000000'

for i in range(0,len(df)):
        f_name = df.loc[i][3]
        f_words = f_name.split()
        f_letters = [word[0] for word in f_words]
        f_key = f_letters[0]
        #f_key = "".join(f_letters)
        #print(f_letters)
        
        l_name = df.loc[i][0]
        l_words = l_name.split()
        l_letters = [word[0] for word in l_words]
        l_key = l_letters[0]
        #l_key = "".join(l_letters)
        #print(l_key)
        
        dob = df.loc[i][1]
        dob_key = re.sub('-','',dob)
        
        #print(dob_key)
        gen_key = df.loc[i][2]
        df.loc[i][4] = gen_key+l_key+dob_key+f_key
        
        print(df.loc[i][4])
                
df_final = df.drop_duplicates(subset='primary_key', keep="first")


