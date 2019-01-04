"""
Created on Thu Nov 29 10:27:15 2018

@author: prachi
"""
'''
This script reads the data for the new items fetched from the last 4 months which have been approved.
'''


#Import the required python modules
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk

#Read the data files having the Approved data from the last 4 months having PC_ITEM_ID and MCAT_ID
df = pd.read_csv("E:/BANNED/approved4mio.csv",engine='python')

#Sort the data according to MCAT IDs
df =df.sort_values(by=['MCAT_ID'])
df.reset_index(drop=True,inplace=True)



# Adding a new column having the status value as Approved
df["Status"] = "Approved"

#Remove the duplicates from the data on the basis of PC_ITEM_ID
df.drop_duplicates(subset=['PC_ITEM_ID'],inplace=True)



# Creating a pivot table which takes MCAT_ID as index and prints the number of PC_ITEM_ID's against each
df2 = df.pivot_table(index=['MCAT_ID'], values=['PC_ITEM_ID'], aggfunc='count', margins=True)




#Sorting the frequency pivot table in descending order
df2 = df2.sort_values(by=['PC_ITEM_ID'],ascending=False)




#Finding the MCAT_ID data where the frequency count is less than or equal to 10 PC_ITEM_ID's
df3=df2[df2['PC_ITEM_ID']<=10]




#Removing the extra row (1st row) i.e the sum of all frequencies
lessthan11=pd.DataFrame(df3[1:len(df3)])


# Taking the list of the MCAT_ID's from the above data
mcatswithlessthan11=list(lessthan11.index)


#Extracting all the data from the original dataframe where MCAT_ID is in the above list (i.e. has 10 or lesser items)
dfwithlessthan11=df[df['MCAT_ID'].isin(mcatswithlessthan11)]

#Saving the other data (i.e. having items greater than 10) into another dataframe
dfwithgreaterthan10=df[df['MCAT_ID'].isin(mcatswithlessthan11)==False]



# Creating an empty dataframe with required columns
finaldf = pd.DataFrame(columns=['PC_ITEM_ID', 'MCAT_ID', 'PC_ITEM_NAME', 'PC_ITEM_DESC_SMALL',
       'Status'])




#Appending the dataframe with mcat frequency less than 11 to this empty dataframe
finaldf = finaldf.append(dfwithlessthan11)




# Finding the unique values for mcat id's having greater than 10 frequency of PC_ITEM_ID's
uniquemcatswithgreaterthan10=list(dfwithgreaterthan10['MCAT_ID'].unique())




# taking up each of those unique MCAT ID's and appending only 10 PC_ITEM_ID's of each from the original total data to finaldf
for i in uniquemcatswithgreaterthan10:
    finaldf = finaldf.append(dfwithgreaterthan10[dfwithgreaterthan10['MCAT_ID']==i].head(10))



# Taking up backup of the finaldf into an excel file for future reference
finaldf.to_excel("E:/BANNED/approved_products4mo.xlsx")






#Downloading the inbuilt stopwords from the nltk in english language Python module
nltk.download('stopwords')
stop_words = stopwords.words('english')


#Adding other stopwords identified according to business requirements
stop_words.extend(("mg","mgs","ml","mls","kg","kgs","degree","degrees","g","gms","gm","mm","gram","grams","ft","cm","cms","m","cu","we","are","dealing","quality","manufacturers","manufacturer","exporters","supplier","dealer","good","topmost","business","trusted","finest","offer","offering","involved","provide","reputed","company","organization","trader","trading","li","pvt.","ltd","pvt","ltd."))




#saving finaldf as a new dataframe
Approved = finaldf





# Removing stopwords, special characters, punctuations and refining the description in Approved datafarme

Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[0-9] %', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[0-9]%', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[0-9]', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'<.*?>', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\/', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'/', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\.', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\'', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\"', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'x', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\+', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r',', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=' +', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r':', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r';', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'@', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'#', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\?', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\!', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\[', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\]', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\$', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\*', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\`', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\~', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'lwh', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'l w h', value=' ', regex=True,inplace=True)
    
    
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'&nbsp', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'&', value=' ', regex=True,inplace=True)
    
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=' +', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL']=Approved['PC_ITEM_DESC_SMALL'].str.lower()





Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[0-9] \\w+ *', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[0-9]\\w+ *', value=' ', regex=True,inplace=True)

Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
Approved['PC_ITEM_DESC_SMALL'].replace(to_replace=' +', value=' ', regex=True,inplace=True)




