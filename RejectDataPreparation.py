# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:07:23 2018

@author: prachi
"""

import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
stop_words = stopwords.words('english')

stop_words.extend(("mg","mgs","ml","mls","kg","kgs","degree","degrees","g","gms","gm","mm","gram","grams","ft","cm","cms","m","cu","we","are","dealing","quality","manufacturers","manufacturer","exporters","supplier","dealer","good","topmost","business","trusted","finest","offer","offering","involved","provide","reputed","company","organization","trader","trading","li","pvt.","ltd","pvt","ltd."))

def refine_description(smallDesc):
    
    

    
    Banned['Description1'].replace(to_replace=r'[0-9] \\w+ *', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'[0-9]\\w+ *', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'[0-9] %', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'[0-9]%', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'[0-9]', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'<.*?>', value=' ', regex=True,inplace=True)
    
    Banned['Description1'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\/', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'/', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\.', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\'', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\"', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'x', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\+', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r',', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=' +', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r':', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r';', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'@', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'#', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\?', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\!', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\[', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\]', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\$', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\*', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\`', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'\~', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'lwh', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'l w h', value=' ', regex=True,inplace=True)
    
    
    Banned['Description1'].replace(to_replace=r'&nbsp', value=' ', regex=True,inplace=True)
    Banned['Description1'].replace(to_replace=r'&', value=' ', regex=True,inplace=True)
    
    Banned['Description1'].replace(to_replace=' +', value=' ', regex=True,inplace=True)
    Banned['Description1']=Banned['Description1'].str.lower()
    

Banned = pd.read_csv("testrej.csv",sep="\t", engine='python',error_bad_lines=False, header=None,names=['Item_ID','Item_Name','Display_ID','BannedKW','Description1'])

Banned = Banned.replace(np.nan, '', regex=True)
#Banned2= Banned.merge(Total,how='left',on='Item_ID')

refine_description(Banned['Description1'].str.lower())

Banned['Description1'] = Banned['Description1'].apply(lambda x: [item for item in str(x).split() if item not in stop_words])
Banned['Description1'] = Banned['Description1'].apply(lambda x: ' '.join(map(str, x)))

Banned['Label'] = "__label__Rejected"+ ' '+Banned['Item_Name'].str.lower()+Banned['Description1']
Banned['Test'] = Banned['Item_Name'].str.lower()+Banned['Description1']

Banned.to_csv('RejectDataLabels.csv',index=False)
