import speech_recognition
import pyttsx3
import os
import playsound
import webbrowser as web
import datetime
from gtts import gTTS

class Alexa():
    recognizer  = speech_recognition.Recognizer()

    def Speak(self, user_speech):
        audio = gTTS(text = user_speech, lang= 'en', slow= False )
        audio_file = "audio.mp3"
        audio.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)
    
    def Listen(self):
        try:
            with speech_recognition.Microphone() as mic:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(mic)
                audio = self.recognizer.listen(mic)
                user_speech = self.recognizer.recognize_google(audio, language = "en-US")
                user_speech = user_speech.lower()
                return user_speech

        except speech_recognition.UnknownValueError:
            self.Speak("Sorry Can You Repeat, I couldn't understand that")
        except speech_recognition.RequestError:  
            self.Speak("Sorry, There was an error processing your request")
        return ""

    def search_words(self,list,text):
        for word in list:            
            if word in text:
                return True
        return False


alexa = Alexa()
welcome_text = "Hello Mostafa, How Can I Help You ?"
print(welcome_text)
alexa.Speak(welcome_text)


while True:
    user_speech = alexa.Listen()
    now = datetime.datetime.now()
    print(user_speech)
    
    if alexa.search_words(["time","clock","hour"],user_speech):
        alexa.Speak( str(now.time().strftime("%I:%M:%P")) )

    elif alexa.search_words(["date","calender","today"],user_speech):
        alexa.Speak(str(now.date()))

    elif alexa.search_words(["gmail","email"],user_speech):
        alexa.Speak("I will mark all your Emails to be Read") 
        os.system("cd Python\ Tasks/Python/Session_3")   
        os.system("python3 PyAutoGui_Email.py")
        
