from pynput.mouse import Button, Controller
import time
from datetime import datetime
import subprocess

mouse = Controller()

slackOpened = False

def openSlack():
    #subprocess.call(
    #["/usr/bin/open", "-W", "-n", "-a", "/Applications/Slack.app"]
    #)
    time.sleep(3)
    pos = (865.1015625, 871.875)
    mouse.position = pos
    time.sleep(2)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(5)

while True: 
    print("kake")
    time.sleep(3)
    mouse.move(20,20)
    time.sleep(1)
    mouse.move(-20,-20)
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    print(hour)
    if (hour == 8 and minute > 1) and not slackOpened:
        openSlack()
        slackOpened = True