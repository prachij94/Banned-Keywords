"""
Created on Thu Nov 29 10:27:15 2018

@author: prachi
"""
'''
This script reads the previous data for the approved and rejected items(without the new 4 months data) and concatenates and shuffles into a new dataframe after load balancing (i.e. because of the data length difference in both, we have concatenated reject data 3 times to match up with the length of approved data alone)

We then take the 90% and 10% cuts of data and save for training and testing purposes respectively.


Later, we prepare the training, testing and item id text files with the help of the following data:

1.We had created a unique rejected keywords data from the previous reject data and then prepared labels from it.

2.Labels prepared from the products data added in last 4 months which have been approved.

3. Taking the labels from the 90% cut data above
'''

#Import the required python modules
import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import math



#Reading the Reject Data having labels which we prepared initially
rejectkw = pd.read_excel("E:\BANNED\RejectDataLabels.xlsx",sheet_name="Sheet1")


# Refine the Banned /keywords column by removing special characters
rejectkw['BannedKW'].replace(to_replace=r'\+', value=' ', regex=True,inplace=True)
rejectkw['BannedKW'].replace(to_replace=r'-', value=' ', regex=True,inplace=True)
rejectkw['BannedKW'].replace(to_replace=r' +', value=' ', regex=True,inplace=True)


#Taking the rejected/banned keywords into a list 
rejectedkwlist=list(rejectkw['BannedKW'].str.lower())



#Creating an empty dataframe to add the unique rejected/banned keywords and create labels with it
rejectkwlabels = pd.DataFrame()


rejectedkwlist2=[]


#Creating labels in the unique rejected keywords list
for i in rejectedkwlist:
    rejectedkwlist2.append("__label__Rejected"+" "+str(i))



#Saving the above reject keywords list as a dataframe
rejectkwlabels=pd.DataFrame(rejectedkwlist2)


# Reading the approved data
approveddatalabels = pd.read_excel("E:\BANNED\ApprovedDataLabels1.xlsx",sheet_name="Sheet1")



#Read the 4 months products labels data created earlier
approveddata4mon = pd.read_excel("E:\BANNED\Approved_4mo_withlabel.xlsx")


#An empty dataframe to append the required datasets
totaldf = pd.DataFrame()



#Renaming the approved and rejected data to make the 'BannedKeyword' and 'ApprovedKW' columns same having name 'Keyword' 
approveddatalabels.columns = ['Item_ID', 'Item_Name', 'Display_ID', 'Keyword', 'Description1','Label', 'Test']


rejectkw.columns = ['Item_ID', 'Item_Name', 'Display_ID', 'Keyword', 'Description1',
       'Label', 'Test']


#Adding the approved data and rejected keywords data(3 times) to the empty dataframe
totaldf = pd.concat([totaldf,approveddatalabels[['Item_ID','Label','Test','Keyword']],rejectkw[['Item_ID','Label','Test','Keyword']],rejectkw[['Item_ID','Label','Test','Keyword']],rejectkw[['Item_ID','Label','Test','Keyword']]])


#Shuffling the data
totaldf=shuffle(totaldf)

#Resetting the indices in the dataframe after shuffling
totaldf.reset_index(drop=True,inplace=True)



#Finding the 90% and 10% cut in the above data
part1 = math.ceil(len(totaldf)*0.9)
part2 = len(totaldf)-part1

data90 = totaldf.head(part1)
data10= totaldf.tail(part2)

data90.reset_index(drop=True,inplace=True)
data10.reset_index(drop=True,inplace=True)


# Saving the data with 90% cut and 10% cut as excel files
data90.to_excel('E:\BANNED\Datawith90cutNew.xlsx',index=False)
data10.to_excel('E:\BANNED\Datawith10cutNew.xlsx',index=False)







#Now creating a new dataset having - labels of the data with 90% cut, approved 4 months data labels and the rejected keywords labels
new4molabelsandRejectlabels = pd.concat([data90['Label'],approveddata4mon['Label'],rejectkwlabels])



# Saving this data as training data which contains the 4 month data
np.savetxt("trainwith4monData.txt",new4molabelsandRejectlabels,fmt='%s')


#Saving testing data with the 10% data cut as train,test and item_id files
np.savetxt("testwith4monDataLabel.txt",data10['Label'],fmt='%s')

np.savetxt("testwith4monData.txt",data10['Test'],fmt='%s')


np.savetxt("ItemIDwith4monData.txt",data10['Item_ID'],fmt='%d')

