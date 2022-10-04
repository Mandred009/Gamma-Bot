# The Voice Recognizer for Gamma
import speech_recognition as sr
import arduino_communication

r = sr.Recognizer()


def get_text():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print('Started')
        arduino_communication.set("speak",1)
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="en-us")
            print('Ended')
            arduino_communication.set("nospeak", 1)
            return text
        except:
            arduino_communication.set("nospeak", 1)
            return 'err:No Voice'