#Replacing nulls with blanks
Approved = Approved.replace(np.nan, '', regex=True)




# Removing stopwords:

Approved['Description1'] = Approved['PC_ITEM_DESC_SMALL'].apply(lambda x: [item for item in str(x).split() if item not in stop_words])
Approved['Description1'] = Approved['Description1'].apply(lambda x: ' '.join(map(str, x)))





# Creating test and label data for the same:

Approved['Test'] = Approved['PC_ITEM_NAME'].str.lower()+' '+Approved['Description1']
Approved['Test'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
Approved['Test'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
Approved['Test'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
Approved['Test'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
Approved['Test'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
Approved['Test'].replace(to_replace=' +', value=' ', regex=True,inplace=True)





Approved['Label'] = "__label__Approved"+" "+Approved['Test']



Approved.reset_index(drop=True,inplace=True)




# Exporting to excel_file 


Approved.to_excel("E:/BANNED/Approved_4mo_withlabel.xlsx")



# exporting txt file for training data which is having the 4months data as well



np.savetxt("E:\\BANNED\\Mapped and Approved prod/train4mo.txt",Approved['Label'],fmt='%s')





# Since avg banned products per kw is 121, so we will are taking 120 cut on approved products as well

finaldf2 = pd.DataFrame(columns=['PC_ITEM_ID', 'MCAT_ID', 'PC_ITEM_NAME', 'PC_ITEM_DESC_SMALL',
       'Status'])





# creating a data frame having the 11th PC_ITEM_ID for each MCAT_ID i.e to keep for test data

for i in uniquemcatswithgreaterthan10:
    finaldf2 = finaldf2.append(dfwithgreaterthan10[dfwithgreaterthan10['MCAT_ID']==i].iloc[10])








# Removing stopwords, special characters, punctuations and symbols from description

finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[0-9] %', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[0-9]%', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[0-9]', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'<.*?>', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\/', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'/', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\\', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\.', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\'', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\"', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'x', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\+', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r',', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=' +', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r':', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r';', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'@', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'#', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\?', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\!', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\[', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\]', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\$', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\*', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\`', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\~', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'lwh', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'l w h', value=' ', regex=True,inplace=True)
    
    
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'&nbsp', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'&', value=' ', regex=True,inplace=True)
    
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=' +', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL']=finaldf2['PC_ITEM_DESC_SMALL'].str.lower()





finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[0-9] \\w+ *', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[0-9]\\w+ *', value=' ', regex=True,inplace=True)

finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
finaldf2['PC_ITEM_DESC_SMALL'].replace(to_replace=' +', value=' ', regex=True,inplace=True)




# Removing stopwords, special characters, punctuations and symbols from description
finaldf2['Description1'] = finaldf2['PC_ITEM_DESC_SMALL'].apply(lambda x: [item for item in str(x).split() if item not in stop_words])
finaldf2['Description1'] = finaldf2['Description1'].apply(lambda x: ' '.join(map(str, x)))





# Creating test and label data for the same:

finaldf2['Test'] = finaldf2['PC_ITEM_NAME'].str.lower()+' '+finaldf2['Description1']
finaldf2['Test'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
finaldf2['Test'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
finaldf2['Test'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
finaldf2['Test'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
finaldf2['Test'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
finaldf2['Test'].replace(to_replace=' +', value=' ', regex=True,inplace=True)





finaldf2['Label'] = "__label__Approved"+" "+finaldf2['Test']



finaldf2.to_excel("E:/BANNED/Approved_4mo_test.xlsx")




#Saving text files for label,test and item_id's
np.savetxt("E:\\BANNED\\Mapped and Approved prod/test4mo_label.txt",finaldf2['Label'],fmt='%s')

np.savetxt("E:\\BANNED\\Mapped and Approved prod/test4mo.txt",finaldf2['Test'],fmt='%s')


np.savetxt("E:\\BANNED\\Mapped and Approved prod/test_itemid.txt",finaldf2['PC_ITEM_ID'],fmt='%d')




