import webbrowser,speech_recognition as sr,pyttsx3
from infi.systray import SysTrayIcon

def take_command( SysTrayIcon):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    def speak(engine,text:str):
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak(engine=engine,text='Hi.')
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            speak(engine=engine,text=f'You said: {statement}')
            webbrowser.open(statement)
        except sr.UnknownValueError:
            speak(engine=engine,text="Pardon me, Please say that again.")
            statement = r.recognize_google(audio, language='en-in')
            speak(engine=engine,text=f'You said: {statement}')
            webbrowser.open(statement)
        except sr.RequestError:
            speak(engine=engine,text="Sorry, I am currently unable to process your request. Please try again.")

    
menu_options = ((("Take Command"),None,take_command),)
sysTrayIcon = SysTrayIcon("boticon.ico", "Bot",menu_options)
sysTrayIcon.start()
