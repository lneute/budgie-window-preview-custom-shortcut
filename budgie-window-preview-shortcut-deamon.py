#!/bin/python3

"""
It listens for the right and left arrow keys, and when they are pressed, it copies the trigger files
to the `/tmp` folder  
"""

import os
import argparse
from pynput import keyboard
from shutil import copy


# Constants:

# Setting the HOME_DIR to the user's home directory, the DEFAULT_DIR to the user's home directory with
# the .triggers-budgie folder, the USER to the user's username, and the TEMP to the /tmp folder.
HOME_DIR = os.environ["HOME"]
DEFAULT_DIR = os.path.join(HOME_DIR, ".triggers-budgie")
USER = os.environ["USER"]
TEMP = "/tmp/"

# Creating a dictionary with the keys `next` and `prev` and the values are the trigger files names.
TRIGGERS = {"next":f"{USER}_nexttrigger", 
            "prev":f"{USER}_previoustrigger"}

# Arguments:
# Parsing the arguments that the user passes to the script.
parser = argparse.ArgumentParser()
parser.add_argument("-d", help="Set custom location for the 'triggers' directory")
parser.add_argument("-n", action="store_true", help="Enable toasty notification on startup")
args = parser.parse_args()

# Notify:
def send_toast(message, body, timer=1000):
    """
    It sends a toast notification to the user.
    
    :param message: The title of the notification
    :param body: The body of the notification
    :param timer: The time in milliseconds that the toast will be displayed, defaults to 1000 (optional)
    """
    try:
        cmd = f"notify-send -t {timer} '{message}' '{body}'"
        os.system(cmd)
    except:
        pass

# Check the custom trigger_path
if args.d and os.path.exists(args.d):
    folder = args.d
elif args.d:
    send_toast("budgie-custom-shortcut", f"Unable to find directory, fallback is {DEFAULT_DIR}")
    folder = DEFAULT_DIR
else:
    folder = DEFAULT_DIR


def valid_dir(dir_path):
    """
    If the directory path exists and is a directory, return True, otherwise return False
    
    :param dir_path: The path to the directory to be checked
    :return: True or False
    """

    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        return True

    return False


def check_folder(dir_path):
    """
    Checking if the directory exists and if it doesn't it creates it.
    """
    
    valid = valid_dir(dir_path)
    
    if not valid:
        
        os.makedirs(dir_path, exist_ok=True)
        
        return True

    
def check_triggers():
    """
    It checks if the trigger files exist, and if they don't, it creates them
    """

    for _, v in TRIGGERS.items():
        filename = os.path.join(folder, v)
        exist = os.path.exists(filename)

            
        if not exist:
            create_triggers(filename)


def create_triggers(path):
    """
    > This function creates a trigger file in the specified path
    
    :param path: The path to the trigger file
    """
    
    with open(path, "w") as f:
        send_toast("Trigger Created", f"Trigger {os.path.split(path)[-1]} was created successfully")


def main():
    """
    It listens for the right and left arrow keys, and when they are pressed, it copies the trigger files
    to the `/tmp` folder
    """

    if args.n:
        send_toast("Daemon Started", "Serivice budgie-custom-shortcut is running")

    next_trigger = os.path.join(folder, TRIGGERS["next"])
    prev_trigger = os.path.join(folder, TRIGGERS["prev"])

    with keyboard.Events() as events:
        c = 0
        while True:
            event = events.get()

            if event.key == keyboard.Key.right and "neute_prvtrigger_all" in os.listdir("/tmp"):
                c+=1
                if c % 2 == 0:
                    copy(next_trigger, f"/tmp/{TRIGGERS['next']}")
                
                
            elif event.key == keyboard.Key.left:
                c+=1
                if c % 2 == 0:
                    copy(prev_trigger, f"/tmp/{TRIGGERS['prev']}")
            
            if c == 100:
                c = 0

if __name__ == "__main__":
    check_folder(folder)
    check_triggers()
    main()




        
        