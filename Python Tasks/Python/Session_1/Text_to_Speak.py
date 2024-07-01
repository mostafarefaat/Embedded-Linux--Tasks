from gtts import gTTS
import playsound
import os

myObj = gTTS(text = "Hello Mostafa How Are You ?", lang= 'en', slow= False )

audio = "welcome.mp3"

myObj.save(audio)

playsound.playsound(audio)
os.remove(audio)



