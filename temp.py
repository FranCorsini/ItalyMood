# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from translator import Translator


def temp():
    tr = Translator()

    #tweet = 'In fatto di falso nn siete secondi a nessuno'
    #tweet = 'Cinque anni fa, oggi, avevo girato tutti i negozi della Lombardia per poi arrendermi e fare il mio primo ordine online'
    tweet = "ho mangiato 500 cioccolatini ma parte questo tutto okay"
    a,v = tr.translate(tweet)
    print('arousal:' + str(a))
    print('valence:' + str(v))
    '''
    with open('output','w') as out:
        out.write(a)
        out.write('\n')
        out.write(v)
    '''

temp()