# Central Nervous System Module for Gamma
import time
import datetime
import voice_module
import websearch_module
import weather_module
import application_open_module
import arduino_communication

voice_input = ""
gamma_wakeup = 0
arduino_communication.set("sleep", 10000)

start_time = datetime.datetime.now()
print(start_time)
rest_time = 60  # in minutes


def find_key(txt):
    txt = str.lower(txt)
    if 'edge browser' in txt:
        searchtxt = txt.replace('edge browser', '')
        websearch_module.search(searchtxt, 'edge', False)
        arduino_communication.set("edge", 10)
        return

    if 'weather' in txt:
        l = str.split(txt)
        # print(l)
        try:
            ind = l.index('city')
        except:
            return
        weather_txt = weather_module.get_weather(l[ind + 1])
        arduino_communication.set(weather_txt, 1)
        return

    if 'search' in txt:
        searchtxt = txt.replace("search", "")
        engine = 'youtube' in searchtxt
        searchtxt = searchtxt.replace("youtube", "")
        if 'brave browser' in txt:
            searchtxt = searchtxt.replace('brave browser', '')
            websearch_module.search(searchtxt, 'brave', engine)
            arduino_communication.set("brave", 10)
        if 'chrome browser' in txt:
            searchtxt = searchtxt.replace('chrome browser', '')
            websearch_module.search(searchtxt, 'chrome', engine)
            arduino_communication.set("chrome", 10)

    if 'open' in txt:
        searchtxt = txt.replace('open', '')
        opener(searchtxt.strip())

    if 'hands' in txt:
        searchtxt = txt.replace('hands', '')
        arduino_communication.set(searchtxt.strip(), 2)
    if 'light' in txt:
        arduino_communication.set(txt.strip(), 2)
    if 'timer' in txt:
        arduino_communication.set("stop", 5)
        global start_time
        start_time = datetime.datetime.now()
    if 'time' in txt:
        arduino_communication.set("Time {}".format(datetime.datetime.now().strftime("%H:%M:%S")), 2)
    if 'music' in txt:
        searchtxt = "music"
        engine = False
        if 'brave browser' in txt:
            websearch_module.search(searchtxt, 'brave', engine)
            arduino_communication.set("brave", 10)
        if 'chrome browser' in txt:
            websearch_module.search(searchtxt, 'chrome', engine)
            arduino_communication.set("chrome", 10)


def opener(txt):
    application_open_module.process(txt)


while True:
    voice_input = str.lower(voice_module.get_text())
    print(voice_input)
    if voice_input == 'gamma activate' or voice_input == 'gama activate':
        arduino_communication.set("activate", 10)
        gamma_wakeup = 1
        print("I am Awake Mandred Sir")
        arduino_communication.set("N", 100)
        continue
    if voice_input == 'gamma deactivate' or voice_input == 'gama deactivate':
        arduino_communication.set("deactivate", 10)
        gamma_wakeup = 0
        print("Good Night Mandred Sir")
        arduino_communication.set("sleep", 10000)
        continue

    if gamma_wakeup == 1:
        find_key(voice_input)
        diff_time = datetime.datetime.now() - start_time
        timecheck = divmod(diff_time.total_seconds(), 60)[0]
        if timecheck >= rest_time:
            print('Time to Stretch')
            arduino_communication.set("both", 10)
