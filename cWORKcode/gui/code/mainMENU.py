import os					    # these lines are imported libraries needed for the GUI
from tkinter import *
import tkinter.messagebox as tm
import datetime
import tkinter as tk

from userPage import User_page_run		    # these lines are importing the functions from the other GUI modules
from guiOptions import gui_options
from encryptPage import encrypt_page
from databasePage import database_page
from developerPage import developer
from startRunningPage import start_running
from dataGraphs import data_graphs

def main_menu(self, root, LoginFrame, username, password):
#------------------------------------------------
    def dest():					    # this function is destroying the widgets on the page for when the page is changed
        self.lab.destroy()
        self.lab2.destroy()
        self.lab3.destroy()
        self.bp.destroy()
        self.bp2.destroy()
        self.bp3.destroy()
        self.bp4.destroy()
        self.bp5.destroy()
        self.bp6.destroy()
    def aiScreen(event): print ("AI screen")	    # these lines are creating functions that link the menu buttons to other pages in the GUI
    def dataGraphs(event):
        dest()
        data_graphs(self, root, LoginFrame, username, password)
    def StartRun(event):
        dest()
        start_running(self, root, LoginFrame, username, password)
    def CUC(event):
        dest()
        User_page_run(self, root, LoginFrame, username, password)
    def GUIset(event):
        dest()
        gui_options(self, root, LoginFrame, username, password)
    def ENC(event):
        dest()
        encrypt_page(self, root, LoginFrame, username, password)
    def dataBP(event):
        dest()
        database_page(self, root, LoginFrame, username, password)
    def DEVOP(event):
        path, pathx = os.getcwd().split("\\"), ""                       # these lines find the files opened and created later in the function
        for i in path: pathx = pathx + i + "\\"
        pathy = pathx + "\\userInfo\\" + username
        pathz = pathy + ("\\" + username + "Info.txt")
        file = open(pathz, "r")
        for line in file:
            if "admin: " in line: admin = line[7:-1]
        file.close()
        if admin == "True":
            dest()
            developer(self, root, LoginFrame, username, password)
        else: tm.showerror("Page Access Error", "You do not have access to this page")
        
    def ext(event): root.destroy()
#------------------------------------------------
    # these lines are creating the 3 main buttons for the welcome page and configuring them them
    self.lab = Label(self, compound = "left", text="AI\ninfo", bg="#e5c379", pady=10, width=37, height=6)				
    self.lab.config(font=("Courier", 20))
    self.lab2 = Label(self, compound = "left", text="Data\ngraphs", bg="#99ccba", pady=10, width=37, height=6)
    self.lab2.config(font=("Courier", 20))
    self.lab3 = Label(self, compound = "left", text="Start AIs\nRunning", bg="#9197bf", width=50, height=3)
    self.lab3.config(font=("Courier", 30))

    self.bp = Label(self, text="• GUI settings", bg="#d7e0e5")	    # these lines are creating the other buttons for the page and configuring them
    self.bp.config(font=("Courier", 20), width=30, height=2)
    self.bp2 = Label(self, text="• current user", bg="#d7e0e5")
    self.bp2.config(font=("Courier", 20), width=30, height=2)
    self.bp3 = Label(self, text="• encrypt     ", bg="#d7e0e5")
    self.bp3.config(font=("Courier", 20), width=30, height=2)
    self.bp4 = Label(self, text="• Developer Options", bg="#d7e0e5")
    self.bp4.config(font=("Courier", 20), width=30, height=2)
    self.bp5 = Label(self, text="• Database page    ", bg="#d7e0e5")
    self.bp5.config(font=("Courier", 20), width=30, height=2)
    self.bp6 = Label(self, text="   -- exit --   ", bg="#a3c7cc", borderwidth=4, relief="groove")
    self.bp6.config(font=("Courier", 15), width=25, height=1)

    self.lab.bind("<Button-1>", aiScreen)			    # these lines are binding the buttons to their respective functions
    self.lab2.bind("<Button-1>", dataGraphs)
    self.lab3.bind("<Button-1>", StartRun)
    self.bp.bind("<Button-1>", GUIset)
    self.bp2.bind("<Button-1>", CUC)
    self.bp3.bind("<Button-1>", ENC)
    self.bp4.bind("<Button-1>", DEVOP)
    self.bp5.bind("<Button-1>", dataBP)
    self.bp6.bind("<Button-1>", ext)
    
    self.lab.grid(row=1, column=1, padx=2, pady=2)		    # these lines are placing the labels on the screen
    self.lab2.grid(row=1, column=2, padx=2)
    self.lab3.grid(row=2, column=1, columnspan=2)
    self.bp.grid(row=4, pady=5, column=1)
    self.bp2.grid(row=3, pady=5, column=1)
    self.bp3.grid(row=5, pady=5, column=1)
    self.bp4.grid(row=3, pady=10, column=2)
    self.bp5.grid(row=4, pady=5, column=2)
    self.bp6.grid(row=5, pady=5, column=2)
