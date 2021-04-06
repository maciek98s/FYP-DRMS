#------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Author : Maciej Skrzypczynski 
Date: 06/04/2021
Description: Thile file consists of methods which are used to process user images and attemp image processing techniques on user images
after thats completed the image is goes through a method to predict the user image for diabetic Retinopathy and then the result is returned
Code References : Code uses for of the code which was inspired by the following code : 
https://github.com/debayanmitra1993-data/Blindness-Detection-Diabetic-Retinopathy-/blob/master/3_resnet50(colab).ipynb
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------
import csv
import tensorflow as tf
import numpy as np
import os
import cv2 as cv2
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
from keras.layers import *
from keras.models import model_from_json
from keras.backend import stack
from keras.optimizers import SGD
import tensorflow as tf; 
#-------------------------------------------------------------------------------------------------------------------------------------------------------


#function to remove black background from image
def crop_image_from_gray(img,tol=7):
    if img.ndim ==2:
        mask = img>tol
        return img[np.ix_(mask.any(1),mask.any(0))]
    elif img.ndim==3:
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        mask = gray_img>tol
        
        check_shape = img[:,:,0][np.ix_(mask.any(1),mask.any(0))].shape[0]
        if (check_shape == 0): # image is too dark so that we crop out everything,
            return img # return original image
        else:
            img1=img[:,:,0][np.ix_(mask.any(1),mask.any(0))]
            img2=img[:,:,1][np.ix_(mask.any(1),mask.any(0))]
            img3=img[:,:,2][np.ix_(mask.any(1),mask.any(0))]
    #         print(img1.shape,img2.shape,img3.shape)
            img = np.stack([img1,img2,img3],axis=-1)
    #         print(img.shape)
        return img

#function to ricle crop the image 
def circle_crop(img, sigmaX = 30):   
    """
    Create circular crop around image centre    
    """    
    img = crop_image_from_gray(img)    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    height, width, depth = img.shape    
    
    x = int(width/2)
    y = int(height/2)
    r = np.amin((x,y))
    
    circle_img = np.zeros((height, width), np.uint8)
    cv2.circle(circle_img, (x,y), int(r), 1, thickness=-1)
    img = cv2.bitwise_and(img, img, mask=circle_img)
    img = crop_image_from_gray(img)
    img=cv2.addWeighted(img,4, cv2.GaussianBlur( img , (0,0) , sigmaX) ,-4 ,128)
    return img 

#Function takes in image and processes the image reducing it size and enchancing it that saving it again 
def preprocess_image(values):
    for i in values: 
      input_filepath = os.path.join('./','userImage','{}'.format(i))
      output_filepath = os.path.join('./','processedUserImage','{}'.format(i))
      
      img = cv2.imread(input_filepath)
      height, width, channels = img.shape
      img = circle_crop(img) 
      cv2.imwrite(output_filepath, cv2.resize(img, (512,512)))

#write a CSV from user image containing file name in order to load it into a data frame 
def createCSV():
    with open('predictData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id_code"])
        writer.writerow(["test"])
#function load data into a dataframe
def load_data():
    test = pd.read_csv('predictData.csv')
    
    test_dir = os.path.join('./','processedUserImage/')
    
    test['file_path'] = test['id_code'].map(lambda x: os.path.join(test_dir,'{}.jpg'.format(x)))
    
    test['file_name'] = test["id_code"].apply(lambda x: x + ".jpg")
    
    
    return test

#Function loads in the model and the weights. Following it runs prediction on the model and returns the results
def predictResult():
    createCSV()
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    #print(loaded_model_json)
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("best_model.h5")

    df_test = load_data()

    preprocess_image(df_test.file_name.values)

    test_datagen = ImageDataGenerator(rescale=1./255)
    test_generator = test_datagen.flow_from_dataframe(dataframe=df_test,
                                                    directory = "./processedUserImage/",
                                                    x_col="file_name",
                                                    target_size=(320, 320),
                                                    batch_size=1,
                                                    shuffle=False,
                                                    class_mode=None)



    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    predictions = loaded_model.predict(test_generator)

    predresults = [np.argmax(pred) for pred in predictions]

    for i in predresults:
        return(i)


#-------------------------------------------------------------------------------------------------------------------------------------------------------


