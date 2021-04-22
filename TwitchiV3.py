# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:29:13 2021

@author: greed
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import requests
import webbrowser
import threading
from os import environ

nomAppli = "Twitchi"	
global URLLive

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()

class theTwitcher(QWidget):
    
    def __init__(self):
        super(theTwitcher, self).__init__()
                
        global nomAppli
        self.setWindowTitle(nomAppli)
        self.setupUi()
        self.setupConnection()

        self.show()
        
    def setupUi(self):
        
        
        #Base
        self.gridLayout = QGridLayout(self)
        self.resize(400,120)
        
        #Declaration de bases
        self.info = QLabel("Entrer le nom de votre streamer favori")
        self.name = QLineEdit()
        self.name.setPlaceholderText("nom du streamer ici")
        self.boutonOk = QPushButton("lancé")
        
        #Emplacement 
        self.gridLayout.addWidget(self.info,1 ,0 ,1 ,6)
        self.gridLayout.addWidget(self.name,2 ,0 ,1 ,6)
        self.gridLayout.addWidget(self.boutonOk,3 ,0 ,1 ,6)
        
                    
        
        #CSS
        self.info.setStyleSheet("QLabel { color: white}")
        self.name.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);padding: 1px;border-style: solid;border: 1px solid #1e1e1e;border-radius: 5;")
        self.boutonOk.setStyleSheet("color: #b1b1b1;background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);border-width: 1px;border-color: #1e1e1e;border-style: solid;border-radius: 6;padding: 3px;font-size: 12px;padding-left: 5px;padding-right: 5px;min-width: 40px;")
        
        #Menu
        self.menuBar = QMenuBar(self)
        self.infoMenu = self.menuBar.addMenu('Info')
        self.contact = self.menuBar.addMenu('Contact')
        self.codeSource = self.menuBar.addMenu('Code source')
        self.menuBar.setStyleSheet("""
                QMenuBar {
                    background-color: rgb(49,49,49);
                    color: rgb(255,255,255);
                    border: 1px solid ;
                }
                QMenu::item:selected {
                    background-color: rgb(204,232,255);   
                }
                """)
        
        #sous menu
        self.credit = QAction("Credit" , self)
        self.fonctionnement = QAction('Fonctionnement', self)
        self.version = QAction("Version", self)  
        self.infoMenu.addAction(self.version)
        self.infoMenu.addAction(self.fonctionnement)
        self.infoMenu.addAction(self.credit)
        
        self.mail = QAction("Mail", self)
        self.discord = QAction("Discord", self)
        self.contact.addAction(self.discord)
        self.contact.addAction(self.mail)
        
        self.github = QAction("Github", self)
        self.codeSource.addAction(self.github)
    
    def setupConnection(self):
        #module de base
        self.boutonOk.clicked.connect(self.boutonOkDef)


        
        #module du menu
        self.version.triggered.connect(self.versionDef)
        self.fonctionnement.triggered.connect(self.fonctionnementDef)
        self.credit.triggered.connect(self.creditDef)
        
        self.mail.triggered.connect(self.mailDef)
        self.discord.triggered.connect(self.discordDef)
        
        self.codeSource.triggered.connect(self.codeSourceDef)
      
    def creditDef(self):    
        class creditClass(QWidget):
            def __init__(self):
                super(creditClass, self).__init__()
                global nomAppli
                self.setWindowTitle(nomAppli)
                self.setupUi2()
            def setupUi2(self):
                self.gridLayout = QGridLayout(self)
                self.resize(150,50)
                urlLink="<p>Auteur: <a href=\"https://www.twitch.tv/mrvietsky\" style=\"color:red;\">'MrVietsky'</a></p>\n<p>Developpeur: Mahieux (<a href=\"https://tenchigreed.fr\"style=\"color:red;\">'TenchiGreed'</a>) Dany</p>"
                self.info = QLabel(urlLink)
                self.info.setOpenExternalLinks(True)
                self.gridLayout.addWidget(self.info,0 ,0 ,0 ,0)  

        self.fenetre4 = creditClass()
        self.fenetre4.setStyleSheet("color: #b1b1b1; background-color: #323232;")
        self.fenetre4.show()
        
    def codeSourceDef(self):
        webbrowser.open("https://github.com/Tenchigreed/twitchi")
          
    def versionDef(self):
        class versionClass(QWidget):
            
            def __init__(self):
                super(versionClass, self).__init__()
                global nomAppli
                self.setWindowTitle(nomAppli)
                self.setupUi2()
            def setupUi2(self):
                self.gridLayout = QGridLayout(self)
                self.resize(150,50)
                self.info = QLabel("Version 3.1\n")
                self.gridLayout.addWidget(self.info,0 ,0 ,0 ,0)
                
        self.fenetre2 = versionClass()
        self.fenetre2.setStyleSheet("color: #b1b1b1; background-color: #323232;")
        self.fenetre2.show()
                
    def fonctionnementDef(self):
        class fonctionnemenClass(QWidget):
            
            def __init__(self):
                super(fonctionnemenClass, self).__init__()
                global nomAppli
                self.setWindowTitle(nomAppli)
                self.setupUi2()
            def setupUi2(self):
                self.gridLayout = QGridLayout(self)
                self.resize(200,200)
                self.info = QLabel("Fonctionnement:\nL'application à pour but de lancer une page web sur le stream de votre choix \nsi un live est en cours.\nSi la chaine n'est pas en live, l'application verifiera toutes les 10 minutes l'état actuel de la chaine")
                self.gridLayout.addWidget(self.info,0 ,0 ,0 ,0)

                
        self.fenetre3 = fonctionnemenClass()
        self.fenetre3.setStyleSheet("color: #b1b1b1; background-color: #323232;")
        self.fenetre3.show()
     
    def discordDef(self):
        webbrowser.open("https://discord.gg/pYN8Mvw")
    
    def mailDef(self):
        class mailClass(QWidget):
            def __init__(self):
                super(mailClass, self).__init__()
                global nomAppli
                self.setWindowTitle(nomAppli)
                self.setupUi2()
            def setupUi2(self):
                self.gridLayout = QGridLayout(self)
                self.resize(150,50)
                self.info = QLabel("Pour toutes informations ou suggestion d'amélioration ,\n n'hésite pas à me contacter à l'adresse suivante : tenchigreed@live.fr")
                self.info.setOpenExternalLinks(True)
                self.gridLayout.addWidget(self.info,0 ,0 ,0 ,0)  

        self.fenetre5 = mailClass()
        self.fenetre5.setStyleSheet("color: #b1b1b1; background-color: #323232;")
        self.fenetre5.show()
        
        
        
    def boutonOkDef(self):
        global username
        global URLLive
        username = str(self.name.text())
        self.boutonOk.deleteLater()
        self.name.deleteLater()
        text = "Merci d'avoir choisi " + username + ", une page web s'ouvrira automatiquement dès le lancement du stream \nUne fois fermée, cette application ira dans vos icônes cachées"
        self.info.setText(text)
        URLLive = "https://www.twitch.tv/" + username
        
        def check(self):   
            global username
            self.URL = 'https://api.twitch.tv/helix/streams?user_login='
            self.authURL = 'https://id.twitch.tv/oauth2/token'
            self.Client_ID = "rlbvnlol28w3aaejgvjg943zruwq54"
            self.Secret  = "3d886df4wiej5yblm7xek7jvndcrh1"
            self.AutParams = {'client_id': self.Client_ID,'client_secret': self.Secret,'grant_type': 'client_credentials' }
        
            self.URL = self.URL + username
            
            self.AutParams = {'client_id': self.Client_ID,
                              'client_secret': self.Secret,
                              'grant_type': 'client_credentials'
                              }
                        
                        
            AutCall = requests.post(url=self.authURL, params=self.AutParams) 
            access_token = AutCall.json()['access_token']
            
            head = {
                'Client-ID' : self.Client_ID,
                'Authorization' :  "Bearer " + access_token
                }
                        
            r = requests.get(self.URL, headers = head).json()['data']
                        
            if r:
                r = r[0]
                if r['type'] == 'live':
                    return True
                else:
                    return False
            else:
                return False     
      
            
      
        class MyThread(threading.Thread):    
            def run(self):
                statuLive = True
                global URLLive
                global kill
                
                while 1:
                    live = check(self)
                    if live == True:
                        if statuLive == True:
                            webbrowser.open(URLLive)
                            statuLive = False
        
                        else :
                            for i in range(3600):
                                time.sleep(1)
                            
                    else :
                        statuLive = True
                        for i in range(600):
                            time.sleep(1)
        
                        
        mythread = MyThread(name = "ThreadBoucle")
        mythread.start()

       
app = QApplication([])
fenetre = theTwitcher()
fenetre.show()
fenetre.setStyleSheet("color: #b1b1b1; background-color: #323232;")
app.exec_()

app.setQuitOnLastWindowClosed(False)

icon = QIcon("icon.png")

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()
action = QAction("Fenetre")
menu.addAction(action)
action.triggered.connect(fenetre.show)

quit = QAction("Quit")
menu.addAction(quit)
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)

app.exec_()
