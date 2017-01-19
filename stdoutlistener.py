# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import json
import schedule
import threading
from datetime import datetime 
from tweepy.streaming import StreamListener


from translator import Translator


class StdOutListener(StreamListener):
    tr = Translator()
    counter = 0 #understood tweets in italian
    realcounter = 0 #all tweets
    atot = 0.0
    vtot = 0.0
    alla = []
    allv = []
    booleanWriter = 0 #variabile lock
    lastTime = datetime.now() #time of start
    lock = threading.Lock() 
    color = 'blue' #this is the defaoult one

    def on_data(self, datastream):
        data = json.loads(datastream)
        with self.lock:
            self.realcounter = self.realcounter + 1
            a,v = self.tr.translate(data['text'])
            if a != 0.0 and v != 0.0:
                self.counter = self.counter + 1
                self.atot = self.atot + a
                self.vtot = self.vtot + v
            if self.counter >= 5: #quando ottengo 100 tweets allora calcolo media
                print('uno') #debug
                a,v = self.getResults()
                self.alla.append(a)
                self.allv.append(v)
                self.vtot = 0.0
                self.atot = 0.0
                self.counter = 0
                self.booleanWriter = 1 #almeno scrivo (usato fuori lock) per debug
                now = datetime.now()
                if self.mins_between(self.lastTime,now) >= 2: #se sono passati almeno 60 mins allora calcolo e cambio colore
                    print('due') #debug
                    self.lastTime = now
                    color = self.calculateColour(self,self.alla,self.allv)
                    slef.alla[:] = []
                    self.allv[:] = []
        #only for debug
        print(self.counter) #debug
        '''
        if self.booleanWriter: #solo per debug
            with open("output.txt","a") as out: 
                out.write(str(datetime.now()))
                out.write('\n')
                out.write(str(a))
                out.write('\n')
                out.write(str(v))
                out.write('\n')
            self.booleanWriter = 0
        '''
        return True

    def calculateColor(self,a,v): #a e v sono liste delle medie di ogni 100 tweets
        print('calculate')
        size = len(a)
        totA = 0.0
        totV = 0.0
        for elem in a:
            totA = elem + totA
        for elem in v:
            totV = elem + totV
        totA = totA / size
        totV = totV / size    
    #TODO make the colour here 
        print('colorset')
    	self.color = 'green' #debug color

    def getColor(self):
    	return self.color

    def mins_between(self,d1, d2):
        print('difference') #debug
        print(abs((d2 - d1).days * 24 * 60))
        print('yea')
        return abs((d2 - d1).days * 24 * 60)

    def on_error(self, status):
        print('on_error\n')
        print(status)
        if status_code == 420:
            #returning False in on_data disconnects the stream
            #TODO make the wait and reconnect
            #print('error 420')
            return False

    def getResults(self):
        a_mean = self.atot / self.counter
        v_mean = self.vtot / self.counter
        return a_mean,v_mean

    def __init__(self):
        pass