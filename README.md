# Final Year Project: Diabetic Retinopathy Monitoring System ( DRMS )

This README file contains project description, structure breakdown of the project as well as a description of 
what each folders and important file contains thats crutial to the project. 

## Project Description

Diabetic Retinopathy Monitoring System ( DRMS ) is a mobile application for  IOS / Android which focuses on providing 
a monitoring system for diabetic patients detecting whether they are vulnerable for Diabetic Retinopathy.
The app uses a trained machine learning model that takes in a retinal image and returns a results which 
contains a score between 0 - 4 determining the likelyhood of the user containing Diabetical Retinopathy 

The app takes any retinal image from a mobile devices gallery and returns a prediction however the whole idea
of the application is to use the hardware add on for mobile called D-eye sensor. the D-eye Sensor gives the 
ability for an easier method of acquiring a retinal image from home. However as said the app takes in any 
retinal image .i.e D-eye sensor iamge or Fundus Camera retinal Images.
Images taken from a fundus camera will provide an result of higher accuracy.

The D-eye sensor is a sensor addon mainly for iPhones so this project developement focuses for app deployment on
Apple / IOS, however deploy methods for Android will also be provided 




# Project Structure 
The project is divided into two main folder Frontend and Backend each containing various files
that provide crucial functionalities to the project

## Frontend 

### Description 
The front end is developed in using Ionic with Vue JS. Eventhough Vue is a javascript framework the project was 
made using Typscipt since ionic is created in TypeScript 

### File breakdown 
Folders:
DRSM 
This folder contains the whole Ionic Vue JS project it has various folder inside of it which put the whole project together
however the main files are insode

DRSM/src/views - this is where the main HTML / JS / CSS code can be found for the front end of the application 
DRMS/src/composables - this is where the main typescript of the project is located which enables some functionalities like opening the camera 
DRMS/src/images - this is where all the iamges used in the projected are stored 
File Testing List.xlsx - this file contains details of manual testing that was used to evaluate the frontend 

### Deployment 
There are two steps in order to deploy the front end of the application depending of where you would like to view the app 
Step 1 is the instruction that are to be followed for the deployment of the frontend locally on your  PC.
Step 2 focuses on deploying the application for your mobile SDK either Android Studio / xCode which then can be followed to deploy
the application for your phone. 

Step 1 :
- Download Node JS
- install ionic: npm install -g @ionic/cli
- Clone this repository and navigate to the frontend folder ( DRSM ) using terminal
- install all packages: npm install 
- Now run the frotend on web: ionic serve

Step 2 : 
- Again navigate to the DRMS folder using terminal 
- Build project for deployment: ionic build
- To deploy on android isntall android studio ( if IOS skip this)
- to deploy on IOS install xCode ( If Android skip this )
- For android run : ionic cap add android
- For IOS run : ionic cap 
- Run: ionic cap copy 
- Run: ionic cap sync
- Now for Adnroid run : ionic cap open android
- For IOS run : ionic cap open ios

## Backend 

### Description 
The backend is developed in Python. Various python technologies have been used to create the project backend.
Machine learning model was created using the Resnet50 model from keras tensorflow. the connection between
the frontend and the backend was created using python flask api, hosting the API was used using 
ngrok which allows to host the localhost API publicly so its easily accessible by the frontend. Finally 
the processing of the image and their adjustment was created with the use of libraries such as 
opencv numpy and pandas. 

### File breakdown 
This folder contains all the files that create the backend of the project 
files:

api.py - this file contains the contents of the flask API 

processing.py - this files contains processing that is needed to be done the the image the user
submits before running its through the machine learning model, it also create the predictData.csv,
userImage folder and processedUserImage folder which contain the user image and user image after processing 

best_model.h5 - these are the weights of the trained machine learning model. This is the model that had the best accuracy
while running through the epoches

model.json - this is the json model structure of the machine learning model 

TrainingMlModel.ipynb - this is the jupyter notebook file that contains the code that trains and create the machine larning model 
create the file best_model.h5 and model.json which contain the trained models weight and models structure 

ngrok.exe - this is The ngrok file which when executed starts up ngrok which will allow you to host your local api publicly 
further instructions provided in deployment section 

### Deployment 
The deployment of the files just requires cloning the repositor but to set up the backend properly following steps are to be taken
Steps:

- Clone the repository 
- Open api.py file 
- Run the file and copy the address that the output says the api is hosted at .i.e (  http://localhost:5000/ )
- launch ngrok.exe 
- while ngrok is launched in its terminal type in ngrok http  (*enter local address where APi is hosted*  .i.e http://localhost:5000/ )
- Now another window will open and under forwarding you can see addresses where now the API is hosted publicly under 
- Now The your API is hosted publicly under the address provided by ngrok 

Linking the Frontend with the API 

In the frontend do the following 
- got to DRMS/src/views
- Open Tab1.vue 
- Scroll down to submitFile() method 
- got to axios.post 
- change the address to the address provided by ngrok  

Now the Frontend should be linked with the backend ( Flask Api )

# Download Model weights and Model structure
## Under this link you can download the models weights and model json structure
## https://drive.google.com/drive/folders/1DxwyNjefVaVttWnbH-6fQ0wuUUNF4u1m?usp=sharing

# Code References 
## Here you will find reference to all of the code from which some of backend was inspired by 
## https://github.com/debayanmitra1993-data/Blindness-Detection-Diabetic-Retinopathy-/blob/master/3_resnet50(colab).ipynb