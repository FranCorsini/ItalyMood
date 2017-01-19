
from tweepy import OAuthHandler
from tweepy import Stream

from server import serverApp
from stdoutlistener import StdOutListener
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

consumer_key="51P3KpeuwPd36GlnprCAkDeym"
consumer_secret="kPVvXepP1ahCqfhDF7disL7eLqiCDh11NSH5MGO55VxbGKnNgC"

access_token="116003647-ELfyysC98T6jIBJu6HC7c6Kj6DYTyVQKAu9fY6Vl"
access_token_secret="IWBDNlcYBWOQa5hdzD05spaplyimvTnswAZcCMBA2gt5w"



if __name__ == '__main__':


	#setup lo stream listener
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	#fai partire server per le CURLs
	ser = serverApp(l)
	ser.start()


	#fai partire lo stream listener
	stream = Stream(auth, l)
	try:
		stream.filter(locations=[7.24,43.08,13.32,46.10,10.07,41.27,16.38,43.43,8.04,38.33,18.93,41.24,12.03,36.31,16.09,38.3], async=True)
	except Exception as e:
		print('here except\n')
		print(e)