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
import argparse
import xml.etree.ElementTree as ET

global screenHeight
screenWidth, screenHeight = py.size()
global start_key
start_key = "Ctrl+Alt+I"
global config

global choice
global lang
global res

def config():
    file_exists = os.path.exists(f"{os.getcwd()}/config.xml")

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reconfigure", 
        action="store_true", help="display a square of a given number")
    args = parser.parse_args()

    if args.reconfigure:
        print("a")
        file_exists = False

    if file_exists == False:

        #configuring
        choices = [
            inquirer.List(
                "choice",
                message="What should the program do?",
                choices=[("Exit Program after 12 Iteration", 0), 
                ("Exit Program after 1 Iteration", 1), 
                ("Shutdown Computer after 12 Iterations", 2)],
            ),
        ]
        
        choice = inquirer.prompt(choices)

        language = [
            inquirer.List(
                "lang",
                message="Which language are you playing on",
                choices=[("German", "v"), ("English", "l")],
            ),
        ]
        lang = inquirer.prompt(language)

        resolution = [
            inquirer.List(
                "res",
                message="With which resolution are you playing?",
                choices=[("1440p", 1440), ("1080p", 1080), 
                (f"{screenHeight}p", screenHeight)],
            ),
        ]
        res = inquirer.prompt(resolution)

        #generating new config file
        root = ET.Element("Config")
        cl = ET.Element("Configurations")

        ET.SubElement(cl, "choice").text = str(choice['choice'])

        ET.SubElement(cl, "language").text = lang['lang']

        ET.SubElement(cl, "resolution").text = str(res['res'])

        root.append(cl)  # Append the "Configurations" element to the "Config" element

        tree = ET.ElementTree(root)
        with open("config.xml", "wb") as files:
            tree.write(files)

config()
print("To start, press:", start_key, "\nTo exit the program, press: Ctrl+C")

def main():
    #reading from config.xml
    file_exists = os.path.exists(f"{os.getcwd()}/config.xml")
    if file_exists == True:
        print("Reading from config file")
        tree = ET.parse("config.xml")
        root = tree.getroot()

        choice = root.find(".//choice").text
        lang = root.find(".//language").text
        res = root.find(".//resolution").text

    #factor to convert the coordinates for the moveTo() function corresponding to the resolution of the monitor
    global factor
    factor = float(1.0)
    if res != 1080:
        factor = 1+(1080/int(res))

    i = 0
    while True:
        if choice == 0:
            if i == 12:
                print("Prgram finished successfully")
                sys.exit()
        elif choice == 1:
            if i == 1:
                print("Prgram finished successfully")
                sys.exit()
        elif choice ==2:
            if i == 12:
                print("Guten Morgen Piz")
                os.system("shutdown /s /t 10") 

        print(i+1, ". Iteration")
        time.sleep(5)
        makro()          
        i+=1

def searchPictureLang(picture_name,  message, confidence):
    location = None
    while (location == None):
        try:
            location = py.locateCenterOnScreen(f"{os.getcwd()}/pictures/{lang}/{picture_name}_{screenHeight}.jpg", 
                confidence = confidence)
            confidence -= 0.001
        except Exception as e:
            print(e)
    print(message, location)   
    py.moveTo(location)  
    py.click()

def searchPicture(picture_name,  message, confidence):
    location = None
    while (location == None):
        try:
            location = py.locateCenterOnScreen(f"{os.getcwd()}/pictures/universal/{picture_name}_{screenHeight}.jpg", 
                confidence = confidence)
            confidence -= 0.001
        except Exception as e:
            print(e)
    print(message, location)   
    py.moveTo(location)  
    py.click()    

def makro():

    #start game
        searchPictureLang("start", "Start Game |", 0.60) 

    #click red button
        searchPictureLang("button", "Start Match |", 0.60) 

    #spawn enemy grenadiers in your base 
        #spawn troups
        searchPicture("cheat", "Open cheat menue |", 0.60)   
        searchPicture("ostheer", "'Ostheer' slected |", 0.80)   
        searchPicture("infantry", "'Infantry' selected |", 0.80)   
        searchPicture("grenadiers", "spawned grenadiers |", 0.80)
        #making them enemies
        searchPicture("grenadiers_symbole", "Selected the grenadiers |", 0.80)
        searchPicture("selection", "'Selection' selected |", 0.80)
        searchPicture("owner", "'Owner' selected |", 0.80)
        searchPicture("enemy", "enemy grenadiers |", 0.80)

    #wait 5 minutes
        time.sleep(295) #changing back because of task beforehand

    #winning condition
        searchPicture("game", "'Game,Ai,&FOW' selected |", 0.80)
        searchPicture("end", "'End game' selected |", 0.80)
        py.moveTo(732*factor, 373*factor)
        searchPicture("confirm", "'confirm' selected |", 0.80)
        time.sleep(1)
        py.click()

    #leaving match
        time.sleep(7)
        keyboard.press(Key.Enter)
        keyboard.type(f"/{lang}")
        keyboard.press(Key.Enter) 

    #close statistics
        searchPictureLang("close", "Closing Statistics |", 0.80)


# Hotkeys registrieren
keyboard.add_hotkey(start_key, main)
keyboard.wait()