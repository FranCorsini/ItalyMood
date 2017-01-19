# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import schedule
import threading
from datetime import datetime #debug

from translator import Translator

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

consumer_key="51P3KpeuwPd36GlnprCAkDeym"
consumer_secret="kPVvXepP1ahCqfhDF7disL7eLqiCDh11NSH5MGO55VxbGKnNgC"

access_token="116003647-ELfyysC98T6jIBJu6HC7c6Kj6DYTyVQKAu9fY6Vl"
access_token_secret="IWBDNlcYBWOQa5hdzD05spaplyimvTnswAZcCMBA2gt5w"

class StdOutListener(StreamListener):
    tr = Translator()
    counter = 0 #understood tweets in italian
    realcounter = 0 #all tweets
    atot = 0.0
    vtot = 0.0
    booleanWriter = 0 #variabile lock
    lock = threading.Lock() 

    def on_data(self, datastream):
        data = json.loads(datastream)
        with self.lock:
            self.realcounter = self.realcounter + 1
            a,v = self.tr.translate(data['text'])
            if a != 0.0 and v != 0.0:
                self.counter = self.counter + 1
                self.atot = self.atot + a
                self.vtot = self.vtot + v
            if self.counter >= 100: #quando ottengo 1000 tweets allora calcolo colore luci e resetto
                a,v,c = self.getResults()
                self.vtot = 0.0
                self.atot = 0.0
                self.counter = 0
                self.booleanWriter = 1 #almeno scrivo (usato fuori lock)
        print(self.counter) #debug
        if self.booleanWriter:
            with open("output.txt","a") as out: #solo per debug
                out.write(str(datetime.now()))
                out.write('\n')
                out.write(str(a))
                out.write('\n')
                out.write(str(v))
                out.write('\n')
            self.booleanWriter = 0

        return True

    def on_error(self, status):
        print(status)
        if status_code == 420:
            #returning False in on_data disconnects the stream
            #TODO make the wait and reconnect
            #print('error 420')
            return False

    def getResults(self):
        a_mean = self.atot / self.counter
        v_mean = self.vtot / self.counter
        return a_mean,v_mean,self.counter

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(locations=[7.24,43.08,13.32,46.10,10.07,41.27,16.38,43.43,8.04,38.33,18.93,41.24,12.03,36.31,16.09,38.3], async=True)
    #,10.07,41.27,16.38,43.43,8.04,38.33,18.93,41.24,12.03,36.31,16.09,38.3
'''
    schedule.every(1).minutes.do(l.getResults())

    while 1:
        a_mean,v_mean,counter = schedule.run_pending()
        print(a_mean)
        print(v_mean)
        print(counter)
        time.sleep(10)

'''