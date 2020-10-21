import os				# these lines are imported libraries needed for the GUI
from tkinter import *
import tkinter.messagebox as tm
import datetime
import tkinter as tk

def start_running(self, root, LoginFrame, username, password):
    def dest():				# this function is destroying the widgets on the page for when the page is changed
        self.leftFrame.destroy()
        self.rightFrame.destroy()
        self.infoBox.destroy()
        self.lab6.destroy()
    def ret(event):			# this function is calling the dest function and and then loading the function main menu onto the page
        dest()
        from mainMENU import main_menu
        main_menu(self, root, LoginFrame, username, password)

        path, pathx = os.getcwd().split("\\"), ""                       # these lines find the file and put the data into variable info
        for i in path: pathx = pathx + i + "\\"
        pathx = pathx + "\\GUIdata\\var_stop.txt"
        file = open(pathx, "w")                                         # these lines change the value in the text file
        file.write("stop: True\n")
        file.close()
    
    self.leftFrame = Frame(self, height=650, width=600, bg="#e5c379")	    # these lines create the frames and labels for the page
    self.rightFrame = Frame(self, height=650, width=600, bg="#a3c7cc")
    self.lab6 = Label(self, text="Return", bg="#a3c7cc", borderwidth=3, relief="groove")
    self.lab6.config(font=("Courier", 20), width=35, height=1)
    self.infoBox = Label(self, height=10, width=100, bg="#ffffff")

    self.leftFrame.grid(row=0,column=0, rowspan=2)			    # these lines put them on the page
    self.rightFrame.grid(row=0, column=1, rowspan=2)
    self.lab6.grid(row=1, column=0, columnspan=2)
    self.infoBox.grid(row=0, column=0, columnspan=2)

    self.lab6.bind("<Button-1>", ret)					    # this line binds the return button to the ret function
#===============================================================================================
    path, pathx = os.getcwd().split("\\"), ""                       # these lines find the file and put the data into variable info
    for i in path: pathx = pathx + i + "\\"
    pathx = pathx + "\\GUIdata\\var_stop.txt"
    file = open(pathx, "w")                                         # these lines change the value in the text file
    file.write("stop: False\n")
    file.close()
#===============================================================================================
    running = True
    path, pathx = os.getcwd().split("\\"), ""                       # these lines find the path to the file containing the code
    path.pop()
    for i in path: pathx = pathx + i + "\\"
    pathy = pathx + "\\crypto_modules\\data_handler.py"
    import importlib.util
    spec = importlib.util.spec_from_file_location("data_handler", pathy)     # these lines open the module
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    foo.dataHandler(running, root, LoginFrame, start_running, username)
    
