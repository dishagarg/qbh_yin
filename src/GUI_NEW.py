
# coding: utf-8

# In[ ]:



# Form implementation generated from reading ui file 'latest_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3 as lite
#reload(WholeCodeHummedFeatures)
import WholeCodeHummedFeatures
import MatchSongs
import os
import winsound
from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout,    QLineEdit, QRadioButton

DB = '..\\db\\MIR_QBH.db'
path='..\\db';
connection = lite.connect(DB)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(757, 486)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 240, 441, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
       
    
        self.Featureext = QtGui.QPushButton(self.centralwidget)
        self.Featureext.setGeometry(QtCore.QRect(30, 120, 111, 21))
        self.Featureext.setObjectName(_fromUtf8("Featureext"))
        self.Featureext.clicked.connect(WholeCodeHummedFeatures.AubioYin)
        
#        self.progress = QtGui.QProgressBar(self)
#        self.progress.setGeometry(200, 80, 250, 20)
        
        self.clearsong = QtGui.QPushButton(self.centralwidget)
        self.clearsong.setGeometry(QtCore.QRect(690, 260, 41, 20))
        self.clearsong.setObjectName(_fromUtf8("clearsong"))
        self.clearsong.clicked.connect(self.setLabelText_empty_6)
        
        
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 70, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rockwell"))
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 450, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rockwell"))
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 240, 231, 21))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 270, 171, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rockwell"))
        font.setPointSize(10)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(290, 290, 441, 161))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 270, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rockwell"))
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
###        
        self.clearquery = QtGui.QPushButton(self.centralwidget)
        self.clearquery.setGeometry(QtCore.QRect(690, 61, 41, 20))
        self.clearquery.setObjectName(_fromUtf8("clearquery"))
        self.clearquery.clicked.connect(self.setLabelText_empty)
