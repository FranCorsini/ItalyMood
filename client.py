import request
import schedule
import time
from dmxcontroller import dmxController




def main():
	self.myDmx = dmxController()
    schedule.every(1).hours.do(getColor)

    while 1:
        schedule.run_pending()
        time.sleep(20)

def getColor():
	req = requests.get('http://127.0.0.1:5000/api_color') #cambiare indirizzo qui
	color = req.text

	#qui c'è il traduttore colore a valori dmx

	self.sendColor()

def sendColor(val1,val2,val3):
	self.myDmx.changeColour()
	self.myDmx.changeColour()
	self.myDmx.changeColour()