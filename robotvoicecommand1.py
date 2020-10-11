# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:22:56 2020

@author: soorya
"""
import speech_recognition as sr
def robotvoicecommand():
 recognizer = sr.Recognizer()
 microphone=sr.Microphone() 
 with microphone as source:
        print("start")
        recognizer.adjust_for_ambient_noise(source)# #  analyze the audio source for 1 second
        print("####")

        print("Listening")
        audio = recognizer.listen(source,phrase_time_limit=10)

        print("####")
        print("speech to text")
        try:
            text = recognizer.recognize_google(audio)
            print(text)
            if "kitchen" in text:
               #going to kitchen code
                  print("Going to Kitchen")
            elif "room 1" in text:
               #Going to Room 1 code
                  print("Going to Room 1")
            elif "room 2" in text:
                #Going to Room 2 code
                  print("Going to Room 2")
            elif (("living room")or("living"))  in text:
                #Going to Room 1 code
                  print("Going to Hall")
            else:
                  print("Enter Valid Command")
       

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
robotvoicecommand()