#IMPORT SYSTEM FILES
import os
import pickle
import numpy as np
from scipy.io.wavfile import read
from sklearn import mixture
import parameters as p
from feature_extraction import extract_features as extract_features

node = True

def enroll(name, file):
    """Enroll a user with an audio file
        inputs: str (Name of the person to be enrolled and registered)
                str (Path to the audio file of the person to enroll)
        outputs: None"""
    

    # Path
    path = os.path.join(p.source_train, name) #create folder and save audio there
    #create directory
    try: 
        os.mkdir(path) 
        print("Directory '% s' created" % name)
    except OSError as error: 
        print(error)  

    #add file to directory
    # file = os.path.join(path, file+".wav")
    print('path', path, '-----file', file)
    import shutil
    shutil.copy(file+'.wav', path)

def featureExtraction(directoryName):
    features = np.asarray(()) #we created Array
    path = os.path.join(p.source_train, directoryName) 
    
    # sourceFolder = [os.path.join(name)
    #     for name in os.listdir(source)] 
    #     # for name in os.listdir(path)] 

    # print("Source Folders: ",sourceFolder)
    sources = [] #create a new list. We will take the .wav files in the folders in the training data/Username folder into this list.

    for name in os.listdir(p.source_train + directoryName): #TrainingData/x where x is the folder in it. This function will work for each folder.
        if name.endswith('.wav'): #If it is a wav file in TrainingData/x;
            nn = "{}".format(directoryName)+"/"+"{}".format(name) #Path
            sources.append(nn) #Adding it to our list.

    print('Sources', sources)


    for path in sources:    
        path = path.strip()   
        print("Path", path)
        # Read the voice
        sr,audio = read(p.source_train + path)
        print('sr extracted', sr)
        # sr = 16000
        print("Source+path", p.source_train + path)
        # Let's explain the 40-dimensional MFCC and delta MFCC properties
        vector   = extract_features(audio,sr)
        if features.size == 0: #If we doesn't have any data
            features = vector 
            print("No featureS")#Features will equal to vector and program ends.
        else: 
            features = np.vstack((features, vector)) #We stack arrays vertically (on a row basis) sequentially.
            print("features.size", features.size)
        if node == True:    
            gmm = mixture.GaussianMixture(n_components = p.n_components, max_iter = p.max_iter,  covariance_type='diag',n_init = p.n_init) #We are calling gmm function.
            gmm.fit(features)
            # We save the models we calculated to the folder
            picklefile = path.split("/")[0]+".gmm"
            print('picklefile', picklefile)
            pickle.dump(gmm,open(p.modelpath + picklefile,'wb'))
            print("  >> Modeling complete for file: ",picklefile,' ',"| Data Point = ",features.shape   )
            features = np.asarray(()) 

# name = input("Name of user")
# featureExtraction(name)