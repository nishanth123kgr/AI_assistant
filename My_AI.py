import ctypes
import datetime
import json
import os  # to save/open files
import shutil
import smtplib
import subprocess
import time
import webbrowser
from urllib.request import urlopen

# from pygame import mixer
import playsound  # to play saved mp3 file
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr  # importing speech recognition package from google api
import wikipedia
import winshell
import wolframalpha  # to calculate strings into formula, its a website which provides api, 100 times per day
from clint.textui import progress
from gtts import gTTS  # google text to speech
from twilio.rest import Client

num = 1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    global num
    num += 1
    print("JaRVis : ", audio)
    tospeak = gTTS(text=audio, lang='en-US', slow=False)
    file = str(num) + ".mp3"
    tospeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = "JaRVis 1.0"
    speak("I am your Assistant " + assname)


def get_audio():
    r = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source, phrase_time_limit=5)
    print("Recognizing....")

    try:
        text = r.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text

    except Exception as e:
        print(e)
        speak("I was unable to recognize your voice. Please try again")
        return ""


def usrname():
    speak("What should I call you sir?")
    uname = get_audio()

    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print(("Welcome " + uname).center(columns))
    print("#####################".center(columns))
    speak("Welcome " + uname)

    speak("How can i Help you, Sir")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('nishanth123kgr@gmail.com', 'nishanth123')
    server.sendmail('nishanth123kgr@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    usrname()

while True:

    query = get_audio().lower()

    # All the commands said by user will be
    # stored here in 'query' and will be
    # converted to lower case for easily
    # recognition of command
    if 'wikipedia' in query:
        try:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)
        except:
            speak("Sorry, there are no results about " + query)


    elif 'open youtube' in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
        time.sleep(5)

    elif 'open google' in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")
        time.sleep(5)

    elif 'open stackoverflow' in query:
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")
        time.sleep(5)

    elif 'play music' in query or "play song" in query:
        speak("Here you go with music")
        # music_dir = "G:\\Song"
        music_dir = "D:\\Songs"
        songs = os.listdir(music_dir)
        print(songs)
        random = os.startfile(os.path.join(music_dir, songs[1]))
        time.sleep(5)

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

    elif 'open opera' in query:
        codePath = r"C:\\Users\\Nishanth\\AppData\\Local\\Programs\\Opera\\launcher.exe"
        os.startfile(codePath)

    elif 'email to Nishanth' in query:
        try:
            speak("What should I say?")
            content = get_audio()
            to = "nishanth123kgr@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif 'ask' in query:
        speak('I can answer to computational and geographical questions and what question do you want to ask now')
        question = get_audio()
        app_id = "R2K75H-7ELALHR35X"
        client = wolframalpha.Client('R2K75H-7ELALHR35X')
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)



    elif 'send a mail' in query:
        try:
            speak("What should I say?")
            content = get_audio()
            speak("whome should i send")
            to = input()
            sendEmail(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif 'how are you' in query:

        speak("I am fine, Thank you")
        speak("How are you, Sir")
        query = get_audio().lower()
        if 'fine' in query or "good" in query:
            speak("It's good to know that your fine")


    elif "what's your name" in query or "what is your name" in query:

        speak("My friends call me, JaRVis 1.0")


    elif 'exit' in query or "bye" in query or "see you later" in query:

        speak("Thanks for giving me your time")
        exit()

    elif "who made you" in query or "who created you" in query:

        speak("I have been created by Nishanth.")

    elif 'joke' in query:
        a = pyjokes.get_joke()

        speak(a)

    elif "calculate" in query:

        app_id = "E46YXW-T5LG6RT7K7"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text

        speak("The answer is " + answer)

    elif 'search' in query or 'play' in query:

        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)

    elif "who i am" in query:
        speak("If you talk then definately your human.")

    elif "why you came to world" in query:
        speak("Thanks to Nishanth. further It's a secret")

    elif 'power point presentation' in query:
        speak("opening Power Point presentation")
        power = r"C:\\Users\\Nishanth\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
        os.startfile(power)

    elif 'is love' in query:
        speak("It is 7th sense that destroy all other senses")

    elif "who are you" in query:
        speak("I am your virtual assistant created by Nishanth")

    elif 'reason for you' in query:
        speak("I was created as a Minor project by Mister Nishanth ")

    elif 'change background' in query:
        ctypes.windll.user32.SystemParametersInfoW(20,
                                                   0,
                                                   "Location of wallpaper",
                                                   0)
        speak("Background changed succesfully")

    elif 'open bluestack' in query:
        appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
        os.startfile(appli)

    elif 'news' in query:

        try:
            jsonObj = urlopen(
                '''http://newsapi.org/v2/top-headlines?country=in&apiKey=c3838ec820db42f0804b9c9d0c447f36''')
            data = json.load(jsonObj)
            i = 1

            speak('here are some top news from the times of india')
            print('''=============== TIMES OF INDIA ===============''' + '\n')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1


        except Exception as e:

            print(str(e))


    elif 'lock window' in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in query:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin Recycled")

    elif "don't listen" in query or "stop listening" in query:
        speak("for how much time you want to stop jarvis from listening commands")
        a = int(get_audio())
        time.sleep(a)
        print(a)

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("User asked to Locate " + location)
        webbrowser.open("https://www.google.nl / maps / place/" + location + "")



    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query or "sleep" in query:
        speak("Hibernating")
        subprocess.call("shutdown / h")

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif "write a note" in query:
        speak("What should i write, sir")
        note = get_audio()
        file = open('jarvis.txt', 'w')
        speak("Sir, Should i include date and time")
        snfm = get_audio()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            file.write(float(strTime))
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)

    elif "show note" in query:
        speak("Showing Notes")
        file = open("jarvis.txt", "r")
        print(file.read())


    elif "update assistant" in query:
        speak("After downloading file please replace this file with the downloaded one")
        url = '# url after uploading file'
        r = requests.get(url, stream=True)

        with open("Voice.py", "wb") as Pypdf:

            total_length = int(r.headers.get('content-length'))

            for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                   expected_size=(total_length / 1024) + 1):
                if ch:
                    Pypdf.write(ch)

            # NPPR9-FWDCX-D2C8J-H872K-2YT43
    elif "jarvis" in query:

        wishMe()
        speak("Jarvis 1.0 in your service Mister")


    elif "weather" in query:
        api_key = "8ef61edcf1c576d65d836254e11ea420"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        speak("whats the city name")
        city_name = get_audio()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in kelvin unit is " +
                  str(current_temperature) +
                  "\n humidity in percentage is " +
                  str(current_humidiy) +
                  "\n description  " +
                  str(weather_description))
            print(" Temperature in kelvin unit = " +
                  str(current_temperature) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))

        else:
            speak(" City Not Found ")

    elif "send message " in query:
        # You need to create an account on Twilio to use this service
        account_sid = 'Account Sid key'
        auth_token = 'Auth token'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=get_audio(),
            from_='Sender No',
            to='Receiver No'
        )

        print(message.sid)

    elif "wikipedia" in query:
        webbrowser.open("wikipedia.com")

    elif "Good Morning" in query:
        speak("A warm" + query)
        speak("How are you Mister")


    # most asked question from google Assistant
    elif "will you be my gf" in query or "will you be my bf" in query:
        speak("I'm not sure about, may be you should give me some time")

    elif "how are you" in query:
        speak("I'm fine, glad you me that")

    elif "i love you" in query:
        speak("It's hard to understand")

    elif "what is" in query or "who is" in query:

        # Use the same API key
        # that we have generated earlier
        client = wolframalpha.Client("API_ID")
        res = client.query(query)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print("No results")

        # elif "" in query:

    # Command go here
    # For adding more commands
