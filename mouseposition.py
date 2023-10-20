import pyautogui as py
import keyboard
import time

def main():
	start_key = "<strg+alt+i>"

	screenWidth, screenHeight = py.size()

	print(screenHeight)

	factor = float(1.0)

	if screenHeight != 1080:
		factor == 1+(1080/screenHeight)

	currentMouseX, currentMouseY = py.position()
	print(currentMouseX, currentMouseY)

	
	py.moveTo(882*factor, 555*factor)

	print(currentMouseX, currentMouseY)
	
	print(screenHeight)
	print(screenHeight)
	print(screenHeight)
	print(screenHeight)
	print(screenHeight)
	print(screenHeight)
	print(screenHeight)
	print(screenHeight)
	print(screenHeight)
	print(screenHeight)
	print(screenHeight)
	print(screenHeight)

def stop_code():
    # Hier wird der Code für die Beendigung gestartet
    print("Code beendet")
    keyboard.unhook_all()

# Hotkeys registrieren
keyboard.add_hotkey('Ctrl+Alt+I', main)
keyboard.add_hotkey('Ctrl+Alt+Q', stop_code)

keyboard.wait()