# Importing necessary modules
import keyboard
import pyautogui
import json
import time
import os

shortcut = 'alt+x'  # define your hot-key

# template
template = {
    "current_account": "rizzitis",
    "accounts": {
        "rizzitis": {
            "agents": {
                "q": {
                    "agent_name": "jett",
                    "coords": [
                        962,
                        842
                    ]
                },
                "w": {
                    "agent_name": "raze",
                    "coords": [
                        1219,
                        842
                    ]
                },
                "e": {
                    "agent_name": "reyna",
                    "coords": [
                        1290,
                        842
                    ]
                }
            }
        }
    },
    "lockin": [
        952,
        728
    ]
}

# check weather data.json exists
if not os.path.isfile('data.json'):
    with open("data.json", 'w') as f:
        json.dump(template, f)

# reading JSON file
with open('data.json') as f:
    data = json.load(f)

lockIn = data['lockin'] # coordinates of lock in

agents = data["accounts"][data['current_account']]['agents'] # fetching agents data

# functions which triggers the process of locking
def trigger(key):
    try:
        # selecting and clicking agent for 17 time
        for i in range(0, 18):
            
            pyautogui.click(agents[key]['coords'][0], agents[key]['coords'][1]) # clicking on agent
            
            pyautogui.click(lockIn[0], lockIn[1]) # clicking on lockin

    except Exception as e:
        pass

def insta_locking():
    while True:
        for key in agents:
            
            if keyboard.is_pressed(key): # checking which key is pressed
                trigger(key)
                return
        
        if keyboard.is_pressed('esc'): # exiting program if escape pressed
            return
        time.sleep(0.1)  # Adding a small delay to reduce CPU usage

def main():
    
    keyboard.add_hotkey(shortcut, insta_locking) # Intiating shortcut key
   
    keyboard.wait('esc') # Waiting till user presses escape

main()
