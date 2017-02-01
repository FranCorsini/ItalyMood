from pydmx import DMXConnection
from time import sleep


class dmxController():
	mydmx = DMXConnection('COM3')

	prevR = 0
	prevG = 0
	prevB = 0
	redVal = 0
	grnVal = 0
	bluVal = 0

	def changeColor(self,red,green,blue):
		self.crossFade(red,green,blue)

	def calculateStep(self,prevValue,endValue):
		step = endValue - prevValue
		if step:
			 step = 1020/step
		return step

	def calculateVal(self,step,val,i):
		if step != 0 and i % step == 0:
			if step > 0:
				val = val + 1
			elif step < 0:
				val = val - 1
		if val > 255:
			val = 255
		elif val < 0:
			val = 0
		return val

	def crossFade(self,R,G,B):
		stepR = self.calculateStep(self.prevR, R)
		stepG = self.calculateStep(self.prevG, G)
		stepB = self.calculateStep(self.prevB, B)

		for i in range(0,1020):
			self.redVal = self.calculateVal(stepR, self.redVal, i)
			self.grnVal = self.calculateVal(stepG, self.grnVal, i)
			self.bluVal = self.calculateVal(stepB, self.bluVal, i)

			self.mydmx.setChannel(146, 255) 
			self.mydmx.setChannel(147, redVal) # set DMX channel 1 
			self.mydmx.setChannel(148, grnVal) # set DMX channel 2 
			self.mydmx.setChannel(149, bluVal) # set DMX channel 3 
			self.mydmx.render() 

			sleep(0.01)

			#debug color (in the for cicle)
			'''
			if i == 0 or i % 60 == 0:
				print("Loop/RGB: #");
				print(i);
				print(" | ");
				print(self.redVal);
				print(" / ");
				print(self.grnVal);
				print(" / ");  
				print(self.bluVal);
				print('\n') 
			'''

		self.prevR = self.redVal
		self.prevG = self.grnVal
		self.prevB = self.bluVal
