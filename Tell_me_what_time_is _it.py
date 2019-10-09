#!/usr/bin/python
import time
import os

class spell(object ):
    def __init__(self ):
        #self.argument=argv
        self.hour=time.strftime("%H")
        self.minutes=time.strftime("%M")
        a2 = ["Sono le ore :","e" ,"minuti"]
        self.frase= a2[0]  + self.hour + a2[1] + self.minutes + a2[2] + str(object)
        print ("_______INIZIO FRASE____ : \n\n " ,self.frase , "\n")
        print ("___________FINE FRASE ________ ")
        windows= 0
        if os.environ.get('OS')=="Windows_NT":
            windows =1
        else:
            windows =0

    def talk(self):
        '''This library it's run with Windows and MacOSX'''
        #print (argv)
        if os.environ.get('OS')=="Windows_NT":
            from win32com.client import Dispatch
            speack = Dispatch ("SAPI.SpVoice")
            speack.Speak(self.frase)
        else:
            '''' UNIX'''
            os.system("say self.frase")
    def talk_time(talk):
        if os.environ.get('OS')=="Windows_NT":
            speack.Speak(self.frase) # da modificare
        else:
            os.system("say self.frase") # da modificare


A=spell()
A.talk() #.talk_time()
