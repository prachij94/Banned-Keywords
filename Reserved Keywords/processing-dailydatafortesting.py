# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:45:36 2019

@author: prachi
"""

import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk

#Downloading the common english language stopwords from the nltk module in Python
nltk.download('stopwords')
stop_words = stopwords.words('english')


#Adding the extra stopwords identified as per business use-case into the above set 
stop_words.extend(("for medicine","medicine","for medicines","medicines","mg","mgs","ml","mls","kg","kgs","degree","degrees","g","gms","gm","mm","gram","grams","ft","cm","cms","m","cu","we","are","dealing","quality","manufacturers","manufacturer","exporters","supplier","dealer","good","topmost","business","trusted","finest","offer","offering","involved","provide","reputed","company","organization","trader","trading","li","pvt.","ltd","pvt","ltd."))


#This function removes all the undesired punctuations, special characters,digits,extra spaces,etc from the Description column of the data 
def refine_description(DescriptionColumn):
    
    

    
    DescriptionColumn.replace(to_replace=r'[0-9] \\w+ *', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'[0-9]+ *$', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'[0-9]\\w+ *', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'[0-9] %', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'[0-9]%', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'[0-9]', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'<.*?>', value=' ', regex=True,inplace=True)
    
    DescriptionColumn.replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\/', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'/', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\.', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'-', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\'', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\"', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'x', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\+', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r',', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=' +', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r':', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r';', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'@', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'#', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\?', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\!', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\[', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\]', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\$', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\*', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\`', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'\~', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'lwh', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'l w h', value=' ', regex=True,inplace=True)
    
    
    DescriptionColumn.replace(to_replace=r'&nbsp', value=' ', regex=True,inplace=True)
    DescriptionColumn.replace(to_replace=r'&', value=' ', regex=True,inplace=True)
    
    DescriptionColumn.replace(to_replace=' +', value=' ', regex=True,inplace=True)
    DescriptionColumn=DescriptionColumn.str.lower()
    




#Read the Totaldata keywords product data from the csv file
Totaldata = pd.read_excel("BanLog-01-01-19.xlsx")

#Replacing all the empty values with blanks
Totaldata = Totaldata.replace(np.nan, '', regex=True)


#Calling the above function for refining the Description column
refine_description(Totaldata['Actual Text'].str.lower())

Totaldata['Actual Text']=Totaldata['Actual Text'].str.lower()
#Removing the stopwords identified above from the Description column
Totaldata['Actual Text'] = Totaldata['Actual Text'].apply(lambda x: [item for item in str(x).split() if item not in stop_words])
Totaldata['Actual Text'] = Totaldata['Actual Text'].apply(lambda x: ' '.join(map(str, x)))




np.savetxt('01jan19_desc.txt',Totaldata['Actual Text'],fmt='%s')
np.savetxt('01jan19_offerids.txt',Totaldata['Offer Id'],fmt='%d')













