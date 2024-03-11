from tkinter import *    #tkinter is a kind of GUI library for python
from tkinter import ttk   
import requests


#API for weather Fetching here API will fetch the data and get placed in the given names

def get_data():

    city = city_nam.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+" &appid=f07fd47fea13085d2f05974b09f76de4").json()
    weather_lb1.config(text=data["weather"][0]["main"])
    descr_lb1.config(text=data["weather"][0]["description"])
    Temp_lb.config(text=str(int(data["main"]["temp"]-273.15))) #converting degree to celcius 
    press1_lb.config(text=data["main"]["pressure"])
    

windows = Tk()
windows.title("Weather Forcast")
windows.config(bg= "Light blue") #background color
windows.geometry("500x500") #windows border


head_lb = Label(windows, text="Weather Forcasting App", font=("georgia", 17, "bold", "italic"))
head_lb.place(x = 25, y = 50, height= 50, width= 440) #for placement of the text in the placeholder.


#combo box for city list 

city_nam = StringVar()

city_list = ["Kathmandu", "Pokhara", "Baglung","Bharatpur", "London"]
combobox = ttk.Combobox(windows, text="Weather Forcasting App", font=("Time New Roman", 17, "bold"), textvariable=city_nam)
combobox['values'] = city_list
combobox.place(x = 25, y = 120, height= 40, width= 440)


#Weather placeholder column

weather_lb = Label(windows, text="Weather Pattern: ", font=("Time New Roman", 10, "bold"), fg="#FC8955")
weather_lb.place(x = 25, y = 260, height= 35, width= 145) #for placement of the text in the placeholder.

#For RHS portion
weather_lb1 = Label(windows, text=" ", font=("Time New Roman", 10, "bold"), fg="#FC8955")
weather_lb1.place(x = 250, y = 260, height= 35, width= 145) #for placement of the text in the placeholder.



#Weather Description placeholder

descr_lb = Label(windows, text="Weather Description: ", font=("Time New Roman", 10, "bold"), fg="#FC8955")
descr_lb.place(x = 25, y = 315, height= 35, width= 145) #for placement of the text in the placeholder.

descr_lb1 = Label(windows, text=" ", font=("Time New Roman", 10, "bold"), fg="#FC8955")
descr_lb1.place(x = 250, y = 315, height= 35, width= 145) #for placement of the text in the placeholder.


#Temperature Placeholder

Temp_lb = Label(windows, text="Current Temperature: ", font=("Time New Roman", 10, "bold"), fg="#FC8955")
Temp_lb.place(x = 25, y = 370, height= 35, width= 145) #for placement of the text in the placeholder.

Temp_lb = Label(windows, text=" ", font=("Time New Roman", 10, "bold"), fg="#FC8955")
Temp_lb.place(x = 250, y = 370, height= 35, width= 145) #for placement of the text in the placeholder.

#Pressure Placeholder
press_lb = Label(windows, text="Current Pressure: ", font=("Time New Roman", 10, "bold"), fg="#FC8955")
press_lb.place(x = 25, y = 425, height= 35, width= 145) #for placement of the text in the placeholder.

press1_lb = Label(windows, text=" ", font=("Time New Roman", 10, "bold"), fg="#FC8955")
press1_lb.place(x = 250, y = 425, height= 35, width= 145) #for placement of the text in the placeholder.


#Search button

search_btn = Button(windows, text="Search", font= ("Time New Roman", 17, "bold"), command=get_data)
search_btn.place( x = 200, y = 190, height= 50, width= "100")



windows.mainloop() #to run the windows continuously with the help of main loop function
