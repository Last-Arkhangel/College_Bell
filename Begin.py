import sys

import tkinter as tk
from tkinter import filedialog
from tkinter import *   ## notice lowercase 't' in tkinter here

import time
import os

from playsound    import playsound
from PIL 		  import Image
from time 		  import gmtime, strftime, localtime, strptime

from pystray import MenuItem
import pystray

from Socket_Singleton import Socket_Singleton

# ================ SETUP ====================

fields = ['Пара 1:' , 'Пара 2:', 'Пара 3:', 'Пара 4:' , 'Пара 5:']
len(fields)

global times_bell, times_bell_sec

# === Times for bell ===
times_bell = ['07:55:00','08:00:00','09:20:00', '09:25:00', '09:30:00', '10:50:00', '11:05:00', '11:10:00', '12:30:00', 
			  '12:35:00', '12:40:00', '14:00:00', '14:05:00', '14:10:00', '15:30:00']

#times_bell-70 = ['07:55:00','08:00:00','09:10:00', '09:15:00', '09:20:00', '10:30:00', '10:45:00', '10:50:00', '12:00:00', 
#			  '12:05:00', '12:10:00', '13:20:00', '13:25:00', '13:30:00', '14:40:00']
              
#times_bell-60 = ['07:55:00','08:00:00','09:00:00', '09:05:00', '09:10:00', '10:10:00', '10:25:00', '10:30:00', '11:30:00', 
#			  '11:35:00', '11:40:00', '12:40:00', '12:45:00', '12:50:00', '13:50:00']

	# Make array with bell times in seconds
times_bell_sec=[]

for i in range(0, len(times_bell)):
	bell_time = time.strptime(times_bell[i],'%H:%M:%S')
	times_bell_sec.append(bell_time.tm_hour * 3600 + bell_time.tm_min * 60 + bell_time.tm_sec)

# === Music setup ===
global default_music 
default_music = os.getcwd() + '\sound3.mp3'

# === BUTTON FUNCTIONS ===

# Button play music again
def playagain():
	playsound(default_music)

# === FUNCTIONS ===

def time2sec(time_arg):
	timeis = time.strptime(time_arg,'%H:%M:%S')
	timeinsec = timeis.tm_hour * 3600 + timeis.tm_min * 60 + timeis.tm_sec
	return timeinsec

# === Clock function + play music
def tick():
    global time1
    global default_music
    global times_bell, times_bell_sec
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        lable_clock.config(text=time2)
        # calls itself every 200 milliseconds
		# to update the time display as needed
		# could use >200 ms, but display gets jerky
    lable_clock.after(200, tick)
	
	# === Timer
    localtime = time.localtime()
    localtime_sec = time2sec("{0}:{1}:{2}".format(localtime.tm_hour, localtime.tm_min, localtime.tm_sec))

    if (localtime_sec < times_bell_sec[0]) or (localtime_sec > times_bell_sec[-1]):
    	lable_belltime.config(text = "ЗАНЯТТЯ ЗАКІНЧИЛИСЯ!!!", font=("Ubuntu", 16))
    else:
    	for i in range(0, len(times_bell_sec)-1):
    		if (localtime_sec >= times_bell_sec[i]) and (localtime_sec <= times_bell_sec[i+1]):
    			sec = times_bell_sec[i+1] - localtime_sec
    			s = sec % 60
    			m = int(sec / 60)
    			lable_belltime.config(text = "{0}:{1}".format(m, s) )

    # === MUSIC PLAY
    for i in range(0, len(times_bell)):
    	if (time2 == times_bell[i]) or (time2 == times_bell[i]) or (time2 == times_bell[i]):
    		playsound(default_music)
# === END of Clock function

# Open file 
def file_open():
	global default_music
	default_music = filedialog.askopenfilename()
	entry_file.insert(END, default_music)

def quit_win():
	window.destroy()

def quit_window(icon):
	icon.stop()
	window.destroy()

def show_window(icon):
	icon.stop()
	window.after(0, window.deiconify())

def hide_window():
	window.withdraw()
	image = Image.open('bell.ico')
	menu = (MenuItem('Розгорнути', show_window), MenuItem('Вихід', quit_window))
	icon = pystray.Icon("Дзвінки пар", image, 'Дзвінки пар (коледж) v.2.0', menu)
	icon.run()


if __name__ == '__main__':

	#global default_music # directory of music file

	# === Window ===
	window = tk.Tk()
	window.title('Дзвінки пар - 80 хвилин. v 2.0')
	window.iconbitmap("bell.ico")
	window.resizable(0, 0)
	window.geometry('780x280')

	time1 = ''
	
	# === Labels ===
		# Make labels with lesson numbers
	for i in range(0, len(fields)):
		Label(window, text=fields[i], padx=5, pady=5, font=("Ubuntu", 14)).grid(row=i+1)
	
		# Make lessons time labels
	count = 0	
	for i in range(0, len(times_bell), 3):
		Label(window, text=times_bell[i][0:5]    , background="lightblue", width = 10, font=("Ubuntu", 14)).grid(row=count+1, column=1)
		Label(window, text=times_bell[i+1][0:5]  , background="lightblue", width = 10, font=("Ubuntu", 14)).grid(row=count+1, column=2)
		Label(window, text=times_bell[i+2][0:5]  , background="lightblue", width = 10, font=("Ubuntu", 14)).grid(row=count+1, column=3)
		count += 1
		
		# Make lables with Begin and End word
	Label(window, text="Попередній:", padx=5, font=("Ubuntu", 14)).grid(row=0, column=1)
	Label(window, text="Початок пари:", padx=5, font=("Ubuntu", 14)).grid(row=0, column=2)
	Label(window, text="Кінець пари:", padx=5, font=("Ubuntu", 14)).grid(row=0, column=3)


		# Make label for Time now	
	Label(window, text="КОТРА ГОДИНА:", font=("Ubuntu", 16)).grid(row=0, column=5)
	lable_clock = Label(window, background="#F23A3A", font=("Ubuntu", 16))
	lable_clock.grid(row=1, column=5)

	
	Label(window, text = "ДЗВІНОК ЧЕРЕЗ:", width = 23, font=("Ubuntu", 16)).grid(row=3, column=5)
	lable_belltime = Label(window, background="#F23A3A")
	lable_belltime.grid(row=4, column=5)
	lable_belltime.config(text = "???", font=("Ubuntu", 16))

	tick()

	# === FILE buttons + entry + play again
	button_file = Button(window, text = "Файл...", padx=5, font=("Ubuntu", 14), command = file_open).grid(row=7, column=0)

	entry_file = Entry(window, font=("Ubuntu", 14))
	entry_file.grid(row=7, column=1, columnspan=2)
	entry_file.insert(END, default_music)

	tk.Button(window, text = "Дзвонити...", font=("Ubuntu", 14), command = playagain).grid(row=7, column=3)

	Label(window, text="    ", font=("Ubuntu", 10)).grid(row=6, column=4)
	Label(window, text="© 2022, Last-Arkhangel", font=("Ubuntu", 10)).grid(row=7, column=5, sticky="ws")

	tk.Button(window, text = "Вихід", font=("Ubuntu", 10), command = quit_win).grid(row=7, column=5, sticky="es")
	
	Socket_Singleton()
	window.protocol('WM_DELETE_WINDOW', hide_window)
	window.mainloop()

