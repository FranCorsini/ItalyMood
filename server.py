from threading import Thread
from flask import Flask
from flask_classy import FlaskView
app = Flask(__name__)


class serverApp(Thread,FlaskView):
	route_base = "/"

	def color(self):
		return self.tweetListener.getColor()

	def run(self):
		app.run()

	def __init__(self, listener):
		Thread.__init__(self)
		self.tweetListener = listener

serverApp.register(app)



