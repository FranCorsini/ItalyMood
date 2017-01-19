# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Translator():
    itadic = dict()
    engdic = dict()
    #load dictionary
    def __init__(self):
        with open('itadictionary.csv','r') as infile:
            for line in infile:
                temp = line.split(',')
                self.itadic[str(temp[0])] = [float(temp[1]),float(temp[2])]

        with open('engdictionary.csv','r') as infile:
            for line in infile:
                temp = line.split(',')
                self.engdic[str(temp[0])] = [float(temp[1]),float(temp[2])]


    def translate(self, sentence):
        words = []
        wordcounter = 0
        realwords = [] #debug
        a = 0.0
        v = 0.0
        words = sentence.lower().split(' ')
        for word in words: #rimuovi punteggiatura (altrimenti non riconosce parole)
            for ch in ['.','?','!']:
                if ch in word:
                    word=word.replace(ch,'')
            if str(word).startswith('#'): #case hashtag
                word = word[1:]
                if self.itadic.get(word,'None') != 'None': #è nel dic ita?
                    wordcounter = wordcounter + 1
                    v = v + self.itadic.get(word,'None')[0]
                    a = a + self.itadic.get(word,'None')[1]
                    realwords.append(word) #debug
                elif self.engdic.get(word,'None') != 'None': #è nel dic eng?
                    wordcounter = wordcounter + 1
                    v = v + self.engdic.get(word,'None')[0]
                    a = a + self.engdic.get(word,'None')[1]
                    realwords.append(word)
            else: #case normal word
                if self.itadic.get(word,'None') != 'None': #è nel dic ita?
                    wordcounter = wordcounter + 1
                    v = v + self.itadic.get(word,'None')[0]
                    a = a + self.itadic.get(word,'None')[1]
                    realwords.append(word)
        if wordcounter > 1: #deve essere più di due parole
            a = a/wordcounter
            v = v/wordcounter
            '''
            with open("outputtweets.txt","a") as out: #debug
                out.write(str(a))
                out.write('\n')
                out.write(str(v))
                out.write('\n')
                out.write(str(realwords))
                out.write('\n')
                out.write(sentence)
                out.write('\n')
                out.write('\n') 
            '''
        else:
            a = 0.0
            v = 0.0

        return a,v
