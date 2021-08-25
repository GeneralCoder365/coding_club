import pyautogui
import subprocess
import datetime
# import time
from time import sleep
import os
import psutil
from typing import Union

# Opens OBS and Zoom --> Joins Zoom Meeting
def join(id, password):
    # Starts up OBS
    os.startfile(r"C:\Users\Public\Desktop\OBS Studio.lnk")
    sleep(4)
    # Checks if OBS is running
    for i in range(3):
        if ("obs64.exe" in (p.name() for p in psutil.process_iter())):
            break
        else:
            if (i == 2):
                return False
            sleep(4)
            continue

    sleep(4)

    # Starts up Zoom
    subprocess.call(r"C:\Users\Ainesh\AppData\Roaming\Zoom\bin\Zoom.exe")
    sleep(4)
    # Checks if Zoom is running
    for i in range(3):
        if ("Zoom.exe" in (p.name() for p in psutil.process_iter())):
            break
        else:
            if (i == 2):
                return False
            sleep(4)
            continue
    
    # Clicks Join Button 1
    for i in range(3):
        join1 = pyautogui.locateOnScreen(r'.\demos\zoom\join1.png')
        if join1 != None:
            pyautogui.click(join1)
            break
        else:
            if(i == 2):
                return False
            sleep(4)
            continue

    sleep(2)

    # Enters Meeting ID
    pyautogui.typewrite(id)

    # # Clicks Join Button 2
    for i in range(3):
        join2_button = pyautogui.locateOnScreen(r'.\demos\zoom\join2.png')
        if (join2_button != None):
            pyautogui.click(join2_button)
            break
        else:
            if(i == 2):
                return False
            sleep(4)
            continue

    sleep(2)

    # Optional Meeting Password:
    if (password != ""):
        # Enters Meeting Password
        pyautogui.typewrite(password)

        # Clicks Join Button 3
        for i in range(3):
            join3_button = pyautogui.locateOnScreen(r'.\demos\zoom\join3.png')
            if (join3_button != None):
                pyautogui.click(join3_button)
                break
            else:
                if(i == 2):
                    return False
                sleep(4)
                continue

            # meeting_pwd_field = pyautogui.locateOnScreen(r'.\demos\zoom\Zoom-bot-main\meeting_pwd_field.png')
            # if meeting_pwd_field != None:
                # pyautogui.click(meeting_pwd_field)
                # print("Made the Input Feild 2 active")
                # pyautogui.typewrite(password)
                # pyautogui.click(pyautogui.locateOnScreen(r'.\demos\zoom\Zoom-bot-main\join3.png'))
                # break
    
    # returns if everything ran properly
    return True

# Starts OBS and Zoom --> Joins Zoom Meeting at specific date and time
def master(month: str, day: str, year: str, military_time: str, id: str, password: str = "") -> Union[str, bool]:
    # Converts parameters into desired join datetime
    if (month.isnumeric() == False):
        month_array = ["January", "February", "March", "April", 
        "May", "June", "July", "August", "September", "October", 
        "November", "December"]

        month = str(month_array.index(month) + 1)
    if (len(month) == 1):
        month = "0" + month
    if (len(day) == 1):
        day = "0" + day
    if (len(year) == 2):
        current_year = str(datetime.datetime.now().year)
        current_century = current_year[:2]
        year = current_century + year

    
    month = int(month)
    day = int(day)
    year = int(year)
    
    military_time = military_time.split(":")
    hour: int = int(military_time[0])
    minute: int = int(military_time[1])

    join_time = datetime.datetime(year, month, day, hour, minute)


    while True:
        # Sets current time seconds to 0
        current_time = datetime.datetime.now()
        current_time = (current_time.strftime("%m,%d,%Y,%H,%M"))
        current_time = current_time.split(",")
        current_time = [int(i) for i in current_time]
        current_time = datetime.datetime(current_time[2], current_time[0], current_time[1], current_time[3], current_time[4])
        # print(current_time)
        # print(join_time)

        # Cases for joining meeting:
        # Case 1: On time
        if current_time == join_time:
            if (join(id, password) == True):
                print(f"Meeting {id} has been joined successfully!")
            break

        # Case 2: Late
        elif current_time > join_time:
            print("The meeting joining time has passed")
            break

        # Case 3: Early
        else:
            print("It is not yet time to join the meeting")
            if (join_time.day > current_time.day):
                break
            sleep(10)

# spaces in meeting id is optional
master("8", "24", "21", "23:10", "918 948 8470")
# master("8", "24", "21", "21:38", "918 948 8470", "402609")

# join("918 948 8470", "402609")