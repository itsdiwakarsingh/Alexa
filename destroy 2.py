# Repeat me, virtual friend
"""import pyttsx3

friend = pyttsx3.init()
speech = input("say someting")
friend.say(speech)
friend.runAndWait()


# its gonna auto message I Love U
import pyautogui

while True:
    pyautogui.sleep(3)
    pyautogui.typewrite('I Love u')
    pyautogui.sleep(3)
    pyautogui.press('enter')



# auto mouse move, zoom active all time
import pyautogui

pyautogui.FAILSAFE = False
while True:
    pyautogui.sleep(10)
    for i in range(0, 100):
        pyautogui.moveTo(300, 300)
    for i in range(0, 3):
        pyautogui.press('shift')



# dino game i have to make "it auto open and play game with pyautogy"
chrome://dino/

Runner.instance_.gameOver = () => {}



# Screen recoder + video recoder

import datetime
import time

import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capture_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
webcam = cv2.VideoCapture(0)
fps = 120
prev = 0

while True:
    time_elapsed = time.time() - prev
    img = pyautogui.screenshot()
    if time_elapsed > 1.0/fps:
        prev = time.time()
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        _, frame = webcam.read()
        fr_height, fr_width, _ = frame.shape
        img_final[0: fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :]
        cv2.imshow('Screen_recoder', img_final)
        # cv2.imshow(' Webacam', frame)
        capture_video.write(img_final)
        if cv2.waitKey(10) == ord('q'):
            break
"""

# selfie camera auto

""""
#  make >>>>>>>dougnut

# from vpython import *
# ring()


canvas(background= color.purple)
donut = ring(radius=0.5, thickness=0.25, color=vector(400, 100, 1))
chocolate = ring(radius=0.55, thickness=0.25, color=vector(0.4, 0.2, 0))
rad = 0
while True:
    rate(10)
    donut.pos = vector(3*cos(rad), sin(rad), 0)
    chocolate.pos = vector(3*cos(rad), sin(rad), 0)
    rad = rad + 0.03
"""

"""
# [phone number address + location
import phonenumbers
from phonenumbers import timezone

# Program to convert input to
# phonenumber format

import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder

gb_numbert = phonenumbers.parse("+917258049010", "en")
timezone.time_zones_for_number(gb_numbert)
print(gb_numbert)
phoneNumber = phonenumbers.parse("+917258049010")
timeZone = timezone.time_zones_for_number(gb_numbert)
print(timeZone)

geocoder.description_for_number(gb_numbert, "en")
print(geocoder.description_for_number(gb_numbert, "en"))
"""


"""
 # translate after me reapeat : google translater talk wala
import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'en'
output_lang = 'ja'
try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass

translated = translator.translate(text, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('romantic.mp3')
playsound.playsound('romantic.mp3')
# print(googletrans.LANGUAGES)
"""

"""
# to check harry voice name of google .....

import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    pass
"""

"""
 #weather not working ' https://www.youtube.com/watch?v=Sz0_2fp27Q0&t=226s '

import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "ara&appid=eb0e69fba7a0d8170f7af00ad6576ab7"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()


# code  no working 
 
"""
"""
import geocoder
import folium

g = geocoder.ip("me")
myAddress = g.latlng
print(myAddress)
my_map1 = folium.Map(location=myAddress,
                     zoom_start=12)
folium.CircleMarker(location=myAddress,
                    radius=50, popup="yorkshire").add_to(my_map1)
folium.Marker(myAddress,
              popup="yorkshire").add_to(my_map1)
my_map1.save("my_map.html")

"""
import pyautogui as pg
import time

time.sleep(10)
for i in range(100):
    pg.write('I am bored what should i do')
    pg.press('Enter')
