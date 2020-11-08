import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import os.path
import smtplib
import random
import win32gui
import win32con
import psutil
i = 0
while True:
    try:
        # tst

        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        print(voices[0].id)
        engine.setProperty('voice', voices[0].id)

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()

        def chrome_webbrowser(chrome_path, url):
            webbrowser.get(chrome_path).open(url)

        def wishme():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak('Good Morning Vicky')
            elif hour >= 12 and hour >= 17:
                speak('Good Afternoon Vicky')
            else:
                speak('Good Evening')
            print('My name is Jarvis, May I help you?')
            speak('My name is Jarvis, May I help you?')

        def takecommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening....')
                r.pause_threshold = 1

                audio = r.listen(source, timeout=1, phrase_time_limit=3)

            try:
                print('Recognizing....')
                querry = r.recognize_google(audio, language='en-in')
                print(f'You said {querry}')
            except Exception:
                print('Say That Again Please!')
                return 'None'
            return querry

        if __name__ == "__main__":
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            plugged = "Plugged In" if plugged else "Not Plugged In"
            # print("Battery is "+percent+'% | '+plugged)
            if int(percent)==100 and plugged=="Plugged In":
                print("Vicky, Please remove the charger your battery is fully charged")
                speak("Vicky, Please remove the charger your battery is fully charged")
                speak("Vicky, Please remove the charger your battery is fully charged")
                
            if i == 0:
                wishme()
                i = 1
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path)

            querry = takecommand().lower()
            if 'wikipedia' in querry:
                speak('Searching wikipedia...')
                querry = querry.replace('wikipedia', '')
                querry = querry.replace('please', '')

                results = wikipedia.summary(querry, sentences=2)
                speak('According to wikipedia, ')
                print(results)
                speak(results)
            elif "vscode" in querry or "vs code" in querry:
                speak("Vs code open to you Vicky")
                os.system("code .")
            elif 'who are you' in querry:
                print('I am Waqas Sir!')
                speak('I am Waqas Sir!')
            elif "open whatsapp" in querry or "open whats up" in querry or "open whats" in querry:
                speak("Whatsapp Open to you Mr Vicky")
                os.startfile(r"C:\Users\Muhammad Waqas\AppData\Local\WhatsApp\WhatsApp.exe")
            elif 'made you' in querry:
                print('I am made by you Sir Waqas powered by Vicky World Production')
                speak('I am made by you Sir Waqas powered by Vicky World Production')

            elif "sleep" in querry or "sleap" in querry:
                speak("We set your PC to sleeping mode")
                        # os.system("Powercfg -H OFF")
                os.system("rundll32.exe Powercfg -H OFF,SetSuspendState 0,1,0")

            elif 'open youtube' in querry:
                url = ('youtube.com')
                chrome_webbrowser(chrome_path, url)
                        # webbrowser.open('youtube.com')
                speak('Youtube has been opened dear Vicky')

            elif 'open google' in querry or 'open chrome' in querry:
                        # webbrowser.open('google.com')
                # url = ('google.com')
                url=""
                chrome_webbrowser(chrome_path, url)
                speak('Google Has been opened dear Vicky')

            elif 'stack overflow' in querry:
                        # webbrowser.open('stackoverflow.com')
                url = ('stackoverflow.com')
                chrome_webbrowser(chrome_path, url)

            elif 'stackoverflow' in querry:
                url = ('stackoverflow.com')
                chrome_webbrowser(chrome_path, url)
            elif 'the time' in querry:
                # str = datetime.datetime.now().strftime('%H:%M:%S')
                time_h = datetime.datetime.now().strftime('%H')
                time_m = datetime.datetime.now().strftime('%M')
                if int(time_h)>12:
                    time_h=int(time_h)-12
                    print(f"Time is {time_h} hours {time_m} minutes PM")
                    speak(f"Time is {time_h} hours {time_m} minutes PM")
                else:
                    print(f"Time is {time_h}:{time_m} AM")
                    speak(f"Time is {time_h} : {time_m} AM")
            elif 'search' in querry:
                querry = querry.replace('search','')
                querry = querry.replace('please','')
                chrome_webbrowser(chrome_path, querry)
            elif 'open song' in querry or 'open songs' in querry:


                music_dir = r'E:\D\New folder (2)'
                songs = os.listdir(music_dir)
                print(songs)
                files_len = len([name for name in os.listdir('.') if os.path.isfile(name)])
                print(files_len)
                r = random.randint(0, files_len-1)
                print(songs[r])
                os.startfile(os.path.join(music_dir, songs[r]))

            elif "shutdown computer" in querry or "shut down computer" in querry or "computer shut down" in querry or "computer shutdown" in querry:
                speak("Computer has been closed")
                os.system("shutdown /s /t 1")
            elif "computer shutdown" in querry or "computer shut down" in querry:
                    speak("Computer has been closed")
                    os.system("shutdown /s /t 1")

            elif "poweroff computer" in querry or "computer poweroff" in querry:
                speak("Computer has been closed")
                os.system("shutdown /s /t 1")
            elif "power off computer" in querry or "computer power off" in querry:
                speak("Computer has been closed")
                os.system("shutdown /s /t 1")
            elif "power of computer" in querry:
                speak("Computer has been closed")
                os.system("shutdown /s /t 1")
            elif "quit Computer" in querry:
                    speak("Computer has been power off")
                    os.system("shutdown /s /t 1")
            elif "restartcomputer" in querry:
                    speak("We restarting your PC")
                    os.system("shutdown /r /t 1")
            elif "restart computer" in querry:
                    speak("We restarting your PC")
                    os.system("shutdown /r /t 1")
            elif "rstart computer" in querry:
                speak("We restarting your PC")
                os.system("shutdown /r /t 1")
            elif "restart Computer" in querry:
                speak("We restarting your PC")
                os.system("shutdown /r /t 1")
            elif "sleep" in querry or "sleap" in querry:
                speak("We set your PC to sleeping mode or turn off your screen")
                win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
            elif "open screen" in querry or "openscreen" in querry:
                speak("Screen has been turn")
                win32gui.SendMessage(win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)
    except Exception as e:
        print(e)
