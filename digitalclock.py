from tkinter import *// importing the necessary library 
from time import *

def update():


    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    time_string = strftime("%I:%M:%S%p")
    time_label.config(text=time_string)

    

    window.after(1000, update)

window = Tk()

window.minsize(450,450)
window.title("Digital Clock")
window.config(bg="#A8DF8E")
window.geometry("350x350")

day_label = Label(window, font=("Arial", 25), bg= "#A8DF8E")
day_label.pack()

date_label = Label(window, font=("Ink Free", 30), bg= "#A8DF8E" )
date_label.pack()



time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

Text_labels = Label(window, font=("Arial", 50), text="                                            ", bg= "#A8DF8E")
Text_labels.pack()

Text_label = Label(window, font=("Arial", 10), text="Made by FT.", bg= "#A8DF8E" )
Text_label.pack()




update()

window.mainloop()
