#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
import sys
import time
import argparse
import xml.etree.ElementTree as ET
import inquirer
import pyautogui as py
import keyboard

global screenHeight
screenWidth, screenHeight = py.size()
global start_key
start_key = "Ctrl+Alt+I"
global config

# Global variables
global choice
global lang
global res

def config():
    file_exists = os.path.exists(f"{os.getcwd()}/config.xml")

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reconfigure", action="store_true", help="display a square of a given number")
    args = parser.parse_args()

    if args.reconfigure:
        print("a")
        file_exists = False

    if not file_exists:
        # Configuring
        choices = [
            inquirer.List(
                "choice",
                message="What should the program do?",
                choices=[
                    ("Exit Program after 12 Iteration", 0),
                    ("Exit Program after 1 Iteration", 1),
                    ("Shutdown Computer after 12 Iterations", 2)
                ],
            ),
        ]

        global choice
        choice = inquirer.prompt(choices)

        language = [
            inquirer.List(
                "lang",
                message="Which language are you playing on",
                choices=[("German", "v"), ("English", "l")],
            ),
        ]
        global lang
        lang = inquirer.prompt(language)

        resolution = [
            inquirer.List(
                "res",
                message="With which resolution are you playing?",
                choices=[("1440p", 1440), ("1080p", 1080), (f"{screenHeight}p", screenHeight)],
            ),
        ]
        global res
        res = inquirer.prompt(resolution)

        # Generating new config file
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
print(f"To start, press: {start_key}\nTo exit the program, press: Ctrl+C")

def main():
    # Reading from config.xml
    file_exists = os.path.exists(f"{os.getcwd()}/config.xml")
    if file_exists:
        print("Reading from config file")
        tree = ET.parse("config.xml")
        root = tree.getroot()

        choice = root.find(".//choice").text
        lang = root.find(".//language").text
        res = root.find(".//resolution").text

    # Factor to convert the coordinates for the moveTo() function corresponding to the resolution of the monitor
    global factor
    factor = 1.0
    if res != "1080":
        factor = 1 + (1080 / int(res))

    i = 0
    while True:
        if choice == "0":
            if i == 12:
                print("Program finished successfully")
                sys.exit()
        elif choice == "1":
            if i == 1:
                print("Program finished successfully")
                sys.exit()
        elif choice == "2":
            if i == 12:
                print("Guten Morgen Piz")
                os.system("shutdown /s /t 10")

        print(f"{i + 1}. Iteration")
        time.sleep(5)
        makro()
        i += 1

def search_picture_lang(picture_name, message, confidence):
    location = None
    while location is None:
        try:
            location = py.locateCenterOnScreen(f"{os.getcwd()}/pictures/{lang}/{picture_name}_{screenHeight}.jpg", confidence=confidence)
            confidence -= 0.001
        except Exception as e:
            print(e)
    print(f"{message} {location}")
    py.moveTo(location)
    py.click()

def search_picture(picture_name, message, confidence):
    location = None
    while location is None:
        try:
            location = py.locateCenterOnScreen(f"{os.getcwd()}/pictures/universal/{picture_name}_{screenHeight}.jpg", confidence=confidence)
            confidence -= 0.001
        except Exception as e:
            print(e)
    print(f"{message} {location}")
    py.moveTo(location)
    py.click()

def makro():
    # Start game
    search_picture_lang("start", "Start Game |", 0.60)

    # Click red button
    search_picture_lang("button", "Start Match |", 0.60)

    # Spawn enemy grenadiers in your base
    # Spawn troops
    search_picture("cheat", "Open cheat menu |", 0.60)
    search_picture("ostheer", "'Ostheer' selected |", 0.80)
    search_picture("infantry", "'Infantry' selected |", 0.80)
    search_picture("grenadiers", "Spawned grenadiers |", 0.80)
    # Making them enemies
    search_picture("grenadiers_symbole", "Selected the grenadiers |", 0.80)
    search_picture("selection", "'Selection' selected |", 0.80)
    search_picture("owner", "'Owner' selected |", 0.80)
    search_picture("enemy", "Enemy grenadiers |", 0.80)

    # Wait 5 minutes
    time.sleep(295)  # Changing back because of task beforehand

    # Winning condition
    search_picture("game", "'Game, Ai, & FOW' selected |", 0.80)
    search_picture("end", "'End game' selected |", 0.80)
    py.moveTo(732 * factor, 373 * factor)
    search_picture("confirm", "'Confirm' selected |", 0.80)
    time.sleep(1)
    py.click()

    # Leaving match
    time.sleep(7)
    keyboard.press(Key.Enter)
    keyboard.type(f"/{lang}")
    keyboard.press(Key.Enter)

    # Close statistics
    search_picture_lang("close", "Closing Statistics |", 0.80)

# Hotkeys register
keyboard.add_hotkey(start_key, main)
keyboard.wait()
