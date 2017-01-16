from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging
import doorState as door
import launchdetectdoor
import sendtext

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('GPIOControlIntent', mapping={'status': 'status'})
def gpio_control(status):

   # try:
   #     pinNum = int(pin)
   # except Exception as e:
   #     return statement('The light is not connected.')
    pinNum = 18
    GPIO.setup(pinNum, GPIO.OUT)

    if status in ['on', 'high']:    GPIO.output(pinNum, GPIO.HIGH)
    if status in ['off', 'low']:    GPIO.output(pinNum, GPIO.LOW)

    return statement('Turning light {}'.format(status))

@ask.intent('ReportIntent', mapping={})
def report_control():
    if(GPIO.input(18)):
        led_status = "on"
    else:
        led_status = "off"
    time = door.getDoorTime()
    state = door.getDoorState()
    
    if(state == 'OUT'):
        return statement('The light is {}, and the dog went outside at {}'.format(led_status, time))
    else:
        return statement('The light is {}, and the dog came inside at {}'.format(led_status, time)) 

@ask.intent('DoggyDoorIntent', mapping={})
def report_control():                                                                                       
    time = door.getDoorTime()
    state = door.getDoorState()
    if(state == 'OUT'):
        return statement('The dog went outside at {}'.format(time))
    else:
        return statement('The dog came inside at {}'.format(time))

@ask.intent('DoorIntent', mapping={'door_name': 'door_name'})
def report_control(door_name):                                                                                                
    time = door.getDoorTime()                                                                                      
    return statement('The {} opened at {}'.format(door_name, time))                                                   

@ask.intent('SMSIntent', mapping={'object_name': 'object_name'})
def report_control(object_name):
    launchdetectdoor.startmonitor("The dog came in")                                                                                
    return statement('Alright, I will text you when the {} comes in'.format(object_name))

@ask.intent('JobIntent', mapping={'city': 'city', 'job': 'job'})
def report_control(city, job):                                                                              
    sendtext.sendText("Here are the jobs I found https://www.indeed.com/jobs?q=software+engineer&l=Tucson%2C+AZ")
    return statement('Alright, I will find you a {} job in {}'.format(job, city))

if __name__=='__main__':
    port=5000 # this may be different
    app.run(host='0.0.0.0', port=port)
