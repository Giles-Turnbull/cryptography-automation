import os		    # these lines are imported libraries needed for the GUI
from tkinter import *
import tkinter.messagebox as tm
import datetime
import tkinter as tk
def database_page(self, root, LoginFrame, username, password):
    def dest():		    # this function is destroying the widgets on the page for when the page is changed
        self.canvas.destroy()
        self.scroll_y.destroy()
        self.scroll_x.destroy()
        self.frame.destroy()
        self.act_eff.destroy()
        self.est_eff.destroy()
        self.lab6.destroy()
    def ret(event):	    # this function is calling the dest function and and then loading the function main menu onto the page
        from mainMENU import main_menu
        dest()
        main_menu(self, root, LoginFrame, username, password)

    self.canvas = Canvas(self)
    self.scroll_y = Scrollbar(self, orient="vertical", command=self.canvas.yview)
    self.scroll_x = Scrollbar(self, orient="horizontal", command=self.canvas.xview) # two scroll bars are created and they control a canvas
#-----------------------------------------------
    self.frame = Frame(self.canvas)	    # this is creating a frame in the canvas
    self.width = 10
    self.height = 30
    for i in range(self.height):
        for j in range(self.width):		    # this is populating the frame with text fields for the database 
            self.b = Entry(self.frame, text="")
            self.b.grid(row=i, column=j)
#-----------------------------------------------
    # these lines are configuring the canvas with the scrollbars
    self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
    self.canvas.update_idletasks()
    self.canvas.configure(scrollregion=self.canvas.bbox('all'), bg="blue", yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set, height=350, width=700)

    # these lines are creating the efficiency labels and placing them on the page
    self.act_eff = Label(self, height=15, width=12, text="actual eff", font=("Courier", 20), bg="#bcebe2")
    self.est_eff = Label(self, height=15, width=12, text="actual eff", font=("Courier", 20), bg="#bcebe2")
    self.act_eff.grid(row=0, column=0, padx=15, rowspan=3)
    self.est_eff.grid(row=0, column=3, padx=15, rowspan=3)

    self.lab6 = Label(self, text="Return", bg="#a3c7cc", borderwidth=3, relief="groove")    # these lines are creating the return button and placing it
    self.lab6.config(font=("Courier", 20), width=35, height=1)
    self.lab6.grid(row=2, column=1, pady=30)
    
    self.canvas.grid(row=0, column=1)				# these lines are placing the canvas and scroll bars
    self.scroll_y.grid(row=0, column=2, ipady=140)
    self.scroll_x.grid(row=1, column=1, ipadx=300)

    self.lab6.bind("<Button-1>", ret) 				# this is binding the return button to the function ret
