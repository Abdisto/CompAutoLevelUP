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

def main():
    global screenHeight
    screenWidth, screenHeight = py.size()
    global start_key
    start_key = "Ctrl+Alt+I"
    global config

    global choice
    global lang
    global res

    choice, lang, res = config()
    print("To start, press:", start_key, "\nTo exit the program, press: Ctrl+C")

    def run():
        i = 0
        w = workload(lang, res)

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
            time.sleep(2)
            w.makro()         
            i+=1

    # Hotkeys registrieren
    keyboard.add_hotkey(start_key, run)
    keyboard.wait()

class workload:
    def __init__(self, lang, res):
        self.lang = lang
        self.res = res
        
        self.factor = float(1.0)
        if res != 1080:
            self.factor = (int(res)/1080)

    def searchPicture(self, picture_name,  message, confidence, language="universal"):
        language = language or self.lang
        location = None
        while (location == None):
            try:
                location = py.locateCenterOnScreen(f"{os.getcwd()}/pictures/{language}/{picture_name}_{screenHeight}.jpg", 
                    confidence = confidence)
                confidence -= 0.001
            except Exception as e:
                print(e)
        print(message, location)   
        py.moveTo(location)  
        py.click()

    def makro(self):
        #start game
        self.searchPicture("start", "Start Game |", 0.60, language=None) 

    #click red button
        self.searchPicture("button", "Start Match |", 0.80, language=None) 

    #spawn enemy grenadiers in your base 
        #spawn troups
        self.searchPicture("cheat", "Open cheat menue |", 0.90)   
        self.searchPicture("ostheer", "'Ostheer' slected |", 0.90)   
        self.searchPicture("infantry", "'Infantry' selected |", 0.90)   
        self.searchPicture("grenadiere", "spawned grenadiere |", 0.90)
        #making them enemies
        self.searchPicture("symbol", "Selected the grenadiere |", 0.90)
        self.searchPicture("selection", "'Selection' selected |", 0.90)
        self.searchPicture("owner", "'Owner' selected |", 1.00)
        self.searchPicture("enemy", "enemy grenadiere |", 0.90)

    #wait 5 minutes
        time.sleep(295) #changing back because of task beforehand

    #winning condition
        self.searchPicture("game", "'Game,Ai,&FOW' selected |", 0.90)
        self.searchPicture("end", "'End game' selected |", 0.90)
        py.moveTo(732*factor, 373*factor)
        print("You win!")
        self.searchPicture("confirm", "'confirm' selected |", 0.90)
        time.sleep(1)
        py.click()

    #leaving match
        time.sleep(7)
        py.press("enter")
        py.write(f"/{self.lang}")
        py.press("enter") 

    #close statistics
        self.searchPicture("close", "Closing Statistics |", 0.80, language=None)

def config():
    file_exists = os.path.exists(f"{os.getcwd()}/config.xml")

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reconfigure", 
        action="store_true", help="reconfigure your old configs")
    args = parser.parse_args()

    if args.reconfigure:
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
                (f"{screenHeight}p (auto generated)", screenHeight)],
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

        return choice["choice"], lang["lang"], res["res"]  # Return values when creating a new config

    else:
        print("Reading from config file")
        tree = ET.parse("config.xml")
        root = tree.getroot()

        choice = root.find(".//choice").text
        lang = root.find(".//language").text
        res = root.find(".//resolution").text

        return choice, lang, res

if __name__ == "__main__":
    main()