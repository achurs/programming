import time
import os

time.sleep(10)
for i in range(1,101):
    message = str(i)
    os.system(f"adb shell input text {message}")
    os.system("adb shell input keyevent 66")  # Send the message (ENTER key)
    time.sleep(1)