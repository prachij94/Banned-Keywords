# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:55:58 2019

@author: prachi
"""

import pandas as pd
import numpy as np

    





''' Similarly for the Banned Keywords data:
    '''
    
    

#Read the banned keywords product data from the csv file
Banned = pd.read_csv("reservedkw.csv",sep="\t", engine='python')
Banned = pd.DataFrame(Banned['RESERVED_KEYWORDS'].str.lower())
#Replacing all the empty values with blanks
Banned = Banned.replace(np.nan, '', regex=True)





#Creating a column label for Rejected Data which begins with the label as __label__Rejected
Banned['Label'] = "__label__Rejected"+ ' '+Banned['RESERVED_KEYWORDS']

Banned.reset_index(drop=True,inplace=True)

#Exporting the final data into a csv file
Banned.to_csv('RejectDataLabels.csv',index=False)

np.savetxt("C:\\Users\\prachi\Desktop\\reseredkwlabels.txt",Banned['Label'],fmt='%s')
count = Banned['RESERVED_KEYWORDS'].str.split(' ').apply(len).value_counts()

count =  Banned['RESERVED_KEYWORDS'].str.split().str.len()
count.index = count.index.astype(str) + ' words:'
count.sort_index(inplace=True)
count

sum(count==1)

existingdata = pd.read_csv('final_training_data-set2.txt',sep="\t", engine='python',error_bad_lines=False,header=None,names=['Data'])
reservedlabels = pd.DataFrame(Banned['Label'])
reservedlabels.rename(columns={'Label':'Data'},inplace=True)
for i in range(0,10):
    existingdata = pd.concat([existingdata,reservedlabels])
    #existingdata = pd.DataFrame(existingdata['Data'])
    #existingdata = pd.concat([existingdata['0'],Banned['Label']])
    existingdata.reset_index(drop=True,inplace=True)

np.savetxt("C:\\Users\\prachi\Desktop\\banned_kw-final_training_08_01_19.txt",existingdata['Data'],fmt='%s')