### 
        
        ##Play Selected song using CommandLinkButton
        self.playsong = QtGui.QCommandLinkButton(self.centralwidget)
        self.playsong.setGeometry(QtCore.QRect(30, 410, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        self.playsong.setFont(font)
        self.playsong.setObjectName(_fromUtf8("playsong"))
        self.playsong.clicked.connect(self.playAudio)
        
        
        self.Playquery = QtGui.QPushButton(self.centralwidget)
        self.Playquery.setGeometry(QtCore.QRect(150, 90, 101, 21))
        self.Playquery.setObjectName(_fromUtf8("Playquery"))
        self.Playquery.clicked.connect(WholeCodeHummedFeatures.playAudio)
      
    
###    
        self.plotquery = QtGui.QPushButton(self.centralwidget)
        self.plotquery.setGeometry(QtCore.QRect(150, 120, 101, 21))
        self.plotquery.setObjectName(_fromUtf8("plotquery"))
        self.plotquery.clicked.connect(self.setLabelText_fill)
###        
        
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 300, 151, 101))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.radioButton_1 = QtGui.QRadioButton(self.frame)
        self.radioButton_1.setGeometry(QtCore.QRect(0, 0, 82, 21))
        self.radioButton_1.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(0, 20, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 40, 82, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(0, 60, 82, 17))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.frame)
        self.radioButton_5.setGeometry(QtCore.QRect(0, 80, 82, 17))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        
        ##call function on radio button click
        self.radioButton_1.toggled.connect(self.radio1_clicked)
        self.radioButton_2.toggled.connect(self.radio2_clicked)
        self.radioButton_3.toggled.connect(self.radio3_clicked)
        self.radioButton_4.toggled.connect(self.radio4_clicked)
        self.radioButton_5.toggled.connect(self.radio5_clicked)
        ##
        
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(130, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.commandLinkButton_2.clicked.connect(self.showContour)
        
        self.Record = QtGui.QPushButton(self.centralwidget)
        self.Record.setGeometry(QtCore.QRect(30, 90, 111, 21))
        self.Record.setObjectName(_fromUtf8("Record"))
        #
        self.Record.clicked.connect(WholeCodeHummedFeatures.recordAudio)
        
        
        self.findsongs = QtGui.QPushButton(self.centralwidget)
        self.findsongs.setGeometry(QtCore.QRect(90, 170, 121, 21))
        self.findsongs.setObjectName(_fromUtf8("findsongs"))
        
        #calling on Click functiom for findSongs       
        self.findsongs.clicked.connect(self.findRankedSongs)
        self.findsongs.clicked.connect(self.isFindClicked)
        #####
    
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(270, 80, 20, 371))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rockwell"))
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listView_2 = QtGui.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(290, 90, 441, 141))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 300, 421, 141))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Music_Retrieval/Project/audios/empty.jpg")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        
        
        
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(296, 92, 431, 131))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Music_Retrieval/Project/audios/empty.jpg")))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 10, 91, 51))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Music_Retrieval/Project/audios/19445-200.png")))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(490, 0, 121, 71))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Music_Retrieval/Project/audios/32Z_music.png")))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def setLabelText_fill(self): 
        a = 'E:\\Music_Retrieval\\Project\\audios\\YINhummed.png'
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8(a)))
    
    def showContour(self):
        a = self.imageContour;
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(a)))
    
    def setLabelText_empty(self):    
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Music_Retrieval/Project/audios/empty.jpg")))
        
    def setLabelText_empty_6(self):    
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Music_Retrieval/Project/audios/empty.jpg")))
        
    def isFindClicked(self):
        print ("find songs clicked")
        self.radioButton_1.setHidden(False)
        self.radioButton_2.setHidden(False)
        self.radioButton_3.setHidden(False)
        self.radioButton_4.setHidden(False)
        self.radioButton_5.setHidden(False)
       
   
    def radio1_clicked(self, enabled):
                #self.songToPlay=self.rankedSongs[0][3];
        if enabled:
            print ('1 selected')
            self.songToPlay=self.rankedSongs[0];
            self.imageContour=self.rankedContours[0];
            print (self.imageContour)
           
    def radio2_clicked(self, enabled):
        if enabled:
            print ('2 selected')
            self.songToPlay=self.rankedSongs[1];
            self.imageContour=self.rankedContours[1];
            print (self.imageContour)
   
    def radio3_clicked(self, enabled):
        if enabled:
            print ('3 selected')
            self.songToPlay=self.rankedSongs[2];
            self.imageContour=self.rankedContours[2];
            print (self.imageContour)
           
    def radio4_clicked(self, enabled):
        if enabled:
            print ('4 selected')
            self.songToPlay=self.rankedSongs[3];
            self.imageContour=self.rankedContours[3];
            print (self.imageContour)
   
    def radio5_clicked(self, enabled):
        if enabled:
            print ('5 selected')
            self.songToPlay=self.rankedSongs[4];
            self.imageContour=self.rankedContours[4];
            print (self.imageContour)
               
    def playAudio(self):
        winsound.PlaySound(self.songToPlay, winsound.SND_FILENAME)
       
    def findRankedSongs(self,checked):
        MatchSongs.findSongs()     #Remember to uncomment later
        self.rankedSongs=[];
        with connection:
            cursor = connection.cursor() 
            connection.row_factory = lambda cursor, row: row[0]
            c = connection.cursor()
            names = c.execute('SELECT songName FROM matchedSongs ORDER BY distance ASC LIMIT 5').fetchall()
            songPath = c.execute('SELECT queryTone FROM matchedSongs ORDER BY distance ASC LIMIT 5').fetchall()
            imagePath = c.execute('SELECT ImageName FROM matchedSongs ORDER BY distance ASC LIMIT 5').fetchall()
            self.rankedSongs=songPath;
            self.rankedContours=imagePath;
            connection.commit()  
        self.songnames=names
        print ("num",self.rankedSongs);
        self.radioButton_1.setText(self.songnames[0])
        self.radioButton_2.setText(self.songnames[1])
        self.radioButton_3.setText(self.songnames[2])
        self.radioButton_4.setText(self.songnames[3])
        self.radioButton_5.setText(self.songnames[4])

    
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Featureext.setText(_translate("MainWindow", "SWIPE' Pitch Extract", None))
        self.clearsong.setText(_translate("MainWindow", "Clear", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-style:italic; color:#5500ff;\">* Pitch Contour of Recorded Query</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-style:italic; color:#000000;\">* Record Query of Max 10 Seconds</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#aa0000;\">List of Recommended Songs</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-style:italic; color:#5500ff;\">* Pitch Contour of Matched Song</span></p></body></html>", None))
        self.clearquery.setText(_translate("MainWindow", "Clear", None))
        self.playsong.setText(_translate("MainWindow", "Play Song", None))
        self.Playquery.setText(_translate("MainWindow", "Play Query", None))
        self.plotquery.setText(_translate("MainWindow", "Plot Pitch Contour", None))
        
        #Hiding radio buttons initially
        self.radioButton_1.setHidden(True)
        self.radioButton_2.setHidden(True)
        self.radioButton_3.setHidden(True)
        self.radioButton_4.setHidden(True)
        self.radioButton_5.setHidden(True)
        ###
        
        self.radioButton_1.setText(_translate("MainWindow", "Song1", None))
        self.radioButton_2.setText(_translate("MainWindow", "Song2 ", None))
        self.radioButton_3.setText(_translate("MainWindow", "Song3", None))
        self.radioButton_4.setText(_translate("MainWindow", "Song4", None))
        self.radioButton_5.setText(_translate("MainWindow", "Song5", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Plot Result Pitch", None))
        self.Record.setText(_translate("MainWindow", "Record Query", None))
        self.findsongs.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/ab/IMG_0776.JPG\"/><img src=\":/ab/IMG_0776.JPG\"/></p></body></html>", None))
        self.findsongs.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\":/ab/IMG_0776.JPG\"/><img src=\":/ab/IMG_0776.JPG\"/></p></body></html>", None))
        self.findsongs.setText(_translate("MainWindow", "Find Matched Songs", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#7a005b;\">Query By Humming</span></p></body></html>", None))
        self.listView_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"right\"><img src=\":/ab/IMG_0776.JPG\"/></p></body></html>", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# In[ ]:



