import numpy as np
import pandas as pd
import random

import cv2
import os

# Preparing test and training CSV

root_dir='/content/drive/MyDrive/BYOL-ViT-Hourglass/STL10'
images_dir=os.path.join(root_dir,'img')

data_dir_list=os.listdir(images_dir)
print('The data list is:', data_dir_list)

# Assigning label to each category

num_classes=10
#num_classes=5
#num_classes=2
#label_name={'n01440764':0,'n02102040':1,'n02979186':2,'n03000684':3,'n03028079':4,'n03394916':5,'n03417042':6,'n03425413':7,'n03445777':8,'n03888257':9}
#label_name={'airplane':0,'bird':1,'car':2,'cat':3,'gazelle':4,'boat':5,'dog':6,'horse':7,'monkey':8,'truck':9 }
label_name={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10 }
#label_name={'boat':0,'dog':1,'horse':2,'monkey':3,'truck':4}
#label_name={'airplane':0,'bird':1}

#Create two dataframes one for train and one for test with 3 columns as filename,label and classname:

#train_df=pd.DataFrame(columns=['Filename'])

train_df=pd.DataFrame(columns=['Filename','Label','ClassName'])
test_df=pd.DataFrame(columns=['Filename','Label','ClassName'])

#number of images to take for test data from each category

num_images_for_test=60

#Prepare a labeled data

train_labels_path='/content/drive/MyDrive/BYOL-ViT-Hourglass/STL10/annotations/stl.csv'
test_labels_path='/content/drive/MyDrive/BYOL-ViT-Hourglass/STL10/annotations/data_recognition_test.csv'
print(train_labels_path)
train_df=pd.read_csv(train_labels_path,usecols=['Filename'])
test_df=pd.read_csv(test_labels_path,usecols=['Filename','Label','ClassName'])

per_cls_labeled_data=25
labeled_data=pd.DataFrame(columns=['Filename'])


for labels in range(10):
  data=train_df['Filename']
  num_labeled_samp=int((len(data)/100)*per_cls_labeled_data)
  print(num_labeled_samp)
  idxs=random.sample(range(1,len(data)),num_labeled_samp)
  data_selected=data.iloc[idxs]
  labeled_data=pd.concat([labeled_data,data_selected])
  print(labeled_data)
    
labeled_data.to_csv('/content/drive/MyDrive/BYOL-ViT-Hourglass/STL10/annotations/unlabeled.csv')

