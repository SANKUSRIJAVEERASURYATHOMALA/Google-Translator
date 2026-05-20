from gtts import gTTS
import speech_recognition as spr
from googletrans import Translator
import os

def Speech():

    r = spr.Recognizer()

    with spr.Microphone() as s:

        print("Speak...")

        audio = r.listen(s, phrase_time_limit=20)

        text = r.recognize_google(audio)

        print("English :", text)

        # translator
        t = Translator()

        hindi = t.translate(text, dest="hi")

        print("Hindi :", hindi.text)

        # text to speech
        speech = gTTS(text=hindi.text, lang="hi")

        speech.save("stt.mp3")

        # play audio
        os.system("start stt.mp3")

Speech()