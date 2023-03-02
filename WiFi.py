from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from subprocess import PIPE, Popen
import os
import sys

container = Tk()


def about():
        #About
        messagebox.showinfo("About", "This software is coded by Vyankatesh Pipalwa")


def how():
        #How to
        messagebox.showinfo("How to use","Just open Wi-Fi Extractor and press Extract that's it.")


def compatibility():
        #Compatibility
        messagebox.showinfo("Compatibility","This software is compatible with all Windows operating systems.")


def done():
        #Done message
        messagebox.showinfo("Done","Wi-Fi Passwords Extracted!")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def extract():
        #Extract process
        command = 'netsh wlan show profiles | find "All User Profile"'
        with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
         output = process.communicate()[0].decode("utf-8")
         ou=output.replace("    All User Profile     : ","")
         lst1 = [item for item in ou.split("\r\n")]
         for lists in lst1:
                        print(lists)
                        os.system(f'netsh wlan show profiles name="{lists}" key=clear | find "Key Content"')
                        print("---------------------------------------------")
         done()


#Title
container.title("Wi-Fi Extractor")
#Width X Height
container.geometry("285x190")
#Background color
container.config(bg="DarkGoldenrod2")
#Icon
iconPath = resource_path("logoV2.ico")
container.iconbitmap(iconPath)


#Label
wifiLabel=Label(container, text='Wi-Fi Password Extractor', bg="yellow2", font=("Helvetica", "10", "bold"))
wifiLabel.grid(row=1, column=1, padx=60, pady=40)
# Button
generateButton = Button(container, text='Extract', width=10, command=extract, activebackground='IndianRed1', bg="OrangeRed2")
generateButton.grid(row=2, column=1, padx=30, pady=5)


# Menu
menu = Menu(container)
container.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=container.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Compatibility', command=compatibility)
helpmenu.add_command(label='How', command=how)
helpmenu.add_command(label='About', command=about)
container.mainloop()
