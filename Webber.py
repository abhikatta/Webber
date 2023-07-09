import webbrowser
import speech_recognition as sr
import pyttsx3
from infi.systray import SysTrayIcon

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(engine, text: str):
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def take_command(statement):
    others = {'shutdown'}
    if statement not in others:
        webbrowser.open(statement)
    else:
        import os
        os.system('shutdown /s')


calls = {'hey webber', 'webber'}
listening = False

if __name__ == '__main__':
    sysTrayIcon = SysTrayIcon("Webber.ico", "Webber", '')
    sysTrayIcon.start()
    r = sr.Recognizer()
    FIRST_CALL = False
    while True:
        # if KeyboardInterrupt or exit:
        #     exit()

        with sr.Microphone() as source:
            if not listening:
                if not FIRST_CALL:
                    print("Loading modules...\n")
                    audio = r.listen(source)
                    print("Modules Loaded\n")
                    FIRST_CALL = True

                # statement = r.recognize_google(audio, language='en-in')

                statement = str(input("Not yet listening"))
                print('statement taken')
                if statement in calls:
                    listening = True
                    speak(engine, 'Whazz up?')
            else:

                try:
                    # statement = r.recognize_google(audio, language='en-in')
                    statement = str(input('listening...'))
                    take_command(statement=statement)
                    listening = False
                except sr.UnknownValueError:
                    speak(engine, "Pardon me, please say that again.")
                except sr.RequestError:
                    speak(
                        engine, "Sorry, I am currently unable to process your request. Please try again.")
