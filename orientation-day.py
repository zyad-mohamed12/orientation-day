import pyttsx3
import speech_recognition as sr
import serial

ser=serial.Serial('COM3', 9660)
MASTER = "sir"

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 170)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    talk("I am Atena... How may I help you?")
def takeCommand():
    command = None
    while command is None:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Recognising...")
            command = r.recognize_google(audio, language= 'en-us')
            print(f"sir said: {command}\n")
            print(command)

        except Exception:
            command = None
    
    if 'turn on' in command:
             talk('Sir, which led you want to turn on')
             with sr.Microphone() as source:
              print('listening...')
              voice = listener.listen(source)
              led = listener.recognize_google(voice)
              led = led.lower()
             if led == 'blue':
                    ser.write(b'1')
             elif led == 'red':
                    ser.write(b'3')
             elif led == 'yellow':
                    ser.write(b'5')
             elif led == 'all of them':
                    ser.write(b'8')
             elif led == 'police lights':
                    ser.write(b'9')

                    
             talk('turning on' + led + ' led')
    elif 'turn off' in command:
            talk('Sir, which led you want to turn off')
            with sr.Microphone() as source:
             print('listening...')
             voice = listener.listen(source)
             led = listener.recognize_google(voice)
             led = led.lower()
            if led == 'blue':
                    ser.write(b'2')
            elif led == 'red':
                    ser.write(b'4')
            elif led == 'yellow':
                    ser.write(b'6')
            elif led == 'all of them':
                    ser.write(b'7')
            elif led == 'police lights':
                    ser.write(b'A')
            else:
                    command=0
            talk('turning off' + led + ' led')


def main():
    print("Initializing Atena")
    wishMe()
    while True:
        
            takeCommand()
            
main()