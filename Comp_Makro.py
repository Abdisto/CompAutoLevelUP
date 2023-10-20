#!/usr/bin/python
# -*- coding: latin-1 -*-

import pyautogui as py
import trio, sys
import time                 
import os
from datetime import datetime
import keyboard
import pprint
sys.path.append(os.path.realpath("."))
import inquirer

configuration = [
    inquirer.List(
        "config",
        message="What should the programm do?",
        choices=[("Exit Programm after 12 Iteration", 0), ("Exit Programm after 1 Iteration", 1), ("Shutdown Computer after 12 Iterations", 2)],
    ),
]
config = inquirer.prompt(configuration)

start_key = "Ctrl+Alt+I"
close_key = "Ctrl+C"
print("To start, press:", start_key, "\nTo exit the programm, press:", close_key)

def main():
    screenWidth, screenHeight = py.size()
    #Faktor zur Umrechnung der Koordinaten für die moveTo() Funktion
    factor = float(1.0)
    if screenHeight != 1080:
        factor == 1+(1080/screenHeight)

    i = 0
    while True:
        if config == 0:
            if i == 12:
                print("Prgramm finished successfull")
                sys.exit()
        elif config == 1:
            if i == 1:
                print("Prgramm finished successfull")
                sys.exit()
        elif config ==2:
            if i == 12:
                print("Guten Morgen Piz")
                os.system("shutdown /s /t 10") 

        print(i+1, ". Iteration")
        time.sleep(5)
        makro()          
        i+=1

def searchPicture(picture_name,  message, confidence):
    location = None
    while (location == None):
        try:
            location = py.locateCenterOnScreen(picture_name.screenHeight.jpg, confidence = confidence)
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
            location = py.locateCenterOnScreen(picture_name.screenHeight.jpg, confidence = confidence)
            confidence -= 0.001
        except Exception as e:
            print(e)
    print(message, location)   
    py.moveTo(location)  
    py.click()

def makro():

    #start game
        searchPicture("start", "Start Game |", 0.60) 

    #click "Taste dr�cken"
        searchPicture("button", "Start Match |", 0.60) 

    #spawn enemy grenadiers in your base
            

    #Base of enemy            
    #    searchPicture("base", "Gegnerische Basis anvisiert |", 0.60)  

    #spawnen troups
        searchPicture_2("cheat", "Cheat Men� ge�ffnet |", 0.60)   
        searchPicture_2("ostheer", "Ostheer ausgew�hlt |", 0.80)   
        searchPicture_2("infantry", "Infantry ausgew�hlt |", 0.80)   
        searchPicture_2("grenadiere", "Grenadiere gespawnt |", 0.80)

    #wait 5 minutes
        time.sleep(300) # exact is like 295 for me but lag could be in the way so i am being generous

    #destroy enemy base
        #searchPicture_2("misk.jpg", "misk ausgew�hlt |", 0.80)   
        #searchPicture_2("kill_everything.jpg", "kill everything ausgew�hlt |", 0.80)   
        #searchPicture_2("radius_15m.jpg", "Alles im Radius von 15 metern zers�rt |", 0.90)

    #Match verlassen
        time.sleep(7)
        keyboard.press(Key.Enter)
        keyboard.type("/v")
        keyboard.press(Key.Enter) 

    #close statistics
        searchPicture("close", "Match schlie�en|", 0.80)

        #Timer schl�gt 5 Minuten
        #location = None
        #while (location == None):
        #    try:
        #        location = py.locateCenterOnScreen('end_time.jpg', confidence = 0.8)
        #    except Exception as e:
        #        print(e)   
        #print("5 Minuten vergangen")

# Hotkeys registrieren
keyboard.add_hotkey('Ctrl+Alt+I', main)

keyboard.wait()