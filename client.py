import ast
import requests
import schedule
import time
#from dmxcontroller import dmxController
from datetime import datetime #debug



def main():
	#self.myDmx = dmxController()
	schedule.every(15).minutes.do(getColor)

	while 1:
		schedule.run_pending()
		time.sleep(20)

def getColor():
	req = requests.get('http://127.0.0.1:5000/api_color') #cambiare indirizzo qui
	color = ast.literal_eval(req.text)
	print 'DONE\n'
	print color
	#debug
	with open("outputcolor.txt","a") as out: 
		out.write(str(datetime.now()))
		out.write('\n')
		out.write(str(color))
		out.write('\n')


	#self.sendColor(color[0],color[1],color[2])
'''
def sendColor(val1,val2,val3):

	#TODO find channels
	self.myDmx.changeColour()
	self.myDmx.changeColour()
	self.myDmx.changeColour()
'''

if __name__ == "__main__":
    main()