# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:53:03 2018

@author: prachi
"""
'''
This script creates the training and testing text files from the combined randomised data of both approved and banned data. 

'''

#Import the required python modules
from sklearn.utils import shuffle
import numpy as np
import pandas as pd
import math


#Read the data files having the Approved and Rejected Labels column
df1 = pd.read_excel("ApprovedDataLabels.xlsx",header=None)
df2 = pd.read_excel("RejectDataLabels.xlsx",header=None)


#Create a new empty dataframe and add the above two dataframes into it
df3 = pd.DataFrame()
df3 = df3.append(df1,ignore_index=True)
df3 = df3.append(df2,ignore_index=True)


#Remove the first two dataframes now to release memory held by them
del(df1,df2)


#Naming the columns in the new combined dataframe
df3.columns = ['Item_ID', 'Item_Name', 'Display_ID', 'SuspectedKW', 'Description1','Label', 'Test']


#Shuffling the data to randomize the rows of approved and rejected labels
df3 = shuffle(df3)
df3.reset_index(drop=True,inplace=True)


#Finding the 90% and 10% cut row index from the data
part1 = math.ceil(len(df3)*0.9)
part2 = len(df3)-part1

#Separating the data into two dataframes viz. 90 and 10 cut i.e. for 90% data for training the model and 10% kept for testing
df4 = df3.head(part1)
df5= df3.tail(part2)

df4.reset_index(drop=True,inplace=True)
df5.reset_index(drop=True,inplace=True)


#Exporting the final data for 90% and 10% cut i.e. kept for training and testing purpose - For future reference
df4.to_excel('Datawith90cut.xlsx',index=False)
df5.to_excel('Datawith10cut.xlsx',index=False)



#Refining the Label column in the training data and test column in the testing data by removing special symbols,etc
df4['Label'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
df4['Label'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
df4['Label'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
df4['Label'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
df4['Label'].replace(to_replace=r',', value=' ', regex=True,inplace=True)
df4['Label'].replace(to_replace=r'\/', value=' ', regex=True,inplace=True)
df4['Label'].replace(to_replace=r':', value=' ', regex=True,inplace=True)
df4['Label'].replace(to_replace=r'}', value=' ', regex=True,inplace=True)
df4['Label'].replace(to_replace=r'{', value=' ', regex=True,inplace=True)
df4['Label'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
df4['Label'].replace(to_replace=' +', value=' ', regex=True,inplace=True)

df5['Test'].replace(to_replace=r'\%', value=' ', regex=True,inplace=True)
df5['Test'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
df5['Test'].replace(to_replace=r'\(', value=' ', regex=True,inplace=True)
df5['Test'].replace(to_replace=r'\)', value=' ', regex=True,inplace=True)
df5['Test'].replace(to_replace=r',', value=' ', regex=True,inplace=True)
df5['Test'].replace(to_replace=r'\/', value=' ', regex=True,inplace=True)
df5['Test'].replace(to_replace=r':', value=' ', regex=True,inplace=True)
df5['Test'].replace(to_replace=r'}', value=' ', regex=True,inplace=True)
df5['Test'].replace(to_replace=r'{', value=' ', regex=True,inplace=True)
df5['Test'].replace(to_replace=r'[[:punct:]]', value=' ', regex=True,inplace=True)
df5['Test'].replace(to_replace=' +', value=' ', regex=True,inplace=True)


#Saving the Label column from the training data(90% cut) as a text file to be used in fasttext
np.savetxt("train.txt",df4['Label'],fmt='%s')


#Saving the Test and Item_ID column from the testing data(10% cut) as a text file to be used in fasttext
np.savetxt("test.txt",df5['Test'],fmt='%s')

np.savetxt("Item_ID.txt",df5['Item_ID'],fmt='%d')

