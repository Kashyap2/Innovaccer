
from fuzzywuzzy import fuzz
import re
import pandas as pd
import numpy as np
import datetime as dt
import math
df = pd.read_csv('dp.csv')

def count_dict(mystring):
    d = {}
    x=0
# count occurances of character
    for w in mystring: 
        d[w] = mystring.count(w)
    for k in sorted(d):
        x = x + d[k]
    
    return math.ceil(x/2) 
    


'''
f_name = df.loc[0][3]
f_key = f_name[:count_dict(f_name)]
l_name = df.loc[0][0]
l_key = l_name[0]
dob = df.loc[0][1]
dob_key = re.sub('-','',dob)
gen_key = df.loc[0][2]

primary_key = f_key+l_key+dob_key+gen_key
fuzz.ratio(primary_key,f_key+l_key )
'''



df['primary_key'] = '000000'
df.head()   




for i in range(0,len(df)):
        f_name = df.loc[i][3]
        f_key = f_name[:count_dict(f_name)]
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



match_ratio = np.zeros((len(df), len(df)))
repeat = pd.DataFrame(np.zeros((1000,2 )))
m=0

for i in range(0, (len(df)-1)):
    for j in range(0,(len(df)-1)):
        match_ratio[i][j] = fuzz.ratio(df.loc[i][4],df.loc[j][4])
        if(match_ratio[i][j]>90):
            if(j>i):
                print(str(i)+ 'and' + str(j)+ 'are same with matching ratio'+str(match_ratio[i][j]))
                
                repeat.loc[m][0] = j
                m=m+1
            




colnames = list(df.loc[:]['primary_key'])
print(colnames)
pd.DataFrame(match_ratio,columns=colnames).to_csv('match_ratio.csv')




