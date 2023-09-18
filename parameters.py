# Paths to folders (train|test|models)
source_train   = r"train/"
source_test = r"test/" 
modelpath   = "models/" 


#   mfcc_feat = mfcc.mfcc(signal=audio,samplerate=rate, winlen=p.nfft/rate, winstep=p.fpt, numcep=p.n_mfcc, nfilt=p.n_mel, nfft=p.nfft, lowfreq=p.fmin, highfreq=p.fmax,
#                                           preemph=0.0, ceplifter=0, appendEnergy=False)    
    
# gmm = mixture.GaussianMixture(n_components = p.n_components, max_iter = p.max_iter,  covariance_type='diag',n_init = p.n_init) #We are calling gmm function.
#             gmm.fit(features)
# MFCC
#####################3
# sr = 16000        # Sampling frequency
# wst = 0.02       # Window size (seconds)
# fpt = 0.01      # Frame period (seconds) 
# nfft = round(wst*sr)      # Window size (samples)
# # nfft = 512 #default value
# fp = round(fpt*sr)        # Frame period (samples)
# nbands = 40    # Number of filters in the filterbank
# ncomp =  20    # Number of MFCC components
# #####################33
# fmin = 0
# fmax = None
# n_mfcc = 20 #   the number of cepstrum to return (default 13) #MFCC is a very compressible representation, often using just 20 or 13 coefficients instead of 32-64 bands in Mel spectrogram
# n_mel = 40  #the number of filters in the filterbank (26 default)

sr = 16000        # Sampling frequency
wst = 0.030       # Window size (seconds)
fpt = 0.015      # Overlaping Frame period (seconds) 
nfft = round(wst*sr)      # Window size (samples)
# nfft = 512 #default value
fp = round(fpt*sr)        # Frame period (samples)
nbands = 20    # Number of filters in the filterbank (40 default)
ncomp =  20    # Number of MFCC components
#####################33
fmin = 0
fmax = None
n_mfcc = 13 # MFCC is a very compressible representation, often using just 20 or 13 coefficients instead of 32-64 bands in Mel spectrogram
n_mel = 40


# sr = 16000        # Sampling frequency
# wst = 0.030       # Window size (seconds)
# fpt = 0.015      # Overlaping Frame period (seconds) 
# # nfft = round(wst*sr)      # Window size (samples)
# nfft = 512 #default value
# fp = round(fpt*sr)        # Frame period (samples)
# nbands = 40    # Number of filters in the filterbank
# ncomp =  20    # Number of MFCC components
# #####################33
# fmin = 0
# fmax = None
# n_mfcc = 13 # MFCC is a very compressible representation, often using just 20 or 13 coefficients instead of 32-64 bands in Mel spectrogram
# n_mel = 26

# MFCC
#####################3
# sr = 16000        # Sampling frequency
# wst = 0.030       # Window size (seconds)
# fpt = 0.015      # Overlaping Frame period (seconds) 
# # nfft = round(wst*sr)      # Window size (samples)
# nfft = 512 #default value
# fp = round(fpt*sr)        # Frame period (samples)
# nbands = 40    # Number of filters in the filterbank
# ncomp =  20    # Number of MFCC components
# #####################33
# fmin = 0
# fmax = None
# n_mfcc = 13 # MFCC is a very compressible representation, often using just 20 or 13 coefficients instead of 32-64 bands in Mel spectrogram
# n_mel = 26

# GMM
n_components = 10
max_iter = 100
covariance_type='diag'
n_init = 3


# n_components = 5
# max_iter = 200
# covariance_type='diag'
# n_init = 1
# GMM 2
# n_components = 10
# max_iter = 100
# covariance_type='spherical'
# n_init = 1

# mfcc_feat = mfcc.mfcc(signal=audio,samplerate=p.sr, winlen=p.nfft/p.sr, winstep=p.fpt, numcep=p.n_mfcc, nfilt=p.n_mel, nfft=p.nfft, lowfreq=p.fmin, highfreq=p.fmax,
#                                           preemph=0.0, ceplifter=0, appendEnergy=False)    
#     print("mfcc", mfcc_feat.shape)
#########################2222222222222
# winlen, ovrlen, pre_coef, nfilter, nftt = 0.025, 0.01, 0.97, 20, 512  #[window size (sec)], [frame shift(sec)], [pre-emp coeff],
#                                                                       #[no. of filter in MFCC], [N-point FFT]
# sr = 16000        # Sampling frequency
# wst = 0.025       # Window size (seconds)
# fpt = 0.01      # Frame period (seconds) 
# nfft = 512      # Window size (samples)
# # nfft = 512 #default value
# fp = round(fpt*sr)        # Frame period (samples)
# nbands = 20    # Number of filters in the filterbank
# ncomp =  20    # Number of MFCC components
# #####################33
# fmin = 0
# fmax = None
# n_mfcc = 20 # MFCC is a very compressible representation, often using just 20 or 13 coefficients instead of 32-64 bands in Mel spectrogram
# n_mel = 30

