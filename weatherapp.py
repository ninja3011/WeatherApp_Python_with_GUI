#A python gui project using Python Tkinter
#Written By Ninad Sunil Jangle at 8:59 pm 15/08/2020
#documentation referred: https://www.tutorialspoint.com/python/tk_pack.htm
#tutorial referred Keith Galli: https://www.youtube.com/watch?v=D8-snVfekto

#This Program handles the gui look and operations, api calls and icon assignment.

#importing the gui lib
#named it tk so can use tk.funcname()
import tkinter as tk
#importing the font lib to give font-type
from tkinter import font
#ImageTk will be used for the icon generation
from PIL import Image, ImageTk
#requests is required when dealing with APIs
import requests

#naming the window gui
root = tk.Tk()

#parameters of the gui screen
HEIGHT = 500
WIDTH = 600

#func() takes in weater JSON and returns the multiline concatenated name,desc,and temp of the place
#If Invalid entry is made by user, It will return an error. 
#Due to the use of try except exception handling, the app wont crash

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

#func() takes the input city provided and gets the weather JSON from api
def get_weather(city):
	weather_key = 'ed90c739b76f6d08c8a794d81e81eb72'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	print(weather)
	label['text'] = format_response(response.json()) #calls format_response()
	icon_name = weather['weather'][0]['icon']
	open_image(icon_name) #calls open_image()

#func() takes in the appropriate icon name and addsit to the obj: weather_icon
def open_image(icon):
        size = int(lower_frame.winfo_height()*0.25)
        img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
        weather_icon.delete("all") #removes any previous associated icon
        weather_icon.create_image(0,0, anchor='nw', image=img) #sets the img
        weather_icon.image = img #attaches image to obj
        
#creating a container for the background image    
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)


background_image = tk.PhotoImage(file='clouds.png') #getting the bg image
background_label = tk.Label(root, image=background_image) #adding it to the label
background_label.place(relwidth=1, relheight=1) #adding it to the gui
canvas.pack() #adding it to the gui

frame = tk.Frame(root, bg='#80c1ff', bd=5) #creating a container for entry and submit button
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') #anchor gives fix dir

entry = tk.Entry(frame, font=('Courier',12)) #adding a Textbox to frame container
entry.place(relwidth=0.65, relheight=1) #adding to gui

button = tk.Button(frame, text="Get Weather", font=('Courier',12), command=lambda: get_weather(entry.get())) #adding to frame container and calling get_weather()
button.place(relx=0.7, relheight=1, relwidth=0.3) #adding to gui

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10) #creating a container for result label
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n') #adding to gui

label = tk.Label(lower_frame,anchor='nw',justify='left',bd=4) #adding to lower_frame container
label.config(font=('Courier',18),bg='white') #setting some formatting
label.place(relwidth=1, relheight=1) #adding to gui

weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0) #adding to label , no border, no thickness, bg is white
weather_icon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5) 

root.mainloop() #restart the loop from root
