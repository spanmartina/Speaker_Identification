import os
import pickle
import numpy as np
import shutil
import scipy.io.wavfile as wav
from feature_extraction import extract_features
from refactOne import featureExtraction #refact model after succesful log in
from refactAll import featureExtraction_allUsers #refact all models
import parameters as p

def availableUsername(username):
	sourceFolder = sorted([os.path.join(name)
		for name in os.listdir(p.source_train)])
	for user in sourceFolder:
		if user == username:
			#username Not available  
			return False
		
		else: 
			# username Available -> create folder
			path = os.path.join(p.source_train, username)
			try: 
				os.mkdir(path) 
				print("Directory '% s' created" % username)
			except OSError as error: 
				print(error)
			return True
	

def enroll(username, fpath):
	"""Enroll a user with an audio file
		inputs: str (Name of the person to be enrolled and registered)
				str (Path to the audio file or folder of the person to enroll)
		outputs: None"""

	path = os.path.join(p.source_train, username)
	if os.path.isfile(fpath):
		shutil.copy(fpath, path)
	elif os.path.isdir(fpath):
		for name in os.listdir(fpath): #Train/x where x-folder name (corrseponds with the name of the user)
			if name.endswith('.wav'): #Check if it is a wav file
				name = os.path.join(fpath, name)
				shutil.copy(name, path)

def test(path):	
	# read voice  
	sr,audio = wav.read(path)
	feature_vector   = extract_features(audio,sr)

	gmmModels = [os.path.join(p.modelpath,fname) for fname in os.listdir(p.modelpath) if fname.endswith('.gmm')] #Model files ending with .gmm in models

	#Load the Gaussian gender Models
	models = [pickle.load(open(fname, 'rb')) for fname in gmmModels] #Opening model files
	# models = [pickle.load(open(fname,'r')) for fname in gmmModels] #Opening model files
	person = [fname.split("/")[-1].split(".gmm")[0] for fname in gmmModels] #Split and get the name of the person.
	log = np.zeros(len(models))  #score of individual comparison

	for i in range(len(models)):
		gmm    = models[i]  #checked one by one with each model
		scores = np.array(gmm.score(feature_vector))
		print('Score for i = ', i, ' is:  ', scores)
		log[i] = scores.sum()
	winner = np.argmax(log) #We rotate indexes of maximum values along our axis
	print("= >> Detected as person: "+person[winner], " ")
	speaker_detected = person[winner]
	return speaker_detected

#main--------------------------------------------------
print("Write 0 - Enroll || 1 - Test || 2 - Refact All")
take=int(input())
if take == 0:
	username = input('Enter username:')

	while (availableUsername(username) != True):
		#username not available 
		username = input('Username not available. Enter another username:')
	
	fpath = input("Load audio file or folder(path to folder):")
	enroll(username, fpath)

elif take == 1:
	username = input('Enter username')
	path = input("Enter the File name from Test Audio Sample Collection :")
	if username==test(path):
		print("Succesfully logged in. Hello there, ", username, " !")
		#add file to folder
		enroll(username, path)
		#update model
		featureExtraction(username)
	else:
		print("Permision denied")
elif take == 2:
	featureExtraction_allUsers()

else:
	print('Program ended')
