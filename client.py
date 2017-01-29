import ast
import requests
import schedule
import time
from dmxcontroller import dmxController
from datetime import datetime #debug

myDmx = dmxController()

def main():
	schedule.every(1).minutes.do(getColor)

	while 1:
		try:
			schedule.run_pending()
			time.sleep(20)
		except Exception as e:
			print e
			time.sleep(900)

def getColor():
	req = requests.get('http://127.0.0.1:5000/api_color') #cambiare indirizzo qui
	color = ast.literal_eval(req.text)
	print color
	global myDmx
	myDmx.changeColor(color[0],color[1],color[2])


	#debug
	'''
	with open("outputcolor.txt","a") as out: 
		out.write(str(datetime.now()))
		out.write('\n')
		out.write(str(color))
		out.write('\n')
	'''

	
if __name__ == "__main__":
    main()