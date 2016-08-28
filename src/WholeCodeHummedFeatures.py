
# coding: utf-8

# In[2]:

# RECORD WORKING
get_ipython().magic(u'matplotlib inline')
import pyaudio, wave, sys
import sqlite3 as lite
import math
import sqlite3 as lite
import os.path
from os import listdir, getcwd
from IPython.display import display, Image
import json
from pylab import *
import matplotlib.mlab
from matplotlib import pyplot
import wave
import numpy as np
from numpy import matlib
#from scipy.io import wavfile
import sys
import csv     # imports the csv module
import operator
import pylab

import marsyas
import marsyas_util

DB = '..\\db\\MIR_QBH.db'
path='..\\db';
connection = lite.connect(DB)

WAVE_OUTPUT_FILENAME = '..\\db\\Audio.wav'
csvFile = '..\\db\\YinResultNext.csv'
pngFile = '..\\db\\YINhummed.png'

base=os.path.basename(WAVE_OUTPUT_FILENAME)
afile, ext = os.path.splitext(base)    
filePath=WAVE_OUTPUT_FILENAME;

print ("File name",afile+ext) 

def recordAudio():
    
    CHUNK = 8192
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 10

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                   channels = CHANNELS,
                   rate = RATE,
                   input = True,
                   input_device_index = 0,
                   frames_per_buffer = CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()    # "Stop Audio Recording
    stream.close()          # "Close Audio Recording
    p.terminate()           # "Audio System Close

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    connection.close()

def AubioYin():
    filename_input = 'E:\\Music_Retrieval\\Project\\audios\\Audio.wav'
    #filename_input = 'E:\\Music_Retrieval\\Assignment2\\qbh_examples.wav'
    csvFile = 'E:\\Music_Retrieval\\Project\\audios\\YinResultNext.csv'
    #csvFile = 'E:\\Music_Retrieval\\Project\\audios\\qbh_examples.csv'
    series = ["Series/input", ["SoundFileSource/src",
                               "Windowing/win",
                               "AubioYin/pitcher",
                               "CsvSink/csv"
                 ]
                ]
    net = marsyas_util.create(series)
    net.updControl("SoundFileSource/src/mrs_string/filename",filename_input)
    window_size = 1024;
    net.updControl("Windowing/win/mrs_natural/size", window_size);
    net.updControl("CsvSink/csv/mrs_string/filename", csvFile);
    ctrl_fname = net.getControl("SoundFileSource/src/mrs_string/filename");
    notempty = net.getControl("SoundFileSource/src/mrs_bool/hasData")
    
    while notempty.to_bool():
        #print notempty.to_bool()
        net.tick()
    print ctrl_fname.to_string()
    AubioYIN2()
    return net

def AubioYIN2():
    print ("AubioYIN running",filePath);
    #print("AubioYIN running", 'E:\\Music_Retrieval\\Assignment2\\qbh_examples.wav');
    temp=[]
    data=[]
    with open(csvFile, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            temp.append(row)
        
    print ("Features extracted"), type(temp);
    data = reduce(operator.add, temp)
    
    fig = figure();
    plot(data);
    ylabel("Frequency (Hz)");
    fig.savefig(pngFile);
    show(); #show in a window of contour on UI
    
    findFeatures(data);
    

def findFeatures(p):
    print ("findFeatures running");
    print("Read frequencies of audio and find MIDI notes and pattern");
    freq_est=p;
    count = 1
    temp = 1
    output_freq   = [] # Final list of Frequency and Duration
    output_num    = []
    
    output = [[0 for x in range(2)] for x in range(len(freq_est))] 
    for i in range(0, len(freq_est)):
        output_freq.append(freq_est[i])

    output_MIDI = [] # Converting the frequencies obtained after F0 estimation into corresponding MIDI Notes
    for j in range(0, len(output_freq)):
        d=69+(12*math.log(float(output_freq[j])/440))/(math.log(2))
        d = round(d,0)
        output_MIDI.append(d) #Rounding off the MIDI Notes
    finalLength = len(output_freq)
    
    plot(output_MIDI);

    s="" #Initialize an empty String
    for i in range(0,finalLength-1):
        if(output_MIDI[i] < output_MIDI[i+1]):
            if((output_MIDI[i+1]-output_MIDI[i])<=2):
                s += "u"
            else:
                s += "U"
        if(output_MIDI[i] == output_MIDI[i+1]):
            s += "S"
        if(output_MIDI[i] > output_MIDI[i+1]):
            if((output_MIDI[i]-output_MIDI[i+1])<=2):
                s += "d"
            else:
                s += "D"
    
    #Pattern Matching String Ends here 
    #print ("Pattern:",s);

    insertInDB(p,output_MIDI,s,filePath);

    
#*********************************************Insert in DB******************************************
def insertInDB(p,output_MIDI,s,filePath):
    print ("insertInDB ");
    #Insert values in database

    DB = path+'\MIR_QBH.db'

    connection = lite.connect(DB)

    freqArray = json.dumps(p)
    notesArray = json.dumps(output_MIDI)

    with connection:
        
        cursor = connection.cursor() 
        sql1 = "UPDATE hummedFeature SET frequency=?,midiNotes=?,pattern=?, queryTone=?,ImageName=? WHERE id=?";
        cursor.execute(sql1, [freqArray,notesArray,s,filePath,pngFile,1])
        connection.commit()
        with open(pngFile, 'rb') as input_file:
            ablob = input_file.read()
            sql = "UPDATE hummedFeature SET pitchContourImage=? WHERE id=?";
            connection.execute(sql,[lite.Binary(ablob), 1]) 
            connection.commit()
    connection.close()


#***************************************CALL function*******************************************
#recordAudio();
#AubioYin()


# In[3]:

#PLAY WORKING
import time
from sys import byteorder
import pyaudio
import wave
import winsound

def playAudio():
    
    fname = "E:\\Music_Retrieval\\Project\\audios\\Audio.wav"
    winsound.PlaySound(fname, winsound.SND_FILENAME)

    
#playAudio();



# In[ ]:



