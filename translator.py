import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source2:

    r.adjust_for_ambient_noise(source2, duration=0.2)

    print("Say something")
    audio = r.listen(source2)
    print("Recognizing now...")
    try: 
        # sv-SE
        text = r.recognize_google(audio, language="sv-SE")
        text = text.lower()
        print(text)
        # translated = GoogleTranslator(source='auto', target='english').translate(text)
        # print(translated)
        # SpeakText(translated)
    except Exception as e:
        print("error: " + str(e))
    