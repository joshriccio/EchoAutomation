import detectdoor
import threading

def startmonitor(message):
    print("starting door monitor")
    child=threading.Thread(target=detectdoor.monitordoor, args=(message,))
    child.start()
    return


