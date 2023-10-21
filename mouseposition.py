import pyautogui as py
import keyboard
import time

def main():
	start_key = "<strg+alt+i>"

	screenWidth, screenHeight = py.size()

	print(screenHeight)

	factor = float(1.0)

	if screenHeight != 1080:
		factor = (int(screenHeight)/1080)
	print(factor)
	currentMouseX, currentMouseY = py.position()
	print(currentMouseX, currentMouseY)

	py.moveTo(732*factor, 373*factor)

	currentMouseX, currentMouseY = py.position()
	print(currentMouseX, currentMouseY)

# not working while code is running -> resorting back to keyboard interupt
def stop_code():
    # Hier wird der Code für die Beendigung gestartet
    print("Code beendet")
    keyboard.unhook_all()

# Hotkeys registrieren
keyboard.add_hotkey('Ctrl+Alt+I', main)
keyboard.add_hotkey('Ctrl+Alt+Q', stop_code)

keyboard.wait()