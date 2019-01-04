# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:27:15 2018

@author: prachi
"""
'''
This script reads the input data for Approved and Rejected Products which includes details like Item_ID ,Item_Name ,Display_ID, (Approved or Banned Keyword) and the Description.

We then refine the Description field to remove any stopwords (like some words identified below) and remove any special characters or digits which can otherwise result in our training data being biased for some words.

Lastly, the script adds a column Label to the original data which joins the __label__Approved and __label__Rejected to the respective corresponding Item_name and Description.
Then, the updated data is loaded down into a csv file.

'''
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
    




#Read the approved keywords product data from the csv file
Approved = pd.read_csv("newapp.csv",sep="\t", engine='python',error_bad_lines=False, header=None,names=['Item_ID','Item_Name','Display_ID','ApprovedKW','Description1'])

#Replacing all the empty values with blanks
Approved = Approved.replace(np.nan, '', regex=True)


#Calling the above function for refining the Description column
refine_description(Approved['Description1'].str.lower())


#Removing the stopwords identified above from the Description column
Approved['Description1'] = Approved['Description1'].apply(lambda x: [item for item in str(x).split() if item not in stop_words])
Approved['Description1'] = Approved['Description1'].apply(lambda x: ' '.join(map(str, x)))


#Creating a new column Test which is a collection of the item name(in lowercase) and the final refined Description
Approved['Test'] = Approved['Item_Name'].str.lower()+' '+Approved['Description1']

#Removing some frequent characters found in the Item names like %,-,(,),',',etc
Approved['Test'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
Approved['Test'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
Approved['Test'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
Approved['Test'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
Approved['Test'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
Approved['Test'].replace(to_replace=' +', value=' ', regex=True,inplace=True)


#Creating a column label for Approved Data which begins with the label as __label__Approved
Approved['Label'] = "__label__Approved"+ ' '+Approved['Test']
Approved=Approved[Approved['Item_ID'].str.isdigit()]
Approved=Approved[Approved['ApprovedKW'] != '']
Approved.reset_index(drop=True,inplace=True)


#Exporting the final data into a csv file
Approved.to_csv('ApprovedDataLabels.csv',index=False)






''' Similarly for the Banned Keywords data:
    '''
    
    

#Read the banned keywords product data from the csv file
Banned = pd.read_csv("testrej.csv",sep="\t", engine='python',error_bad_lines=False, header=None,names=['Item_ID','Item_Name','Display_ID','BannedKW','Description1'])

#Replacing all the empty values with blanks
Banned = Banned.replace(np.nan, '', regex=True)

#Calling the above function for refining the Description column
refine_description(Banned['Description1'].str.lower())

#Removing the stopwords identified above from the Description column
Banned['Description1'] = Banned['Description1'].apply(lambda x: [item for item in str(x).split() if item not in stop_words])
Banned['Description1'] = Banned['Description1'].apply(lambda x: ' '.join(map(str, x)))

#Creating a new column Test which is a collection of the item name(in lowercase) and the final refined Description
Banned['Test'] = Banned['Item_Name'].str.lower()+' '+Banned['Description1']


#Removing some frequent characters found in the Item names like %,-,(,),',',etc
Banned['Test'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
Banned['Test'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
Banned['Test'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
Banned['Test'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
Banned['Test'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
Banned['Test'].replace(to_replace=' +', value=' ', regex=True,inplace=True)


#Creating a column label for Rejected Data which begins with the label as __label__Rejected
Banned['Label'] = "__label__Rejected"+ ' '+Banned['Test']
Banned=Banned[Banned['Item_ID'].str.isdigit()]
Banned=Banned[Banned['BannedKW'] != '']
Banned.reset_index(drop=True,inplace=True)

#Exporting the final data into a csv file
Banned.to_csv('RejectDataLabels.csv',index=False)





















