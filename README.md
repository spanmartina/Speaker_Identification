# Speaker_Identification

The task is to determine the identity of a person by his/her voice.  This is known as Automatic Speaker Recognition and falls in the category of biometric security systems, as it is related to human characteristics or individuality. 
The application is implemented in Python and is composed of two distinct phases, the training phase and testing phase. They can each be assigned to a task, namely the enroll and recognition task.

We use MFCC to extract the features from the speech signal, Mel-frequency cepstral coefficients (MFCCs) method is one of the most popular strategies for feature extraction in both audio and speech signal. We strive to make the correct identification of the speaker using the Gaussian mixture model (GMM). The features extracted are fed to GMM-based approaches that have the purpose to create speaker models for identification.
To evaluate the performance of the speaker identification system we use a Confusion Matrix. This is a useful machine learning method that allows us to measure recall, precision and accuracy.
