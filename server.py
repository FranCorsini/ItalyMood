from threading import Thread
from flask import Flask
app = Flask(__name__)


class serverApp(Thread):

	#@app.route('/color')
	def api_color():
		global tweetListener
		return tweetListener.getColor()
	app.add_url_rule('/api_color',view_func = api_color)

	def run(self):
		app.run()

	def __init__(self, listener):
		global tweetListener
		Thread.__init__(self)
		tweetListener = listener

