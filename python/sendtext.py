from subprocess import call
import doorState as door

def sendText(message):
   
    time = door.getDoorTime()
    msg = message + " " + time
    mark="7858658049"
    number="4807078873"
    #call(["ls","-l"])
    url="http://textbelt.com/text"
    ptype="POST"
    call(["curl","-X",ptype,url,"-d", "number="+number, "-d",  "message="+msg])



