
from tweepy import OAuthHandler
from tweepy import Stream

from server import serverApp
from stdoutlistener import StdOutListener
from color import getColor
import random
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

consumer_key="51P3KpeuwPd36GlnprCAkDeym"
consumer_secret="kPVvXepP1ahCqfhDF7disL7eLqiCDh11NSH5MGO55VxbGKnNgC"

access_token="116003647-ELfyysC98T6jIBJu6HC7c6Kj6DYTyVQKAu9fY6Vl"
access_token_secret="IWBDNlcYBWOQa5hdzD05spaplyimvTnswAZcCMBA2gt5w"

#setup lo stream listener
l = StdOutListener()

#fai partire server per le CURLs
ser = serverApp(l)
ser.start()





#questo nel caso la connessione va giu, mette random mentre tenta di riconnetersi
def doBackup():
	print('backup Color')
	v = random.uniform(5.45, 5.7)
	a = random.uniform(4.0, 4.2)
	backupColor = getColor(v,a)
	l.setColor(backupColor)
	time.sleep(900) #aspetta per 15 mins


def main():
	#fai partire lo stream listener
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	try:
		stream.filter(locations=[7.24,43.08,13.32,46.10,10.07,41.27,16.38,43.43,8.04,38.33,18.93,41.24,12.03,36.31,16.09,38.3])
	except Exception as e:
		print(e)
		return False

if __name__ == '__main__':
	while 1:
		print('RECONNECTING')
		err = main()
		if err == False:
			#go backup for one hour then try to reconnect
			doBackup()
			doBackup()
			doBackup()
			doBackup()