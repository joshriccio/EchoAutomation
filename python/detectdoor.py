import threading
import sendtext, os, time
path_to_watch = "/home/pi/hackaz/python/log.txt"

def monitordoor(message):
    before = os.path.getmtime(path_to_watch)
    print("timestamp before: ")
    print(before)
    while 1:
        time.sleep(3)
        after = os.path.getmtime(path_to_watch)
        if before != after:
            sendtext.sendText(message)
            print("timestamp after: ")
            print(after)
            print("text sent")
            return

