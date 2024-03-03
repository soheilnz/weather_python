import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?lat="+ city +"&appid={911021ec8b736d3097833c95ab2c825b}"
    json = requests.get(api).json()
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json["sys"]["sunrise"] - 21600))
    label1.config(text = json)
    label2.config(text=sunrise)



canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather appp")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady= 20)
textfield.focus()
textfield.bind("<Return>", getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()
