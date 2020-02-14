# Banned Content detection model

An ecommerce platform involves daily transactions of a huge amount of data about users and products. It becomes vital to check that no illegal content as per the country's legal norms is added or available for sale on the portal. In this project, our purpose is to predict beforehand whether a product should be ***'Approved'*** or ***'Banned'***. 

A supervised text-based classifier is created using **fastText** to train our model. [fastText](https://fasttext.cc/) is an open source library from Facebook for efficient learning of word representations and sentence classification.



**Getting and preparing the data:**

A large chunk of historical product data (approx. in few lacs), which includes approved as well as banned products, is collected and processed to train the model so that later, the model can be utilised to get predictions on new data.
The approach followed here for processing the input text strings considers basic product characteristics like **product name, product description and its specifications values(for example,color,weight,size,etc whatever has been filled by seller)**. The combination of these particular text pointers has been selected to ensure that each product is trained with its appropriate label and confusion is avoided in ambiguous cases.For example, _a tiger soft toy_ should be Approved while _a tiger_ should be Banned where _'tiger'_ is a banned keyword already present in our banned database.


A training text string is created by concatenating lowercase product name, product description and its specifications values. Then the above string is cleaned by removing extra spaces,duplicate words,punctuations, special characters,digits, generally observed stopwords for products like _offering,leading,services,cm,gm,kg_,etc.

All the labels start by the `__label__` prefix, which is how fastText recognises what is a label or what is a word. The model is then trained to predict the labels given the word in the document.
The syntax of each training string for fastText is like:
```
__label__<class1> <training sentence>
```
So, the above cleaned string is concatenated with the approved/banned keyword identified(if any) and then finally appended to their respective appropriate label i.e. ***'Approved'*** or ***'Banned'***,

for example, 

__label__Approved cow milk pasteurised bottle

__label__Banned cowhide leather brown

Some python scripts for label creation purpose in this repository are *ApprovedAndRejectLabelPreparation.py*, *LabelPreparationwitholdAnd4MonthData.py*,*dataprocessing.py*,etc.

Regular updation of the training data with newly identified reserved keywords i.e. use-case specific stopwords can be done with the script *Reserved Keywords/processing-addingReservedKWtoOlddata.py*




When the labelling is complete, the train and test .txt files ( 90% train and 10% test data in this case) can be obtained using the script *SegregationForTrainingAndTestingData.py*

The below steps show how to use fastText in python for creating a supervised model with your own training file and custom hyperparameter values.



Install fastText from command line:
```
$ git clone https://github.com/facebookresearch/fastText.git
$ cd fastText
$ pip install .
```



Python script:
```
import fastText

train_file_name = "training_model.txt"
model_name = "Banned_Model"

classifier = fasttext.train_supervised(str(train_file_name),
                                            str(model_name), label_prefix='__label__',
                                            epoch=75,lr=0.5,word_ngrams=2,minn 5,bucket=200000,dim=100,loss='hs')
# To Save the model for further use:
classifier.save_model("Banned_Model.bin")
# To Predict the classes/Labels from the above model
model = fastText.load_model(model_name+".bin")
Test_String = ['xyz']
Model_Results = model.predict(Test_String,k=1)[0][0][0]     #uses k fold cross validation
```
The predict() outputs the resultant label i.e. __label__Approved or __label__Banned for the test string. Thus, the model(i.e. the .bin file) can be saved and used for predictions from different validation sets and hence, record the [Precision and Recall](https://en.wikipedia.org/wiki/Precision_and_recall).




**Improving the accuracy:**

Run multiple permutations and combinations on the above hyperparameters (*Learning Rate(LR),wordN-grams, Character_nGrams(minn), Number of iterations(epoch), etc.*) while training the model and then select the best among them. 
Use the below commands to get models with multiple combinations of tuning parameters.
```
while read p; do while read q; do while read r; do while read s; do fasttext  supervised -input ~/Desktop/Banned_Model/train.txt -output ~/Desktop/Banned_Model/hypertuned/$p.$q.$r.$s -lr $p -minn $q -epoch $r -wordNgrams $s -thread 4 -loss hs -lrUpdateRate 100; done ; done
```
At this stage, we have created more than 2k unique models. Next step, select the best one among them. The testing command to select the best model based on its precision, recall, and accuracy when tested with the same test dataset is as follows:
```
for b in ~/Desktop/Banned_Model/hypertuned/*.bin ;do ( echo Test results with $b && fasttext test $b /home/Desktop/test\val.txt ); done >> /home/Desktop/banned_hyper_parameters_test.txt
```
Using this approach we should be able to select the best model based on the most suitable combination of hyper-parameters. These hyper-parameters may vary from one use case to another.

At this stage, the model is generally able to predict correctly at a high accuracy rate which can be confirmed when verified with a human auditor. The finalized banned keywords model can be saved it as a ‘.bin’ file and tested or updated whenever required. 


## Requirements:

fastText builds on modern Mac OS and Linux distributions. Since it uses C++11 features, it requires a compiler with good C++11 support. These include :

- (gcc-4.6.3 or newer) or (clang-3.3 or newer)
- python 2.6 or newer
