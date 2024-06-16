# InstaLocking Script

This script allows users to automate the process of selecting agents in a game using keyboard shortcuts. By pressing a predefined hotkey, users can initiate the insta-locking function, which will automatically select a specified agent. The process continues until the user presses the `esc` key to exit the program.

## Features

- **Hotkey Activation**: Start the insta-locking process by pressing a predefined shortcut key (`alt+x` by default).
- **Agent Selection**: Automatically clicks on specified agent coordinates multiple times.
- **Loop Until Escape**: Continues running the insta-locking loop until the user presses `esc` to exit.
- **Customizable**: Modify the `data.json` file to specify different accounts and agents with their respective coordinates.

## Requirements

- Python 3.x
- `keyboard` library
- `pyautogui` library
- `pyuac` library

You can install the required libraries using pip:
```sh
pip install keyboard pyautogui pyuac
````

# How To Use?
1. Download the latest package of the .exe file.
2. Copy the .exe file into an empty folder.
3. Run the file to initiate the boilerplate data.json.
4. Customize data.json according to your needs.
> [!NOTE]
> The initial data.json file includes the coordinates of agents Jett, Reyna, and Raze, as well as the lock-in button according to the latest June 2024 Valorant update. The coordinates are based on a resolution of 1920 x 1080.

- Follow these steps to customize coordinates according to your needs:
  1. Go to [this link](https://www.image-map.net/) to find the coordinates of agents and the lock-in button.
  2. Update the coordinates of the lock-in button and agents in data.json.

5. All done! Now, all you need to do is run the .exe file. The .exe file will run in the background. To initiate the agent selection hotkey, press ```alt+x```. Once you press the hotkey for agent selection, to       initiate it again, press ```alt+x```. To exit the program or close the running .exe file, press ```esc```.

# Setup
1. Clone repository on your local machine
   ````sh
   git clone https://github.com/rishi-boi/valorant-instalocking.git
   ````
2. Navigate to project directory
   ````sh
   cd valorant-instalocking
   ````
3. Install required libraries
   ````sh
   pip install -r requirements.txt
   ````
# Usage
1. Open terminal (run as administrator) and navigate to your project directory.
2. Run the script
   ````sh
   python main.py
   ````
3. Press the predefined shortcut key (``alt+x`` by default) to start the insta-locking process.
4. The script will continuously check for agent selection keys. Press any of the predefined agent keys (q, w, e) to select an agent.
5. To exit the insta-locking loop, press the ``esc`` key.

# ``data.json`` Structure
The data.json file should contain the following structure:
```
{
    "current_account": "rizzitis",
    "accounts": {
        "rizzitis": {
            "agents": {
                "q": {
                    "agent_name": "jett",
                    "coords": [962, 842]
                },
                "w": {
                    "agent_name": "raze",
                    "coords": [1219, 842]
                },
                "e": {
                    "agent_name": "reyna",
                    "coords": [1290, 842]
                }
            }
        }
    },
    "lockin": [952, 728]
}
```
- ``current_account``: The account currently in use.
- ``accounts``: Contains details of each account.
  - ``agents``: Defines the agents and their selection coordinates.
- ``lockin``: Coordinates for the lock-in button.

> [!TIP]
> I would love to see your views from you. Feel free to fill  [feedback](https://docs.google.com/forms/d/1i62PVIGzZ_DyPLJy0MhO7cbh-qoWMVvKhnhLfQlae1w) form

# Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any changes you'd like to make.

# License
This project is licensed under the MIT License. See the ``LICENSE`` file for details.
