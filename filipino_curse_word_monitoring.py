import speech_recognition as sr
import keyboard
from pynput.mouse import Controller
from time import sleep

r = sr.Recognizer()
  
def unblockinput():       
    for i in range(150):
        keyboard.unblock_key(i)
    print("\n[Keyboard and Mouse Unblocked]\n")

def blockinput():
    mouse = Controller()
    for i in range(150):
        keyboard.block_key(i)
    print("\n[Keyboard and Mouse Blocked for 10 Seconds]\n")
    i = 0;
    while i <= 320:
        mouse.position = (0, 0)
        i = i + 1;
        sleep(0.03125)
    
def recog():
    with sr.Microphone(2) as source:
        print("Detecting...\n")
        r.energy_threshold = 8000
        audio = r.listen(source)

        try:
            text = str(r.recognize_google(audio,language="fil-PH")).lower()
            print(text+"\n")

            curses = ["bwisit", "gago", "gaga", "puta", "putang ina", "tang ina", "tarantado", "bobo", "boba", "tanga", "punyeta"]

            if any(curse in text for curse in curses):
                print("[Filipino Curse Word Detected]")
                blockinput()
                unblockinput()                

            recog()

        except:
            recog()

recog()