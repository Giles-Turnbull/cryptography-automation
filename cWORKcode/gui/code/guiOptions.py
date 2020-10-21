from tkinter import colorchooser	    # these lines are imported libraries needed for the GUI
import os
from tkinter import *
import tkinter.messagebox as tm
import datetime
import tkinter as tk

def gui_options(self, root, LoginFrame, username, password):
    def dest():						# this function is destroying the widgets on the page for when the page is changed
        self.layfr.destroy()
        self.layfr2.destroy()
        self.layfr3.destroy()
        self.colorWid.destroy()
        self.colorWid2.destroy()
        self.colorWid3.destroy()
        self.colorWid4.destroy()
        self.colorWidCus.destroy()
        self.fontWid.destroy()
        self.fontWid2.destroy()
        self.fontWid3.destroy()
        self.fontWid4.destroy()
        self.fontWid5.destroy()
        self.lab6.destroy()
    def ret(event):			# this function is calling the dest function and and then loading the function main menu onto the page
        dest()
        from mainMENU import main_menu
        main_menu(self, root, LoginFrame, username, password)
#===================================================================================================================
    path, pathx = os.getcwd().split("\\"), ""               # these lines find the file and put the data into variable info
    for i in path: pathx = pathx + i + "\\"
    pathy = pathx + "\\GUIdata\\GUI_options.txt"            # these lines find the colour and font in the GUI_options file
    file = open(pathy, "r")
    for line in file:
        if "background: " in line: colour = line[12:-1]
        if "font: " in line: font = line[6:-1]
    file.close()
#===================================================================================================================
    def colourWidChanger(event):
        file, colour = open(pathy, "w"),  "#add8e6"                             # this line openes the text file
        file.write("background: " + "#add8e6\n" + "font: " + font + "\n")       # this line writes the change to the text file
        file.close()
        LoginFrame.configure(self, background=colour)                           # these lines update the GUI
        root.configure(pady=10, background=colour)
        self.layfr3.update()
        self.layfr3.config(bg=colour)
#===================================================================================================================
    def colourWid2Changer(event):
        file, colour = open(pathy, "w"),  "#90ee90"
        file.write("background: " + "#90ee90\n" + "font: " + font + "\n")
        file.close()
        LoginFrame.configure(self, background=colour)
        root.configure(pady=10, background=colour)
        self.layfr3.update()
        self.layfr3.config(bg=colour)
#===================================================================================================================
    def colourWid3Changer(event):
        file, colour = open(pathy, "w"),  "#fffdd0"
        file.write("background: " + "#fffdd0\n" + "font: " + font + "\n")
        file.close()
        LoginFrame.configure(self, background=colour)
        root.configure(pady=10, background=colour)
        self.layfr3.update()
        self.layfr3.config(bg=colour)
#===================================================================================================================
    def colourWid4Changer(event):
        file, colour = open(pathy, "w"),  "#D3D3D3"
        file.write("background: " + "#D3D3D3\n" + "font: " + font + "\n")
        file.close()
        LoginFrame.configure(self, background=colour)
        root.configure(pady=10, background=colour)
        self.layfr3.update()
        self.layfr3.config(bg=colour)
#===================================================================================================================
    def colourWidCusChanger(event):
        colourCHOO = colorchooser.askcolor(title="select color")        # this line generates the colour chooser
        colour = colourCHOO[1]                                          # this line retrives the output
        try:                                                            # this try and except just mean there is no error message when cancelling
            if colour[1] != None:
                file = open(pathy, "w")
                file.write("background: " + colour + "\n" + "font: " + font + "\n")     # these lines write the colour to the text file
                file.close()
                LoginFrame.configure(self, background=colour)
                root.configure(pady=10, background=colour)                              # these lines update the GUI
                self.layfr3.update()
                self.layfr3.config(bg=colour)
        except: expen = ""
#===================================================================================================================
    def fontWidChanger(event):
        file, font = open(pathy, "w"), '("Times", 12, "bold")'      # this opens up the text file and writes the new font
        file.write("background: " + colour + "\n" + "font: " + font + "\n")
        file.close()
#===================================================================================================================
    def fontWid2Changer(event):
        file, font = open(pathy, "w"), '("Arial", 12)'
        file.write("background: " + colour + "\n" + "font: " + font + "\n")
        file.close()
