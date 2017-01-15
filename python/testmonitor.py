import threading
import detectdoor

message="this is a message from a thread"
def my_service():
    print("starting monitor")
    monitor.start()
    print("monitor started")
    return

monitor=threading.Thread(name="monitordoor", target=detectdoor.monitordoor, args=(message,))
p=threading.Thread(name="my_service", target=my_service)

p.start()
