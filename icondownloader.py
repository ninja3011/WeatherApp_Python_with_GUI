#A python gui project using Python Tkinter
#Written By Ninad Sunil Jangle at 8:59 pm 15/08/2020
#documentation referred: https://www.tutorialspoint.com/python/tk_pack.htm
#tutorial referred Keith Galli: https://www.youtube.com/watch?v=D8-snVfekto

#This program will download the icons used by the api call to describe weather

import os             #used for checking local directories
import urllib.request # for retrieving images from the api

day = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13n.png', '50d.png'] #day icon names
night = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png'] #night icon names

base_url = 'https://openweathermap.org/img/w/' #url to get icons
img_dir = './img/' #created directory name
if not os.path.exists(img_dir): #if img dir doesnot exist already, it creates one. Double creation might cause issues of ambiguity. Hence a check is imp
	os.makedirs(img_dir)

# Get the day weather icons
for name in day: #loop through all day icons
	file_name = img_dir+name #setting file name to img/<icon_name>
	if not os.path.exists(file_name): #if img path doesnot exist already, it creates one. Double creation might cause issues of ambiguity. Hence a check is imp
		urllib.request.urlretrieve(base_url+name, file_name) #calling the url api to retrive images

# Repeat the same thing for night weather icons
for name in night: #loop through all night icons
	file_name = img_dir+name #setting file name to img/<icon_name>
	if not os.path.exists(file_name): #if img path doesnot exist already, it creates one. Double creation might cause issues of ambiguity. Hence a check is imp
		urllib.request.urlretrieve(base_url+name, file_name)  #calling the url api to retrive images
