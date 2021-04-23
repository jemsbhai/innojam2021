
import os
import pyttsx3
import random
import speech_recognition as sr
import time
from subprocess import Popen
from datetime import datetime
import calendar
from PIL import Image                                                                                
import gcpvisionlib
import gcpocrlib




maindelay = 5  #delay for main loop

r = sr.Recognizer()

def showimage(filename):
    img = Image.open(filename)
    img.show() 


def getSpeech():
    text = "human"
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return text

def speak(sentence):
    eng = pyttsx3.init()
    eng.setProperty('rate', 130) 
    eng.say(sentence)
    eng.runAndWait()
    print(sentence)
    eng.stop() 



count = 0

while (1) :
    count +=1

    ##detect user with distance/motion

    ##led flash


    ## play opening sequence
    # omxp = Popen(['omxplayer', eye1movie])
    
    speak("hello, how may i assist you?")
    name = getSpeech()
    name = name.lower()
    if "scan" in name or "detect" in name:

        command = "Image acquired. please wait for analysis"
        speak(command)

        imgfile = "crosswalk.jpeg"

        if count == 1:
            imgfile = "crosswalk.jpeg"
        
        if count == 1:
            imgfile = "speedbump.jpeg"

        if count == 3:
            imgfile = "street.png"


        if count == 4:
            break



        showimage(imgfile)

        desc = gcpvisionlib.describe(imgfile)

        command = "The scene looks like " + desc
        speak(command)

        command = "python gcpuploader.py " +  imgfile + " innojam"
        os.system(command)
        imgurl = "https://storage.googleapis.com/innojam/" + imgfile


        command = "attempting to read labels."
        speak(command)

        text =  gcpocrlib.detect_text_uri(imgurl)

        command = "The following text was detected " + text
        speak(command)



        ts = int(time.time())

        dt_object = datetime.fromtimestamp(ts)

        print('Day of Week (name): ', calendar.day_name[dt_object.weekday()])
        day = str(calendar.day_name[dt_object.weekday()])
        dom = str(dt_object.day)
        month = calendar.month_name[dt_object.month]
        hour = str(dt_object.hour)
        minute = str(dt_object.minute)
        print (month)
        print (dom)
        
        outs = "sign scan recorded at " + dom + " " + month + " " + day + " "+ hour + " " + minute

    

        speak(outs + ", record updated. ")

        continue
        


    if "exit" in name:
    
        ts = int(time.time())

        dt_object = datetime.fromtimestamp(ts)


        print('Day of Week (name): ', calendar.day_name[dt_object.weekday()])
        day = str(calendar.day_name[dt_object.weekday()])
        dom = str(dt_object.day)
        month = calendar.month_name[dt_object.month]
        hour = str(dt_object.hour)
        minute = str(dt_object.minute)
        print (month)
        print (dom)
        
        outs = "exit recorded at " + dom + " " + month + " " + day + " "+ hour + " " + minute

    

        speak(outs + ", goodbye. ")
        break



    
    speak("sorry, i did not understand this command ... ")



    time.sleep(maindelay)

    if count == 4:
        break


