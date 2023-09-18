import numpy as np
import python_speech_features as mfcc
from sklearn import preprocessing
import parameters as p
from python_speech_features import delta as deltaDefault

def calculate_delta(mfcc_feat):
    """Calculate and returns the delta of given feature vector matrix"""

    rows,cols = mfcc_feat.shape
    deltas = np.zeros((rows,p.n_mfcc))
    N = 2
    for i in range(rows):
        index = []
        j = 1
        while j <= N:
            if i-j < 0:                
                first = 0             
            else:                 
                first = i-j             
            if i+j > rows-1:
                second = rows-1
            else:
                second = i+j 
            index.append((second,first))
            j+=1
        deltas[i] = ( mfcc_feat[index[0][0]]-mfcc_feat[index[0][1]] + (2 * (mfcc_feat[index[1][0]]-mfcc_feat[index[1][1]])) ) / 10
    
    # second method
    # delta        = deltaDefault(mfcc_feat, 2)
    
    # double_deltas = deltaDefault(delta, 2)
    # deltas      = np.hstack((delta, double_deltas))
    # print('delta', deltas)
    # print('double_deltas', double_deltas)

    # print('combined2', combined2)
    
    
    return deltas

def extract_features(audio,rate): 
    mfcc_feat = mfcc.mfcc(signal=audio,samplerate=p.sr, winlen=p.nfft/p.sr, winstep=p.fpt, numcep=p.n_mfcc, nfilt=p.n_mel, nfft=p.nfft, lowfreq=p.fmin, highfreq=p.fmax,
                                          preemph=0.0, ceplifter=0, appendEnergy=False)    
    
    #sr 
    # mfcc_feat = mfcc.mfcc(signal=audio,samplerate=rate, winlen=p.nfft/rate, winstep=p.fpt, numcep=p.n_mfcc, nfilt=p.n_mel, nfft=p.nfft, lowfreq=p.fmin, highfreq=p.fmax,
    #                                       preemph=0.0, ceplifter=0, appendEnergy=False)    
    
    # print("mfcc", mfcc_feat.shape)
    mfcc_feat = preprocessing.scale(mfcc_feat)
    deltas = calculate_delta(mfcc_feat)
    combined = np.hstack((mfcc_feat,deltas)) 

    return combined