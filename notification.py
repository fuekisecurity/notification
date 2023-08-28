from plyer import notification
import os

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

cls()
title = input("Enter Title > ")
message = input("Enter Message > ")
time = int(input("Enter Timeout > "))

notification.notify(title=title, message=message, timeout=time)
