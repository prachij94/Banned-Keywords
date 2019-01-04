# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:19:45 2018

@author: prachi
"""
import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
import nltk
import string
import os

nltk.download('stopwords')
stop_words = stopwords.words('english')

stop_words.extend(("we","are","dealing","quality","manufacturers","manufacturer","exporters","supplier","dealer","good","topmost","business","trusted","finest","offer","offering","involved","provide","reputed","company","organization","trader","trading","li","pvt.","ltd","pvt","ltd."))

def refine_description(smallDesc):
    
    

    
    df2['Description+ISQ'].replace(to_replace=r'[0-9] \\w+ *', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'[0-9]\\w+ *', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'[0-9] %', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'[0-9]%', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'[0-9]', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'<.*?>', value=' ', regex=True,inplace=True)
    
    df2['Description+ISQ'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'\/', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'/', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'\.', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'\'', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'\"', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'x', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'\+', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r',', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=' +', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r':', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r';', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
    
    df2['Description+ISQ'].replace(to_replace=r'&nbsp', value=' ', regex=True,inplace=True)
    df2['Description+ISQ'].replace(to_replace=r'&', value=' ', regex=True,inplace=True)
    
    df2['Description+ISQ'].replace(to_replace=' +', value=' ', regex=True,inplace=True)
    df2['Description+ISQ']=df2['Description+ISQ'].str.lower()
    #return smallDesc
    
 
def remove_duplicates(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
    
def removeStopWords(word):
    tokenized_word = word.split()
    list_of_word = []
    [list_of_word.append(word) for word in tokenized_word if word not in stop_words]
    finalWord = " ".join(list_of_word)
    
    return finalWord

df1=pd.read_csv('C:/Users/prachi/Desktop/BannedKeywords/testrej.csv',error_bad_lines=False,header=None,sep ="\n")
df1=df1.head(50000)
df1.drop(list(range(10,len(df1.columns))),axis=1,inplace=True)
df1.columns=['PCID','Description','ISQ1','ISQ2','ISQ3','ISQ4','ISQ5','ISQ6','ISQ7','ISQ8']
#'ISQ9','ISQ10','ISQ11','ISQ12','ISQ13']
df1.dropna(how='all',inplace=True)
df1.reset_index(drop=True,inplace=True)

df1 = df1.replace(np.nan, '', regex=True)
df2=df1['PCID'].str.split(pat='\t', n=-1, expand=True)
df2 = df2.replace(np.nan, '', regex=True)
df2.columns= ['Item_ID','Item_Name','Display_ID','BannedKW','Description1','name']
df2.drop([5,6,7],axis=1,inplace=True)
df2['Description2']=df1['Description']
df2 = df2.replace(np.nan, '', regex=True)
df2['Description']=df2['Description1']+df2['Description2']
df2.drop(['Description1','Description2'],axis=1,inplace=True)
df2['ISQ'] = df1['ISQ1']+df1['ISQ2']+df1['ISQ3']+df1['ISQ4']+df1['ISQ5']+df1['ISQ6']+df1['ISQ7']+df1['ISQ8']
#+df1['ISQ9']+df1['ISQ10']+df1['ISQ11']+df1['ISQ12']+df1['ISQ13']
df2.columns= ['Item_ID','Item_Name','Display_ID','BannedKW','Description','ISQ']


del(df1)


df2['Description+ISQ']=df2['Description']+df2['ISQ']
df2.drop(['Description','ISQ'],axis=1,inplace=True)

#x=refine_description(df2['Description+ISQ'].str)



refine_description(df2['Description+ISQ'].str.lower())

# df2['Label'] = "__label__Reject_"+ df2['BannedKW']+' '+df2['Item_Name'].str.lower()+df2['Description+ISQ']
df2['Label'] = "__label__Reject"+ ' '+df2['Item_Name'].str.lower()+df2['Description+ISQ']
df2['Test'] = df2['Item_Name'].str.lower()+df2['Description+ISQ']

#df2.to_csv('RejectedLabelled.csv',index=False)


os.getcwd()


df_rej = pd.read_csv("C:/Users/prachi/Desktop/BannedKeywords/RejectedLabelled.csv")

