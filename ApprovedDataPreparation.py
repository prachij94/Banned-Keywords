# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:01:09 2018

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
    
    

    
    Approved['Description1'].replace(to_replace=r'[0-9] \\w+ *', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'[0-9]\\w+ *', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'[0-9] %', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'[0-9]%', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'[0-9]', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'<.*?>', value=' ', regex=True,inplace=True)
    
    Approved['Description1'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\/', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'/', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\.', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\'', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\"', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'x', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\+', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r',', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=' +', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r':', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r';', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'@', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'#', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\?', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\!', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\[', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\]', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\$', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\*', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\`', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'\~', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'lwh', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'l w h', value=' ', regex=True,inplace=True)
    
    
    Approved['Description1'].replace(to_replace=r'&nbsp', value=' ', regex=True,inplace=True)
    Approved['Description1'].replace(to_replace=r'&', value=' ', regex=True,inplace=True)
    
    Approved['Description1'].replace(to_replace=' +', value=' ', regex=True,inplace=True)
    Approved['Description1']=Approved['Description1'].str.lower()
    

Approved = pd.read_csv("newapp.csv",sep="\t", engine='python',error_bad_lines=False, header=None,names=['Item_ID','Item_Name','Display_ID','ApprovedKW','Description1'])

Approved = Approved.replace(np.nan, '', regex=True)
#Approved2= Approved.merge(Total,how='left',on='Item_ID')

refine_description(Approved['Description1'].str.lower())

Approved['Description1'] = Approved['Description1'].apply(lambda x: [item for item in str(x).split() if item not in stop_words])
Approved['Description1'] = Approved['Description1'].apply(lambda x: ' '.join(map(str, x)))

Approved['Label'] = "__label__Approved"+ ' '+Approved['Item_Name'].str.lower()+Approved['Description1']
Approved['Test'] = Approved['Item_Name'].str.lower()+Approved['Description1']

Approved=Approved[Approved['Item_ID'].str.isdigit()]
Approved.reset_index(drop=True,inplace=True)

Approved.to_csv('ApprovedDataLabels.csv',index=False)
