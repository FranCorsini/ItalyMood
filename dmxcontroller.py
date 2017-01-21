import pysimpledmx

class dmxController():
	mydmx = pysimpledmx.DMXConnection(3)

	def changeColour(ch,val):
		mydmx.setChannel(1, 255) # set DMX channel 1 to full
		mydmx.setChannel(2, 128) # set DMX channel 2 to 128
		mydmx.setChannel(3, 0)   # set DMX channel 3 to 0
		mydmx.render()    # render all of the above changes onto the DMX network