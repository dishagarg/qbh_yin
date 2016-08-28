
# coding: utf-8

# In[2]:

# PATTERN MATCHING
get_ipython().magic(u'matplotlib inline')
from pylab import *
import matplotlib.mlab
import wave
import numpy as np
from scipy.io import wavfile
from scipy import signal
from scipy import interpolate
import numpy.matlib
import sqlite3 as lite
from PyQt4 import QtCore, QtGui
import winsound

DB = '..\\db\\MIR_QBH.db'
path='..\\db';
connection = lite.connect(DB)

def findSongs():
    
    def calcDbSongsDistances(dbSongs, str2):
        distances=[]
        for i in range(0,len(dbSongs)):
            distance=dynamicEditDistance(dbSongs[i],str2)
            print (distance)
            distances.append(distance)
        return distances;
        
    
    def dynamicEditDistance(str1, str2):
        temp= np.zeros((len(str1)+1, len(str2)+1)); #creating a temp of rows of length as of str1 and cols of str2
        for i in range(0, len(temp[0])):
            temp[0][i] = i
        for i in range(0, len(temp)):
            temp[i][0] = i
        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                if str1[i-1]==str2[j-1]:
                    temp[i][j] = temp[i-1][j-1]
                else:
                    temp[i][j] = 1 + min(temp[i-1][j-1], temp[i-1][j], temp[i][j-1])
        return temp[len(str1)][len(str2)];
        
    def fetchDBSongs():
        with connection:
            
            cursor = connection.cursor() 
            connection.row_factory = lambda cursor, row: row[0]
            c = connection.cursor()
            patterns = c.execute('SELECT pattern FROM audioFeature').fetchall()
            connection.commit()   
        return patterns;
        
    def fetchHummedSong():
    
        with connection:
            
            cursor = connection.cursor() 
            connection.row_factory = lambda cursor, row: row[0]
            c = connection.cursor()
            pattern = c.execute('SELECT pattern FROM hummedFeature').fetchone()
            fname = c.execute('SELECT queryTone FROM hummedFeature').fetchone()
            connection.commit()
        return pattern;
       
    def updateDistance():
        #Insert values in database
        DB = path+'\MIR_QBH.db'
    
        connection = lite.connect(DB)
        for i in range(len(dbSongs)):
            with connection:
                cursor = connection.cursor()
                sql = "UPDATE audioFeature SET distance=? WHERE pattern=?";
                connection.execute(sql,[result[i], dbSongs[i]]) 
                connection.commit()
        
    def fetchRankedSongs():
        with connection:
            cursor = connection.cursor() 
            connection.row_factory = lambda cursor, row: row[0]
            c = connection.cursor()
            names = c.execute('SELECT songName FROM audioFeature ORDER BY distance ASC LIMIT 5').fetchall()
            distances = c.execute('SELECT distance FROM audioFeature ORDER BY distance ASC LIMIT 5').fetchall()
            ids = c.execute('SELECT id FROM audioFeature ORDER BY distance ASC LIMIT 5').fetchall()
            songPath = c.execute('SELECT song FROM audioFeature ORDER BY distance ASC LIMIT 5').fetchall()
            imagePath = c.execute('SELECT ImageName FROM audioFeature ORDER BY distance ASC LIMIT 5').fetchall()
            connection.commit()   
        return names,distances,ids,songPath,imagePath;
    
    hummedSong = fetchHummedSong();
    dbSongs=fetchDBSongs(); # Collection of songs
    result=calcDbSongsDistances(dbSongs,hummedSong); #Creating list of min distances of all songs in DB from hummed Query
    updateDistance();
    songs=[];
    allList=[];
    RankedSongs, distances, ids,songPath,imagePath = fetchRankedSongs();
    for i in range(len(distances)):
        songs=ids[i], RankedSongs[i], distances[i],songPath[i],imagePath[i] ;
        #print (RankedSongs[i]);
        allList.append(songs);
    
    with connection:    
        for i in range (0,len(allList)):
            cursor = connection.cursor() 
            sql1 = "UPDATE matchedSongs SET songName=?,distance=?,queryTone=?,ImageName=? WHERE id=?";
            cursor.execute(sql1, [RankedSongs[i],distances[i],songPath[i],imagePath[i],i+1])
            connection.commit()
    #connection.close()

    
#findSongs();
#connection.close()


# In[ ]:



