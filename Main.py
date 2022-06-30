import speech_recognition as sr
import pyttsx3
import pywhatkit
import rotatescreen
import datetime
import wikipedia
import pyjokes
import webbrowser
import sys
import subprocess
import cv2
import winsound
import PyPDF2
import pyautogui

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def repeate(repeater):
    engine.say(repeater)
    engine.say('any  thing  else  boss')
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('say= ok google')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'google' in command:
                command = command.replace('ok google', '')
                print(command)
    except:
        pass
    return command


def run_google():
    global hi, file, files, apps, gone
    command = take_command()
    print(command)
    if 'diwakar' in command:
        song = command.replace('play', '')
        talk('playing the song which you have decided,' + song)
        print('playing the song which you have decided,' + song)
        pywhatkit.playonyt(song)
        gone = subprocess.Popen('F:\\Riot Games\\Riot Client\\RiotClientServices.exe')
        apps = subprocess.Popen('C:\\Users\\ritao\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe')
        files = subprocess.Popen('C:\\Users\\ritao\\AppData\\Roaming\\Spotify\\Spotify.exe')
        hi = subprocess.Popen('C:\\Users\\ritao\\AppData\\Local\\Programs\\Notion\\Notion.exe')
        file = subprocess.Popen('C:\\Users\\ritao\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing the song which you have decided,' + song)
        print('playing the song which you have decided,' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %S %p')
        print(time)
        talk('current time is ' + time)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print()
    elif 'repeat after me' in command:
        command = command.replace('repeat after me', '')
        engine.say(command)
        engine.runAndWait()
        print(command)
    elif 'sanskar' in command:
        talk('sanskar   is    good   boy')
        print('sanskar is good boy')
    elif 'piyush' in command:
        talk('mota  have  big      thick      ass ')
        print('mota is good boy')
    elif 'himanshu' in command:
        talk('who   is      ')
        print('who is ')
    elif 'send message to sanskar' in command:
        pywhatkit.sendwhatmsg("+91 73709 09034", "Hi", 10, 31, 15, True, 2)
    elif 'kids' in command:
        talk(' Baka,  baka,  baka,  baka kids')
        print('Baka,Baka,Baka,Baka kids')

    elif 'no' in command:
        talk('have  a    nice    day, ️ sir')
        print('Have a nice day,😁 Sir')
        sys.exit(123)
    elif 'sleep' in command:
        talk('have  a    nice    day, ️ sir')
        print('Have a nice day,😐 Sir')
        sys.exit(123)
    elif 'open spotify' in command:
        files = subprocess.Popen('C:\\Users\\ritao\\AppData\\Roaming\\Spotify\\Spotify.exe')
        talk('opening Spotify')
    elif 'close spotify' in command:
        files.terminate()
    elif 'solve' in command:
        screen = rotatescreen.get_primary_display()
        screen.rotate_to(0)
    elif 'play game' in command:
        screen = rotatescreen.get_primary_display()
        for i in range(49):
            import time
            time.sleep(1)
            screen.rotate_to(i * 90 % 360)
    elif 'open notion' in command:
        hi = subprocess.Popen('C:\\Users\\ritao\\AppData\\Local\\Programs\\Notion\\Notion.exe')
        talk('opening Notion')
    elif 'close notion' in command:
        hi.terminate()
    elif 'open discord' in command:
        apps = subprocess.Popen('C:\\Users\\ritao\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe')
        talk('opening Discord')
    elif 'close discord' in command:
        apps.terminate()
    elif 'open whatsapp' in command:
        file = subprocess.Popen('C:\\Users\\ritao\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
        talk('opening whatsapp')
    elif 'close whatsapp' in command:
        file.terminate()
    elif 'open game' in command:
        gone = subprocess.Popen('F:\\Riot Games\\Riot Client\\RiotClientServices.exe')
        talk('opening Riot client')
    elif 'close game' in command:
        gone.terminate()
    elif 'game' in command:
        pyautogui.click(755, 1055)
        pyautogui.typewrite('ri')
        pyautogui.typewrite(["enter"])
        pyautogui.sleep(7)
        pyautogui.click(323, 341)
        pyautogui.click(1018, 876)
        pyautogui.sleep(1)
        pyautogui.click(272, 982)
        pyautogui.sleep(1)
        pyautogui.click(949, 764)
    elif 'fun' in command:
        import time
        pyautogui.click(755, 1055)
        pyautogui.typewrite('chrome')
        pyautogui.typewrite(["enter"])
        time.sleep(1)
        pyautogui.hotkey("ctrl", "shift", "n")
        time.sleep(1)
        pyautogui.typewrite('https://allporncomic.com/porncomic-genre/hentai/')
        time.sleep(2)
        pyautogui.typewrite(["enter"])
        pyautogui.typewrite(["enter"])
        time.sleep(5)
        pyautogui.scroll(-500)
        time.sleep(1)
        pyautogui.scroll(-500)
        # https://allporncomic.com/porncomic-genre/hentai/
    elif 'read' in command:
        book = open('The_Intelligent_Investor.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages

        speaker = pyttsx3.init()
        for num in range(7, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()
    elif 'open camera' in command:
        cam = cv2.VideoCapture(0)
        while cam.isOpened():
            ret, frame1 = cam.read()
            ret, frame2 = cam.read()
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
            for c in contours:
                if cv2.contourArea(c) < 5000:
                    continue
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
            if cv2.waitKey(10) == ord('q'):
                break
            cv2.imshow('Camera', frame1)
            continue
    elif 'close camera' in command:
        pyautogui.press('q')

    else:
        webbrowser.open('https://www.google.com/search?q=' + command)
        talk(webbrowser)
        print(webbrowser)


while True:
    run_google()
    repeate(repeate)
    run_google()
    repeate(repeate)
    run_google()
    repeate(repeate)
