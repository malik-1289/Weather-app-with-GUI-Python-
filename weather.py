from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

app=Tk()
app.title("WEATHER")
app.geometry("900x500+300+200")
app.resizable(False,False)

def getWeather():
    try:
        city = txtfld.get()

        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        if location is None:
            messagebox.showerror("Error", "City not found")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=e6c812e9df5bc8ba2eca8b2dc403827d"

        json_data = requests.get(api).json()
        cond = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(cond, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description.capitalize())
        p.config(text=pressure)
        
    except Exception as e:
        messagebox.showerror("Error: Invalid Entry!!!")

#searchbox
srch_img=PhotoImage(file="srch.png")
myimg=Label(image=srch_img)
myimg.place(x=20,y=20)

txtfld=tk.Entry(app,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
txtfld.place(x=50,y=40)
txtfld.focus()

srchicon=PhotoImage(file="srch_icon.png")
myimg_icon=Button(image=srchicon, borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimg_icon.place(x=400,y=34)

#logo
logo= PhotoImage(file="logo.png")
myimg_logo=Label(image=logo)
myimg_logo.place(x=150,y=100)

#bottom box
frameimg=PhotoImage(file="box.png")
myimg_frame=Label(image=frameimg)
myimg_frame.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(app,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(app,font=("Helvetica",20))
clock.place(x=30,y=130)

#label1 WIND
label1=Label(app, text="WIND",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label1.place(x=120,y=400)

#label2 HUMIDITY
label2=Label(app, text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label2.place(x=250,y=400)

#label3 DESCRIPTION
label3=Label(app, text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label3.place(x=430,y=400)

#label4 PRESSURE
label4=Label(app, text="PRESSURE",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=250,y=430)
d=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)
p=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=650,y=430)

app.mainloop()



