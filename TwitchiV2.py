# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:29:13 2021

@author: greed
"""
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QLineEdit, QLabel, QAction, QMenu , QSystemTrayIcon)
from PyQt5.QtGui import ( QIcon)
import time
import requests
import webbrowser
import threading

nomAppli = "Twitchi"	
global URLLive
kill = False
class theTwitcher(QWidget):
    


    def __init__(self):
        super(theTwitcher, self).__init__()
        


        global nomAppli
        self.setWindowTitle(nomAppli)
        self.setupUi()
        self.setupConnection()


        self.show()
        
    

    def setupUi(self):
        
        self.gridLayout = QGridLayout(self)
        self.resize(300,20)

        self.info = QLabel("Entrer le nom de votre streamer favori")
        self.name = QLineEdit()
        self.name.setPlaceholderText("nom du streamer ici")
        self.boutonOk = QPushButton("lancé")
        
        self.gridLayout.addWidget(self.info,1 ,0 ,1 ,6)
        self.gridLayout.addWidget(self.name,2 ,0 ,1 ,6)
        self.gridLayout.addWidget(self.boutonOk,3 ,0 ,1 ,6)
        

        self.info.setStyleSheet("QLabel { color: white}")
        self.name.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);padding: 1px;border-style: solid;border: 1px solid #1e1e1e;border-radius: 5;")
        self.boutonOk.setStyleSheet("color: #b1b1b1;background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);border-width: 1px;border-color: #1e1e1e;border-style: solid;border-radius: 6;padding: 3px;font-size: 12px;padding-left: 5px;padding-right: 5px;min-width: 40px;")
        
    def setupConnection(self):
        
        self.boutonOk.clicked.connect(self.boutonOkDef)
        
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
            self.Client_ID = " "
            self.Secret  = " "
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
                                if kill == True:
                                    break
                                time.sleep(1)
                            
                    else :
                        statuLive = True
                        for i in range(600):
                            if kill == True:
                                break
                            time.sleep(1)
        
                        
        mythread = MyThread(name = "ThreadBoucle")
        mythread.start()
       
def killApp():
    kill = True
    app.quit

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

