import os				# these lines are imported libraries needed for the GUI
from tkinter import *
import tkinter.messagebox as tm
import datetime
import tkinter as tk

def signupPage():
    class signUP(Frame):
        def __init__(self, master):
            super().__init__(master)
            
            self.nameLabel = Label(self, text="name: ")           # these lines create the GUI
            self.nameEntry = Entry(self)
            self.usernameLabel = Label(self, text="username: ")
            self.usernameEntry = Entry(self)
            self.genderLabel = Label(self, text="gender: ")
            self.genderEntry = Entry(self)
            self.dobLabel = Label(self, text="DOB: ")
            self.dobEntry = Entry(self)
            self.desiredPasswordLabel = Label(self, text="desired password:")
            self.desiredPasswordEntry = Entry(self, show="*")
            self.repeatPasswordLabel = Label(self, text="repeat password: ")
            self.repeatPasswordEntry = Entry(self, show="*")

            self.signupButton = Button(self, text="signup", command=self.resetCLICKED)

            self.nameLabel.grid(row=0, column=0)
            self.nameEntry.grid(row=0, column=1)
            self.usernameLabel.grid(row=1, column=0)
            self.usernameEntry.grid(row=1, column=1)
            self.genderLabel.grid(row=2, column=0)
            self.genderEntry.grid(row=2, column=1)
            self.dobLabel.grid(row=3, column=0)
            self.dobEntry.grid(row=3, column=1)
            self.desiredPasswordLabel.grid(row=4, column=0)
            self.desiredPasswordEntry.grid(row=4, column=1)
            self.repeatPasswordLabel.grid(row=5, column=0)
            self.repeatPasswordEntry.grid(row=5, column=1)
            self.signupButton.grid(row=6, column=1, pady=5)
            
            self.pack(side="left", padx=5)

        def resetCLICKED(self):
            name = self.nameEntry.get()                                     # these lines retrieve the info from the entries
            username = self.usernameEntry.get()
            gender = self.genderEntry.get()
            dob = self.dobEntry.get()
            passOne = self.desiredPasswordEntry.get()
            passTwo = self.repeatPasswordEntry.get()

            found = False
            path, pathx = os.getcwd().split("\\"), ""                       # these lines find the files opened and created later in the function
            for i in path: pathx = pathx + i + "\\"
            pathy = pathx + "\\GUIdata\\Logins.txt"
            pathz = pathx + "\\userInfo\\" + username
            patha = pathz + ("\\" + username + "Info.txt")

            file = open(pathy, "r")                                         # these lines check if the user already exists
            for line in file:
                if ("username: " + username) in line: found = True
            file.close()
            if (found == False) and (len(passOne) > 7) and (passOne == passTwo) and (gender == "male" or gender == "female"):   # this line valid checks the info inputted
                try:
                    #datetime.datetime.strptime(dob, '%d-%m-Y%')
                    os.mkdir(pathz)                         # these lines create the user directory and create the user file
                    file = open(pathy, "a")
                    file.write("username: " + username + "\n" + "password: " + passOne + "\n")
                    file.close()
                    file = open(patha, "w")
                    file.write("admin: False\ngender: " + gender + "\nDOB: " + dob + "\nusername: " + username + "\npassword: " + passOne + "\nactivity: " + str(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")) + "\nlaston: \n")
                    file.close()
                    signroot.destroy()
                except ValueError: tm.showerror("Signup Error", "Invalid details entered") # these lines throw up a GUI error for the user if the info is invalid
            else: tm.showerror("Signup Error", "Invalid details entered")
            
            

    signroot = Tk()			    # these lines are creating the tkinter window and configuring it
    signroot.configure(pady=10)
    signroot.title('password changer')
    newFrame = signUP(signroot)
    signroot.mainloop()
