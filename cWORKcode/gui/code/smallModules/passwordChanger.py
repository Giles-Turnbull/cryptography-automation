import os				# these lines are imported libraries needed for the GUI
from tkinter import *
import tkinter.messagebox as tm
import datetime
import tkinter as tk

def changePasswordFunc(username, password):
    class passC(Frame):
        def __init__(self, master):
            super().__init__(master)
            
            self.currentPasswordLabel = Label(self, text="current password:")           # these lines create the GUI
            self.currentPasswordEntry = Entry(self, show="*")
            self.desiredPasswordLabel = Label(self, text="desired password:")
            self.desiredPasswordEntry = Entry(self, show="*")
            self.repeatPasswordLabel = Label(self, text="repeat password: ")
            self.repeatPasswordEntry = Entry(self, show="*")
            self.loginButton = Button(self, text="reset", command=self.resetCLICKED)

            self.currentPasswordLabel.grid(row=0, column=1)
            self.currentPasswordEntry.grid(row=0, column=2, pady=1, columnspan=2)
            self.desiredPasswordLabel.grid(row=1, column=1)
            self.desiredPasswordEntry.grid(row=1, column=2, pady=1, columnspan=2)
            self.repeatPasswordLabel.grid(row=2, column=1)
            self.repeatPasswordEntry.grid(row=2, column=2, pady=1, columnspan=2)
            self.loginButton.grid(row=3, column=2, pady=5)
            self.pack(side="left", padx=5)

        def resetCLICKED(self):
            passOne = self.currentPasswordEntry.get()                   # these lines get the inputs
            passTwo = self.desiredPasswordEntry.get()
            passThree = self.repeatPasswordEntry.get()
            if (passThree == passTwo) and (len(passTwo) > 6) and (passOne == password):
                path, pathx = os.getcwd().split("\\"), ""                                   # these lines find text files and put them in a string
                for i in path: pathx = pathx + i + "\\"
                pathz = pathx + "\\GUIdata\\Logins.txt"
                pathy = pathx + "\\userInfo\\" + username + "\\" + username + "Info.txt"    # these lines find the user info file
                file, lines, lines2 = open(pathy, "r"), [], []
                for line in file:
                    if "password: " in line: lines.append("password: " + passTwo + "\n")    # these lines change the info in the text file
                    else: lines.append(line)
                file.close()
                file = open(pathy, "w")                                                     # these lines over write the text file
                for i in lines: file.write(i)
                file.close()
                file = open(pathz, "r")
                for line in file:                                                           # these line change the password in the Logins text file
                    if ("password: " + password) in line: lines2.append("password: " + passTwo + "\n")
                    else: lines2.append(line)
                file.close()
                file = open(pathz, "w")
                for i in lines2: file.write(i)
                file.close()
                passCroot.destroy()
                password = passTwo                          # this line changes the password being passed back to the module
            else: tm.showerror("Reset Error", "Incorrect details entered")

    passCroot = Tk()						# these lines are creating the tkinter window and configuring it
    passCroot.configure(pady=10)
    passCroot.title('password changer')
    newFrame = passC(passCroot)
    passCroot.mainloop()