#===================================================================================================================
    def fontWid3Changer(event):
        file, font = open(pathy, "w"), '("Helvetica", 11, "bold italic")'
        file.write("background: " + colour + "\n" + "font: " + font + "\n")
        file.close()
#===================================================================================================================
    def fontWid4Changer(event):
        file, font = open(pathy, "w"), '("Lucida Console", 11)'
        file.write("background: " + colour + "\n" + "font: " + font + "\n")
        file.close()
#===================================================================================================================
    def fontWid5Changer(event):
        file, font = open(pathy, "w"), '("MS Gothic", 13)'
        file.write("background: " + colour + "\n" + "font: " + font + "\n")
        file.close()
#===================================================================================================================
    self.layfr = Frame(self, bg="#ffffff", width=400, height=450,)  # these lines are creating the three frames and placing them on the screen
    self.layfr2 = Frame(self, bg="#ffffff", width=400, height=450)
    self.layfr3 = Frame(self, width=120, height=450, bg=colour)					# this frame is just a spacer
    self.layfr.grid(row=0, column=1, padx=50, sticky="nsew")
    self.layfr2.grid(row=0, column=2, padx=50, sticky="nsew")
    self.layfr3.grid(row=0, column=0, sticky="nsew")

    # these lines are creating colour labels and placing them in the frame
    self.colorWid = Label(self.layfr, width=35, height=3, font=("Arial", 12), bg="#add8e6") 
    self.colorWid.grid(row=1, column=1, pady=15, padx=25)
    self.colorWid2 = Label(self.layfr, width=35, height=3, font=("Arial", 12), bg="#90ee90")
    self.colorWid2.grid(row=2, column=1, pady=15, padx=25)
    self.colorWid3 = Label(self.layfr, width=35, height=3, font=("Arial", 12), bg="#fffdd0")
    self.colorWid3.grid(row=3, column=1, pady=15, padx=25)
    self.colorWid4 = Label(self.layfr, width=35, height=3, font=("Arial", 12), bg="#D3D3D3")
    self.colorWid4.grid(row=4, column=1, pady=15, padx=25)
    self.colorWidCus = Label(self.layfr, width=35, height=3, font=("Arial", 12), text="custom", relief="raised")
    self.colorWidCus.grid(row=5, column=1, pady=15, padx=25)

    self.colorWid.bind("<Button-1>", colourWidChanger)
    self.colorWid2.bind("<Button-1>", colourWid2Changer)
    self.colorWid3.bind("<Button-1>", colourWid3Changer)
    self.colorWid4.bind("<Button-1>", colourWid4Changer)
    self.colorWidCus.bind("<Button-1>", colourWidCusChanger)

    # these lines are creating font labels and placing them in the frame
    self.fontWid = Label(self.layfr2, width=35, height=3, font=("Times", 12, "bold"), text="'times' font1")		
    self.fontWid.grid(row=1, column=1, pady=15, padx=25)
    self.fontWid2 = Label(self.layfr2, width=35, height=3, font=("Arial", 12), text="'Arial' font2")
    self.fontWid2.grid(row=2, column=1, pady=15, padx=25)
    self.fontWid3 = Label(self.layfr2, width=35, height=3, font=("Helvetica", 11, "bold italic"), text="'helvetica' font3")
    self.fontWid3.grid(row=3, column=1, pady=15, padx=25)
    self.fontWid4 = Label(self.layfr2, width=35, height=3, font=("Lucida Console", 11), text="'Lucida Console' font4")
    self.fontWid4.grid(row=4, column=1, pady=15, padx=25)
    self.fontWid5 = Label(self.layfr2, width=35, height=3, font=("MS Gothic", 13), text="'MS Gothic' font5")
    self.fontWid5.grid(row=5, column=1, pady=15, padx=25)

    self.fontWid.bind("<Button-1>", fontWidChanger)
    self.fontWid2.bind("<Button-1>", fontWid2Changer)
    self.fontWid3.bind("<Button-1>", fontWid3Changer)
    self.fontWid4.bind("<Button-1>", fontWid4Changer)
    self.fontWid5.bind("<Button-1>", fontWid5Changer)

    self.lab6 = Label(self, text="Return", bg="#a3c7cc", borderwidth=3, relief="groove") # these lines are creating the return button and placing it
    self.lab6.config(font=("Courier", 20), width=35, height=1)
    self.lab6.grid(row=1, column=1, columnspan=3, pady=20)
    self.lab6.bind("<Button-1>", ret)
    
