#!/usr/bin/python
# -*- coding: latin-1 -*-

import pyautogui as py
import trio, sys
import time                 
import asyncio
from datetime import datetime
from pynput import keyboard

#config
start_key = "<strg+alt+i>"
close_key = "<strg+alt+q> | not working whilst makro started"
print("to start, press:", start_key, "\nto exit the programm, press:", close_key)

def searchPicture(picture_name,  message, confidence):
    location = None
    while (location == None):
        try:
            location = py.locateCenterOnScreen(picture_name, confidence = confidence)
            time.sleep(1)
            py.click()     #Kein Plan ob das funktioniert
            confidence -= 0.001
        except Exception as e:
            print(e)
    print(message, location)   
    py.moveTo(location)  
    py.click() 
    
def searchPicture_2(picture_name,  message, confidence):
    location = None
    while (location == None):
        try:
            location = py.locateCenterOnScreen(picture_name, confidence = confidence)
            confidence -= 0.001
        except Exception as e:
            print(e)
    print(message, location)   
    py.moveTo(location)  
    py.click()

def makro():
      
    i = 1
    while True:
        print(i, ". Itteration")
        time.sleep(5)

    #start game
        searchPicture("start.jpg", "Starte Spiel |", 0.60) 
    #move mouse to center
        screenWidth, screenHeight = py.size()
        py.moveTo(screenWidth/2, screenHeight/2)
    #click "Beliebige Taste drücken"
        searchPicture("taste.jpg", "Starte Match |", 0.60) 
    #Base of enemy            
        searchPicture("base.jpg", "Gegnerische Basis anvisiert |", 0.60)  
    #spawnen troups
        searchPicture_2("cheat.jpg", "Cheat Menü geöffnet |", 0.60)   
        searchPicture_2("ostheer.jpg", "Ostheer ausgewählt |", 0.80)   
        searchPicture_2("infantry.jpg", "Infantry ausgewählt |", 0.80)   
        searchPicture_2("grenadiere.jpg", "Grenadiere gespawnt |", 0.80)
    #move mouse to center
        screenWidth, screenHeight = py.size()
        py.moveTo(screenWidth/2, screenHeight/2)           
    #wait 5 minutes
        time.sleep(300)
    #destroy enemy base
        searchPicture_2("misk.jpg", "misk ausgewählt |", 0.80)   
        searchPicture_2("kill_everything.jpg", "kill everything ausgewählt |", 0.80)   
        searchPicture_2("radius_15m.jpg", "Alles im Radius von 15 metern zersört |", 0.90) 
    #move mouse to center
        screenWidth, screenHeight = py.size()
        py.moveTo(screenWidth/2, screenHeight/2)
    #clicking until "Match beenden" appears
        searchPicture("beenden.jpg", "Match beendet |", 0.80)   
    #close statistics
        searchPicture("close.jpg", "Match schließen|", 0.80)
    #move mouse to center
        screenWidth, screenHeight = py.size()
        py.moveTo(screenWidth/2, screenHeight/2)
                      
        i+=1

        #Timer schlägt 5 Minuten
        #location = None
        #while (location == None):
        #    try:
        #        location = py.locateCenterOnScreen('end_time.jpg', confidence = 0.8)
        #    except Exception as e:
        #        print(e)   
        #print("5 Minuten vergangen")

def exit():
    sys.exit()
#funktioniert nicht da synchron

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+i': makro,     
        '<ctrl>+<alt>+q': exit}) as h:
        h.join()    