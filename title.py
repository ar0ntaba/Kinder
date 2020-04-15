from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QMessageBox
import sys
import time
import os

#TITLE UI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 481)
        MainWindow.setTabletTracking(True)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(230, 350, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.start.setFont(font)
        self.start.setText("")
        self.start.setFlat(True)
        self.start.setObjectName("start")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\School\\Desktop\\Lunchbox\\samp2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 350, 170, 50))
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setLineWidth(5)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("start.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(106, 145, 411, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("samp4.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 50, 331, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("samp1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 0, 71, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("exit.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(570, 0, 75, 61))
        self.quit.setText("")
        self.quit.setFlat(True)
        self.quit.setObjectName("quit")

        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.quit.raise_()
        self.start.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

#MAIN MENU UI
class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(640, 480)

        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.game = QtWidgets.QPushButton(self.centralwidget)
        self.game.setGeometry(QtCore.QRect(-10, -10, 330, 451))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(26)

        self.game.setFont(font)
        self.game.setText("")
        self.game.setFlat(True)
        self.game.setObjectName("game")
        self.movie = QtWidgets.QPushButton(self.centralwidget)
        self.movie.setGeometry(QtCore.QRect(320, -10, 330, 451))        
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(26)

        self.movie.setFont(font)
        self.movie.setText("")
        self.movie.setFlat(True)
        self.movie.setObjectName("movie")
        self.back2 = QtWidgets.QPushButton(self.centralwidget)
        self.back2.setGeometry(QtCore.QRect(0, 440, 641, 41))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(15)

        self.back2.setFont(font)
        self.back2.setText("")
        self.back2.setFlat(True)
        self.back2.setObjectName("back2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(3, 3, 315, 432))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("games.png"))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(321, 3, 315, 432))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("movies.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(3, 438, 633, 38))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("title.png"))
        self.label.setObjectName("label")

        self.label_4.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.game.raise_()
        self.movie.raise_()
        self.back2.raise_()
        MainMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "MainWindow"))

