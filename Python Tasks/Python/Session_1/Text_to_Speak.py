import vlc
from gtts import gTTS

myObj = gTTS(text = "Hello Mostafa How Are You ? Hope You Are Fine", lang= 'en', slow= False )

myObj.save("welcome.mp4")

audio = vlc.MediaPlayer("./Python\Tasks/welcome.mp4")

audio.play()

while True:
    pass


