import os				# these lines are imported libraries needed for the GUI
from tkinter import *
import tkinter.messagebox as tm
import datetime
import tkinter as tk

def encrypt_page(self, root, LoginFrame, username, password):
    def dest():				# this function is destroying the widgets on the page for when the page is changed
        self.canvas.destroy()
        self.scroll_y.destroy()
        self.frame.destroy()
        self.input_ent.destroy()
        self.output_ent.destroy()
        self.convert.destroy()
        self.retB.destroy()
    def ret(event):		# this function is calling the dest function and and then loading the function main menu onto the page
        dest()
        from mainMENU import main_menu
        main_menu(self, root, LoginFrame, username, password) 
    def reses(event): self.output_ent.insert("1.0", "example text")		    # this line creates the function for conversion
#=====================
    self.canvas = Canvas(self)			# these lines create a canvas and scrollbar and frame, the frame is put in the canvas
    self.scroll_y = Scrollbar(self, orient="vertical", command=self.canvas.yview)
    self.frame = Frame(self.canvas)

    # this line creates buttons and puts them in the frame
    for i in range(20): test = Label(self.frame, text='label %i' % i, height=1, width=22, bg="#bcebe2", relief="groove", font=("Courier", 20)).pack(pady=5, padx=10)	
    ## use globals to create the buttons 
    self.canvas.create_window(0, 0, anchor='nw', window=self.frame)			# these lines configure the canvas
    self.canvas.update_idletasks()

    # these lines configure the canvas and scroll bar
    self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scroll_y.set, height=500)		
    self.canvas.grid(row=0, column=0, rowspan=6)
    self.scroll_y.grid(row=0, column=1, ipady=265, rowspan=6)
#=====================

    self.input_ent = Text(self, width=90, height=10)				    # these lines create the input entry and place it on the screen
    self.input_ent.grid(row=1, column=2, padx=50)

    self.output_ent = Text(self, width=90, height=10)						# these lines create the output entry and place it on the screen
    self.output_ent.grid(row=2, column=2, padx=50)

    self.convert = Label(self, text="convert", bg="#a3c7cc", borderwidth=2, relief="groove")	# these lines create the covert button and place it on the screen
    self.convert.config(font=("Courier", 10), width=15, height=2)
    self.convert.grid(row=3, column=2, columnspan=3)

    self.retB = Label(self, text="Return", bg="#a3c7cc", borderwidth=3, relief="groove")	    # these lines are creating the return button and placing it
    self.retB.config(font=("Courier", 20), width=35, height=1)
    self.retB.grid(row=4, column=2, columnspan=3)
    
    self.retB.bind("<Button-1>", ret)				# these are binding the return button and the convert button to the function ret and reses
    self.convert.bind("<Button-1>", reses)