#VIDEOLISTGAME UI
class Ui_VGAME(object):
    def setupUi(self, VGAME):
        VGAME.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        VGAME.setObjectName("VGAME")
        VGAME.resize(641, 481)
        VGAME.setMinimumSize(QtCore.QSize(641, 481))
        VGAME.setWindowOpacity(1.0)
        VGAME.setAutoFillBackground(True)
        VGAME.setIconSize(QtCore.QSize(24, 24))        
        self.centralwidget = QtWidgets.QWidget(VGAME)
        self.centralwidget.setObjectName("centralwidget")

        self.Btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn1.setGeometry(QtCore.QRect(0, 0, 211, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn1.setFont(font)
        self.Btn1.setText("")
        self.Btn1.setFlat(True)
        self.Btn1.setObjectName("Btn1")

        self.Btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn4.setGeometry(QtCore.QRect(0, 220, 215, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn4.setFont(font)
        self.Btn4.setText("")
        self.Btn4.setFlat(True)
        self.Btn4.setObjectName("Btn4")

        self.Btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn2.setGeometry(QtCore.QRect(214, 0, 215, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn2.setFont(font)
        self.Btn2.setText("")
        self.Btn2.setFlat(True)
        self.Btn2.setObjectName("Btn2")

        self.Btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn5.setGeometry(QtCore.QRect(214, 219, 215, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn5.setFont(font)
        self.Btn5.setText("")
        self.Btn5.setFlat(True)
        self.Btn5.setObjectName("Btn5")

        self.Btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn3.setGeometry(QtCore.QRect(428, 0, 215, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn3.setFont(font)
        self.Btn3.setText("")
        self.Btn3.setFlat(True)
        self.Btn3.setObjectName("Btn3")

        self.Btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn6.setGeometry(QtCore.QRect(428, 219, 213, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn6.setFont(font)
        self.Btn6.setText("")
        self.Btn6.setFlat(True)
        self.Btn6.setObjectName("Btn6")

        self.back3 = QtWidgets.QPushButton(self.centralwidget)
        self.back3.setGeometry(QtCore.QRect(0, 438, 641, 43))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.back3.setFont(font)
        self.back3.setText("")
        self.back3.setFlat(True)
        self.back3.setObjectName("back3")

        self.ABC_1 = QtWidgets.QLabel(self.centralwidget)
        self.ABC_1.setGeometry(QtCore.QRect(3, 3, 209, 215))
        self.ABC_1.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_1.setText("")
        self.ABC_1.setPixmap(QtGui.QPixmap("ALPHABET.png"))
        self.ABC_1.setScaledContents(False)
        self.ABC_1.setObjectName("ABC_1")

        self.ABC_2 = QtWidgets.QLabel(self.centralwidget)
        self.ABC_2.setGeometry(QtCore.QRect(216, 3, 209, 215))
        self.ABC_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_2.setText("")
        self.ABC_2.setPixmap(QtGui.QPixmap("COLOR.png"))
        self.ABC_2.setObjectName("ABC_2")

        self.ABC_5 = QtWidgets.QLabel(self.centralwidget)
        self.ABC_5.setGeometry(QtCore.QRect(216, 221, 209, 215))
        self.ABC_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_5.setText("")
        self.ABC_5.setPixmap(QtGui.QPixmap("SHAPES.png"))
        self.ABC_5.setScaledContents(True)
        self.ABC_5.setObjectName("ABC_5")

        self.ABC_3 = QtWidgets.QLabel(self.centralwidget)
        self.ABC_3.setGeometry(QtCore.QRect(429, 3, 209, 215))
        self.ABC_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_3.setText("")
        self.ABC_3.setPixmap(QtGui.QPixmap("FRUITS.png"))
        self.ABC_3.setScaledContents(True)
        self.ABC_3.setObjectName("ABC_3")

        self.ABC_4 = QtWidgets.QLabel(self.centralwidget)
        self.ABC_4.setGeometry(QtCore.QRect(3, 221, 209, 215))
        self.ABC_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_4.setText("")
        self.ABC_4.setPixmap(QtGui.QPixmap("NUMBER.png"))
        self.ABC_4.setScaledContents(True)
        self.ABC_4.setObjectName("ABC_4")

        self.ABC_6 = QtWidgets.QLabel(self.centralwidget)
        self.ABC_6.setGeometry(QtCore.QRect(429, 221, 209, 215))
        self.ABC_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_6.setText("")
        self.ABC_6.setPixmap(QtGui.QPixmap("VEGGIES.png"))
        self.ABC_6.setScaledContents(True)
        self.ABC_6.setObjectName("ABC_6")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bleck.jpg"))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(3, 440, 634, 38))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("menu.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label.raise_()
        self.ABC_2.raise_()
        self.ABC_3.raise_()
        self.ABC_6.raise_()
        self.ABC_4.raise_()
        self.ABC_5.raise_()
        self.ABC_1.raise_()

        self.Btn1.raise_()
        self.Btn4.raise_()
        self.Btn2.raise_()
        self.Btn5.raise_()
        self.Btn3.raise_()
        self.Btn6.raise_()
        self.label_2.raise_()
        self.back3.raise_()
        VGAME.setCentralWidget(self.centralwidget)

        self.retranslateUi(VGAME)
        QtCore.QMetaObject.connectSlotsByName(VGAME)

    def retranslateUi(self, VGAME):
        _translate = QtCore.QCoreApplication.translate
        VGAME.setWindowTitle(_translate("VGAME", "VideoList"))

#VIDEOLISTMOVIE UI
class Ui_VMOVIE(object):
    def setupUi(self, VMOVIE):
        VMOVIE.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        VMOVIE.setObjectName("VMOVIE")
        VMOVIE.resize(641, 481)
        VMOVIE.setMinimumSize(QtCore.QSize(641, 481))
        VMOVIE.setWindowOpacity(1.0)
        VMOVIE.setAutoFillBackground(True)
        VMOVIE.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(VMOVIE)
        self.centralwidget.setObjectName("centralwidget")

        self.Btn1M = QtWidgets.QPushButton(self.centralwidget)
        self.Btn1M.setGeometry(QtCore.QRect(0, 0, 211, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn1M.setFont(font)
        self.Btn1M.setText("")
        self.Btn1M.setFlat(True)
        self.Btn1M.setObjectName("Btn1M")

        self.Btn4M = QtWidgets.QPushButton(self.centralwidget)
        self.Btn4M.setGeometry(QtCore.QRect(0, 220, 215, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn4M.setFont(font)
        self.Btn4M.setText("")
        self.Btn4M.setFlat(True)
        self.Btn4M.setObjectName("Btn4M")

        self.Btn2M = QtWidgets.QPushButton(self.centralwidget)
        self.Btn2M.setGeometry(QtCore.QRect(214, 0, 215, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn2M.setFont(font)
        self.Btn2M.setText("")
        self.Btn2M.setFlat(True)
        self.Btn2M.setObjectName("Btn2M")

        self.Btn5M = QtWidgets.QPushButton(self.centralwidget)
        self.Btn5M.setGeometry(QtCore.QRect(214, 219, 215, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn5M.setFont(font)
        self.Btn5M.setText("")
        self.Btn5M.setFlat(True)
        self.Btn5M.setObjectName("Btn5M")

        self.Btn3M = QtWidgets.QPushButton(self.centralwidget)
        self.Btn3M.setGeometry(QtCore.QRect(428, 0, 215, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn3M.setFont(font)
        self.Btn3M.setText("")
        self.Btn3M.setFlat(True)
        self.Btn3M.setObjectName("Btn3M")

        self.Btn6M = QtWidgets.QPushButton(self.centralwidget)
        self.Btn6M.setGeometry(QtCore.QRect(428, 219, 213, 220))
        font = QtGui.QFont()
        font.setFamily("Myriad Hebrew")
        font.setPointSize(14)
        self.Btn6M.setFont(font)
        self.Btn6M.setText("")
        self.Btn6M.setFlat(True)
        self.Btn6M.setObjectName("Btn6M")

        self.back4 = QtWidgets.QPushButton(self.centralwidget)
        self.back4.setGeometry(QtCore.QRect(0, 438, 641, 43))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.back4.setFont(font)
        self.back4.setText("")
        self.back4.setFlat(True)
        self.back4.setObjectName("back4")

        self.ABC_1M = QtWidgets.QLabel(self.centralwidget)
        self.ABC_1M.setGeometry(QtCore.QRect(3, 3, 209, 215))
        self.ABC_1M.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_1M.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_1M.setText("")
        self.ABC_1M.setPixmap(QtGui.QPixmap("ANIMALS.png"))
        self.ABC_1M.setScaledContents(False)
        self.ABC_1M.setObjectName("ABC_1M")

        self.ABC_2M = QtWidgets.QLabel(self.centralwidget)
        self.ABC_2M.setGeometry(QtCore.QRect(216, 3, 209, 215))
        self.ABC_2M.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_2M.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_2M.setText("")
        self.ABC_2M.setPixmap(QtGui.QPixmap("OPPOSITES.png"))
        self.ABC_2M.setObjectName("ABC_2M")

        self.ABC_5M = QtWidgets.QLabel(self.centralwidget)
        self.ABC_5M.setGeometry(QtCore.QRect(216, 221, 209, 215))
        self.ABC_5M.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_5M.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_5M.setText("")
        self.ABC_5M.setPixmap(QtGui.QPixmap("GGG.png"))
        self.ABC_5M.setScaledContents(True)
        self.ABC_5M.setObjectName("ABC_5M")

        self.ABC_3M = QtWidgets.QLabel(self.centralwidget)
        self.ABC_3M.setGeometry(QtCore.QRect(429, 3, 209, 215))
        self.ABC_3M.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_3M.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_3M.setText("")
        self.ABC_3M.setPixmap(QtGui.QPixmap("WEATHER.png"))
        self.ABC_3M.setScaledContents(True)
        self.ABC_3M.setObjectName("ABC_3M")

        self.ABC_4M = QtWidgets.QLabel(self.centralwidget)
        self.ABC_4M.setGeometry(QtCore.QRect(3, 221, 209, 215))
        self.ABC_4M.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_4M.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_4M.setText("")
        self.ABC_4M.setPixmap(QtGui.QPixmap("BODYPARTS.png"))
        self.ABC_4M.setScaledContents(True)
        self.ABC_4M.setObjectName("ABC_4M")

        self.ABC_6M = QtWidgets.QLabel(self.centralwidget)
        self.ABC_6M.setGeometry(QtCore.QRect(429, 221, 209, 215))
        self.ABC_6M.setFrameShape(QtWidgets.QFrame.Panel)
        self.ABC_6M.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ABC_6M.setText("")
        self.ABC_6M.setPixmap(QtGui.QPixmap("SENSES.png"))
        self.ABC_6M.setScaledContents(True)
        self.ABC_6M.setObjectName("ABC_6M")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bleck.jpg"))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(3, 440, 634, 38))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("menu.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label.raise_()
        self.ABC_2M.raise_()
        self.ABC_3M.raise_()
        self.ABC_6M.raise_()
        self.ABC_4M.raise_()
        self.ABC_5M.raise_()
        self.ABC_1M.raise_()

        self.Btn1M.raise_()
        self.Btn4M.raise_()
        self.Btn2M.raise_()
        self.Btn5M.raise_()
        self.Btn3M.raise_()
        self.Btn6M.raise_()
        self.label_2.raise_()
        self.back4.raise_()
        VMOVIE.setCentralWidget(self.centralwidget)

        self.retranslateUi(VMOVIE)
        QtCore.QMetaObject.connectSlotsByName(VMOVIE)

    def retranslateUi(self, VMOVIE):
        _translate = QtCore.QCoreApplication.translate
        VMOVIE.setWindowTitle(_translate("VMOVIE", "VideoList"))

#MOVIE POSTER UI
class Ui_MoviePlay(object):
    def setupUi(self, MoviePlay):
        MoviePlay.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MoviePlay.setObjectName("MoviePlay")
        MoviePlay.resize(640, 480)
        MoviePlay.setTabletTracking(True)
        self.centralwidget = QtWidgets.QWidget(MoviePlay)
        self.centralwidget.setObjectName("centralwidget")
        self.sing = QtWidgets.QPushButton(self.centralwidget)
        self.sing.setGeometry(QtCore.QRect(1, 0, 213, 441))
        self.sing.setText("")
        self.sing.setFlat(True)
        self.sing.setObjectName("sing")
        self.frozen = QtWidgets.QPushButton(self.centralwidget)
        self.frozen.setGeometry(QtCore.QRect(213, 0, 213, 441))
        self.frozen.setText("")
        self.frozen.setFlat(True)
        self.frozen.setObjectName("frozen")
        self.shronk = QtWidgets.QPushButton(self.centralwidget)
        self.shronk.setGeometry(QtCore.QRect(425, 0, 213, 441))
        self.shronk.setText("")
        self.shronk.setFlat(True)
        self.shronk.setObjectName("shronk")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(2, 3, 210, 474))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sng.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(214, 3, 210, 474))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("frz.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(426, 3, 210, 474))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("dddddddddd.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("bleck.jpg"))
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.frozen.raise_()
        self.shronk.raise_()
        self.sing.raise_()
        MoviePlay.setCentralWidget(self.centralwidget)

        self.retranslateUi(MoviePlay)
        QtCore.QMetaObject.connectSlotsByName(MoviePlay)

    def retranslateUi(self, MoviePlay):
        _translate = QtCore.QCoreApplication.translate
        MoviePlay.setWindowTitle(_translate("MoviePlay", "MainWindow"))

#TITLE SCREEN
class Login(QtWidgets.QMainWindow, Ui_MainWindow):

    switch = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.start.clicked.connect(self.pushbutton_handler)
        self.quit.clicked.connect(self.closeevent)

    def pushbutton_handler(self):
        self.switch.emit()

    def closeevent(self):
    	reply=QMessageBox.question(self,'Message','Are you sure you want to quit?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No )
    	if reply==QMessageBox.Yes:
    		os.system("sudo shutdown -h now");
    	else:
    		pass

#MAIN MENU BUTTONS
class Menu(QtWidgets.QMainWindow, Ui_MainMenu):
	#Switch2Title
    switch = QtCore.pyqtSignal()
    #Switch2GameList
    switchg = QtCore.pyqtSignal()
    #Switch2MovieList
    switchm = QtCore.pyqtSignal()
    #switchv = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.back2.clicked.connect(self.pushbutton_handler)
        self.game.clicked.connect(self.gamebutton_handler)
        self.movie.clicked.connect(self.moviebutton_handler)

        #pressback
    def pushbutton_handler(self):
        self.switch.emit()

        #pressgame
    def gamebutton_handler(self):
        self.switchg.emit()

    	#pressmovie
    def moviebutton_handler(self):
        self.switchm.emit()

#VIDEOLISTGAME
class VideoGame(QtWidgets.QMainWindow, Ui_VGAME):

    switch = QtCore.pyqtSignal()
    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.back3.clicked.connect(self.pushgbutton_handler)
        self.Btn1.clicked.connect(self.pushbtn1)
        self.Btn2.clicked.connect(self.pushbtn2)
        self.Btn3.clicked.connect(self.pushbtn3)
        self.Btn4.clicked.connect(self.pushbtn4)
        self.Btn5.clicked.connect(self.pushbtn5)
        self.Btn6.clicked.connect(self.pushbtn6) 

    #LIST BUTTONS
    def pushbtn1(self):
        os.system("omxplayer /opt/vc/src/hello_pi/hello_video/test.h264")
        time.sleep(1)
        os.system("emulationstation")

    def pushbtn2(self):
        os.system("")
        time.sleep(1)
        os.system("emulationstation")

    def pushbtn3(self):
        os.system("")
        time.sleep(1)
        os.system("emulationstation")

    def pushbtn4(self):
        os.system("")
        time.sleep(1)
        os.system("emulationstation")

    def pushbtn5(self):
        os.system("")
        time.sleep(1)
        os.system("emulationstation")

    def pushbtn6(self):
        os.system("")
        time.sleep(1)
        os.system("emulationstation")

    #BACKBUTTON
    def pushgbutton_handler(self):
        self.switch.emit()

#VIDEOLISTMOVIE
class Movie(QtWidgets.QMainWindow, Ui_VMOVIE, Ui_MoviePlay):

    switch = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.back4.clicked.connect(self.pushmbutton_handler)
        self.Btn1M.clicked.connect(self.pushbtn1M)
        self.Btn2M.clicked.connect(self.pushbtn2M)
        self.Btn3M.clicked.connect(self.pushbtn3M)
        self.Btn4M.clicked.connect(self.pushbtn4M)
        self.Btn5M.clicked.connect(self.pushbtn5M)
        self.Btn6M.clicked.connect(self.pushbtn6M)

    def pushbtn1M(self):
        self.posty = Poster()
        os.system("C:\\Users\\School\\Desktop\\Lunchbox\\VideoGame\\Alphabet.mp4")
        self.posty.show()

    def pushbtn2M(self):
        #self.posty = Poster()
        os.system("")
        time.sleep(1)
        #self.posty.show()

    def pushbtn3M(self):
        #self.posty = Poster()
        os.system("")
        time.sleep(1)
        #self.posty.show()

    def pushbtn4M(self):
        #self.posty = Poster()
        os.system("")
        time.sleep(1)
        #self.posty.show()

    def pushbtn5M(self):
        #self.posty = Poster()
        os.system("")
        time.sleep(1)
        #self.posty.show()

    def pushbtn6M(self):
        #self.posty = Poster()
        os.system("")
        time.sleep(1)
        #self.posty.show()

    #back4 = pushmbutton

    def pushmbutton_handler(self):
        self.switch.emit()

#MOVIEPOSTERLIST 
class Poster(QtWidgets.QMainWindow, Ui_MoviePlay):
    #SwitchBacktotitle
    switch = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.sing.clicked.connect(self.pushsing)
        self.frozen.clicked.connect(self.pushfrozen)
        self.shronk.clicked.connect(self.pushshrek)

    def TitleBack(self):
        controller = Controller()
        controller.show_login()

    def pushsing(self):
        os.system("C:\\Users\\School\\Desktop\\Lunchbox\\Movie\\Sing.mkv")
        self.switch.emit()

    if __name__ == "__TitleBack__":
        TitleBack()

    def pushfrozen(self):
        os.system("")
        self.switch.emit()
    def pushshrek(self):
        os.system("")
        self.switch.emit()
        
    #back5 = backtomenu

    def pushpbutton_handler(self):
        self.switch.emit()

        
#FUNCTIONS
class Controller():

    def __init__(self):
        pass  
    #SHOW TITLE
    def show_login(self):
        self.login = Login()
        self.login.switch.connect(self.show_menu)
        self.login.show()

    #SHOW MAIN MENU
    def show_menu(self):
        self.menu = Menu()
        self.menu.switch.connect(self.show_login) #BACK
        self.menu.switchg.connect(self.show_listgame) #GAME
        self.menu.switchm.connect(self.show_listmov) #MOVIE
        self.login.close()
        self.menu.show()

    #SHOW GAME VIDEO LIST
    def show_listgame(self):
        self.listgame = VideoGame()
        self.listgame.switch.connect(self.show_menu) #BACK
        self.menu.close()
        self.login.close()
        self.listgame.show()

    #SHOW MOVIE VIDEO LIST
    def show_listmov(self):
        self.listmov = Movie()
        self.listmov.switch.connect(self.show_menu) #BACK
        self.login.close()
        self.menu.close()
        self.listmov.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()