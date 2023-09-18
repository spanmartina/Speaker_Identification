import os
import pickle
import numpy as np
import pandas as pd
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
# from sklearn.metrics import precision_score, recall_score
import parameters as p
from feature_extraction import extract_features as extract_features


def pred(path):
		
	# path = path + '.wav'
	print("Path",path)
	# print("Source+path",p.source_test + path)
	# read voice  
	sr,audio = wav.read(path)
	# sr,audio = wav.read("test\Collin_test.wav")
	feature_vector   = extract_features(audio,sr)

	gmmModels = [os.path.join(p.modelpath,fname) for fname in os.listdir(p.modelpath) if fname.endswith('.gmm')] #Model files ending with .gmm in models

	#Load the Gaussian gender Models
	models = [pickle.load(open(fname, 'rb')) for fname in gmmModels] #Opening model files
	# models = [pickle.load(open(fname,'r')) for fname in gmmModels] #Opening model files
	person = [fname.split("/")[-1].split(".gmm")[0] for fname in gmmModels] #Split and get the name of the person.
	log = np.zeros(len(models))  #score of individual comparison

	for i in range(len(models)):
		gmm    = models[i]  #checked one by one with each model.
		scores = np.array(gmm.score(feature_vector))
		log[i] = scores.sum()
		# print('Score for i:',i, 'is', log)
	winner = np.argmax(log)#index of the maximum value in the array
	print("= >> Detected as person: "+person[winner], " ")
	speaker_detected = person[winner]
	return speaker_detected


class GetFiles:

    def __init__(self,dataset_path):
        # dataset: dataset is the root path for dataset(test,train,predict)
        self.dataset_path = dataset_path

    def getTestFiles(self):

        data_frame_row = []

        data_frame = pd.DataFrame()

        # flag = "test"

        # root test dierctory files listing
        speaker_audio_folder = os.listdir(self.dataset_path)
        print('Root test files', speaker_audio_folder)

        for folders in speaker_audio_folder:

            audio_files = os.listdir(self.dataset_path+"/"+folders)
            # listing of sub directory

            for files in audio_files:
                path_to_audio =  self.dataset_path+"/"+folders+"/"+files
                print('path_to_audio', path_to_audio)
                data_frame_row.append([path_to_audio,folders])

            data_frame = pd.DataFrame(data_frame_row,columns=['audio_path','actual'])

        return data_frame

def getTestFiles(self):

    data_frame_row = []

    data_frame = pd.DataFrame()

    # flag = "test"

    # root test dierctory files listing
    speaker_audio_folder = os.listdir(self.dataset_path)


    for folders in speaker_audio_folder:

        audio_files = os.listdir(self.dataset_path+"/"+folders)
        # listing of sub directory

        for files in audio_files:
            path_to_audio =  self.dataset_path+"/"+folders+"/"+files
            data_frame_row.append([path_to_audio,folders])

        data_frame = pd.DataFrame(data_frame_row,columns=['audio_path','actual'])

    return data_frame

def getActualPredictedList():
    '''
    @return pd-frame : list of the actual and predicted list for confusion matrix calculation
    '''
    print("You are in getActualPredictedList")

    data_frame_row = []

    gf = GetFiles(dataset_path="test")
    print("You are in getActualPredictedList ------get test files")
    
    # testing_files =  getTestFiles()
    testing_files =  gf.getTestFiles()
    print("You are in getActualPredictedList ------get test files", testing_files)
    # print(testing_files)

    for index, row in testing_files.iterrows():
        audio_path = row["audio_path"]
        print("Audio path fo prediction is:_______________", audio_path)
        predicted = pred(audio_path)

        actual = row["actual"]
        data_frame_row.append([actual, predicted])
    # print('actual_predicted BEFORE sorting', actual_predicted)
    # alphabetic sorting by column 'actual' without affecting the predicted column
    actual_predicted = pd.DataFrame(data_frame_row,columns = ['actual','predicted']).sort_values(by='actual')
    # print('actual_predicted AFTER sorting', actual_predicted)

    return actual_predicted


def showAccuracyPlotAndMeasure():
    actual_pred = getActualPredictedList()
    print("You are in showAccuracyPlotAndMeasure")

    actual = actual_pred["actual"].tolist()
    predicted = actual_pred["predicted"].tolist()
    labels  = sorted(actual_pred["actual"].unique().tolist()) # alphabetic sorting
    print("############actual", actual)
    print("############predicted", predicted)
    print("############labels", labels)
    
    cm = confusion_matrix(actual, predicted, labels=labels) #confusion matrix in matrix form
    
    #convert the table into a confusion matrix display.
    print("###################CM", cm)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(cm)
    plt.title('Confusion matrix of Recognition Model')
    fig.colorbar(cax)
    ax.set_xticklabels([''] + labels)
    ax.set_yticklabels([''] + labels)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
    display_numeric_accuracy(actual, predicted,labels) # displays the precision recall and fscore

def display_numeric_accuracy(actual,predicted,labels):
    '''
    @param list actual : actual label for the speaker's audio
    @param list predicted : predicted label by the GMM classifier
    @param list labels : name of the distinct speaker
    '''
    print("\n")
    print("You are in display_numeric_accuracy-----------------------------")
    print("classification_report################################",classification_report(actual, predicted, target_names=labels))
    	
    # print('Precision: %.3f' % precision_score(actual, predicted))
    # print('Recall: %.3f' % recall_score(actual, predicted))

showAccuracyPlotAndMeasure()