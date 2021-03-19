import csv
import tensorflow as tf
import numpy as np
import os
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
from keras.layers import *
from keras.models import model_from_json
from keras.backend import stack
from keras.optimizers import SGD
import tensorflow as tf; 

print(tf.__version__)


def createCSV():
    with open('predictData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id_code"])
        writer.writerow(["test"])

def load_data():
    test = pd.read_csv('predictData.csv')
    
    test_dir = os.path.join('./','userImage/')
    
    test['file_path'] = test['id_code'].map(lambda x: os.path.join(test_dir,'{}.jpg'.format(x)))
    
    test['file_name'] = test["id_code"].apply(lambda x: x + ".jpg")
    
    
    return test

createCSV()


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
#print(loaded_model_json)
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("best_model.h5")
print("Loaded model from disk")

df_test = load_data()
print(df_test.head(6))

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_dataframe(dataframe=df_test,
                                                  directory = "./userImage/",
                                                  x_col="file_name",
                                                  target_size=(320, 320),
                                                  batch_size=1,
                                                  shuffle=False,
                                                  class_mode=None)



loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
predictions2 = loaded_model.predict(test_generator)

predresults2 = [np.argmax(pred) for pred in predictions2]

for i in predresults2:
    print (i)


print("hel")