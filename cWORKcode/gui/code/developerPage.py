import os		    # these lines are imported libraries needed for the GUI
from tkinter import *
import tkinter.messagebox as tm
import datetime
import tkinter as tk
import shutil

def developer(self, root, LoginFrame, username, password):
    def dest():			    # this function is destroying the widgets on the page for when the page is changed
        self.userBanner.destroy()
        self.filesBanner.destroy()
        self.infoBanner.destroy()
        self.spacer.destroy()
        self.userScroll.destroy()
        self.userBox.destroy()
        self.fileScroll.destroy()
        self.fileBox.destroy()
        self.delUserBut.destroy()
        self.delFileBut.destroy()
        self.devUserBut.destroy()
        self.DELUSER_ent.destroy()
        self.DELFILE_ent.destroy()
        self.DEVUSER_ent.destroy()
        self.lab6.destroy()
    def ret(event):	    # this function is calling the dest function and and then loading the function main menu onto the page
        dest()
        from mainMENU import main_menu
        main_menu(self, root, LoginFrame, username, password)
    def DevopFunc(event):
        try:
            devUser = self.DEVUSER_ent.get()
            path, pathx = os.getcwd().split("\\"), ""                       # these lines find the files opened and created later in the function
            for i in path: pathx = pathx + i + "\\"
            pathy = pathx + "\\userInfo\\" + devUser
            pathz = pathy + ("\\" + devUser + "Info.txt")
            file, lines = open(pathz, "r"), []
            for line in file:                                               # these lines find the admin data in the user text file
                if "admin: " in line: lines.append("admin: True\n")
                else: lines.append(line)
            file.close()
            file = open(pathz, "w")                                         # these lines overwrite the file
            for i in lines: file.write(i)
            file.close()
            messagebox.showinfo("Success", "the user was made a developer") # this shows a success message
        except: tm.showerror("Error", "That user does not exist")           # this error message is shown if the user does not exist

    def DelUserFunc(event):
        MsgBox = messagebox.askquestion('Delete Account','Are you sure you want delete this user?',icon = 'warning')
        if MsgBox == 'yes':
            try:
                delUser = self.DELUSER_ent.get()
                if delUser == "": tm.showerror("Error", "That user does not exist")
                else:
                    path, pathx, lines = os.getcwd().split("\\"), "", []                       # these lines find text files and put them in a string
                    for i in path: pathx = pathx + i + "\\"
                    pathy = pathx + "\\GUIdata\\logins.txt"
                    pathx = pathx + "\\userInfo\\" + delUser
                    shutil.rmtree(pathx)
                    file, skip = open(pathy, "r"), False
                    for line in file:                                               # these lines find the login info
                        if delUser in line and skip == False: skip = True
                        elif skip == True: skip = False
                        else: lines.append(line)
                    file.close()
                    file = open(pathy, "w")
                    for x in lines: file.write(x)                                   # this line re-writes the file, deleting the users info
                    file.close()
#-----------------------------------------------------------
                    path.pop()
                    patha = ""
                    for i in path: patha = patha + i + "\\"
                    pathb = patha + "\\crypto_modules\\data\\queue.txt"
                    pathc = patha + "\\crypto_modules\\data\\objects.txt"       # find the file paths
                    rewrite, trigger = [], False
                    file = open(pathb, "w")                                     # clear the queue
                    file.close()
                    file = open(pathc, "r")
                    for line in file:                                           # remove users objects
                        if trigger == False:
                            if delUser in line: trigger = True
                            else: rewrite.append(line)
                        else: trigger = False
                    file.close()
                    file = open(pathc, "w")
                    for line in rewrite:
                        file.write(line)
                    file.close()
#-----------------------------------------------------------
                    messagebox.showinfo("Success", "the user was deleted")
            except: tm.showerror("Error", "That user does not exist")

    def DelUserFile(event):
        fileToDel = self.DELFILE_ent.get()
        if fileToDel != "":
            path, pathx, found = os.getcwd().split("\\"), "", False              # these lines find the file and put the data into variable info
            directories, allUserFiles = [], ""
            for i in path: pathx = pathx + i + "\\"
            pathy = pathx + "\\userInfo"
            direcTwo = os.listdir(pathy)
            for i in direcTwo: directories.append(pathy + "\\" + i)     # these lines find all the current user files
            for i in directories:
                currentDIR = os.listdir(i)
                for x in currentDIR:
                    try:
                        FTD = i + "\\" + fileToDel
                        os.remove(FTD)                    # this line removes the file
                        messagebox.showinfo("Success", "the file was deleted")      # this line shows the success message
                        found = True
                    except: expen = ""                      # this line is a filler
        if found == False: tm.showerror("Error", "That file does not exist")       # if the file is not found then this error message shows
                
        

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
    path, pathx, users = os.getcwd().split("\\"), "", ""               # these lines find the file and put the data into variable info
    for i in path: pathx = pathx + i + "\\"
    pathy = pathx + "\\userInfo"                                    # these lines find the users in the directory
    direc = os.listdir(pathy)
    for file in direc: users = users + file + "\n"
    
#===================================================================================================================
    path, pathx = os.getcwd().split("\\"), ""              # these lines find the file and put the data into variable info
    directories, allUserFiles = [], ""
    for i in path: pathx = pathx + i + "\\"
    pathy = pathx + "\\userInfo"
    direcTwo = os.listdir(pathy)
    for i in direcTwo: directories.append(pathy + "\\" + i)     # these lines find all the current user files
    for i in directories:
        currentDIR = os.listdir(i)
        for x in currentDIR:
            allUserFiles = allUserFiles + x + "\n"
#===================================================================================================================
    
    self.userBanner = Label(self, height=2, width=20, font=("Courier", 15), text="all users", bg="#add8e6")   # these lines are creating the 3 top banners
    self.filesBanner = Label(self, height=2, width=20, font=("Courier", 15), text="user files", bg="#add8e6")
    self.infoBanner = Label(self, height=3, width=35, font=("Courier", 10), text="welcome user, you have\naccess to developer options", bg="#add8e6")
    self.spacer = Label(self, height=1, width=18, bg=colour)

    self.userScroll = Scrollbar(self)				    # these lines are for creating the all user box and user files box with scroll bars
    self.userBox = Text(self, yscrollcommand=self.userScroll.set, bg="#dee0e2", font=("verdana", 11), relief="sunken")
    self.userBox.config(height=20, width=25)
    self.userScroll.config(command=self.userBox.yview)
    self.fileScroll = Scrollbar(self)
    self.fileBox = Text(self, yscrollcommand=self.fileScroll.set, bg="#dee0e2", font=("verdana", 11), relief="sunken")
    self.fileBox.config(height=20, width=25)
    self.fileScroll.config(command=self.fileBox.yview)
    self.userBox.insert("1.0", users)
    self.fileBox.insert("1.0", allUserFiles)

    # these lines create the 3 buttons with user inputs
    self.delUserBut = Label(self, height=3, width=35, font=("Courier", 10), text="delete a user", bg="#add8e6")
    self.delFileBut = Label(self, height=3, width=35, font=("Courier", 10), text="delete a file", bg="#add8e6")
    self.devUserBut = Label(self, height=3, width=35, font=("Courier", 10), text="devop a person", bg="#add8e6")
    self.DELUSER_ent = Entry(self, width=60)
    self.DELFILE_ent = Entry(self, width=60)
    self.DEVUSER_ent = Entry(self, width=60)

    self.spacer.grid(row=0, column=0)				    # these lines are griding the former created widgets and placing them on the screen
    self.userBanner.grid(row=0, column=1, padx=10, pady=10)
    self.filesBanner.grid(row=0, column=3, padx=10)
    self.infoBanner.grid(row=0, column=5, padx=10)
    self.userBox.grid(row=1, column=1, rowspan=7)
    self.userScroll.grid(row=1, column=2, ipady=150, rowspan=7)
    self.fileBox.grid(row=1, column=3, rowspan=7)
    self.fileScroll.grid(row=1, column=4, ipady=150, rowspan=7)
    self.delUserBut.grid(row=2, column=5)
    self.DELUSER_ent.grid(row=3, column=5, padx=10)
    self.delFileBut.grid(row=4, column=5)
    self.DELFILE_ent.grid(row=5, column=5)
    self.devUserBut.grid(row=6, column=5)
    self.DEVUSER_ent.grid(row=7, column=5)
    
    self.lab6 = Label(self, text="Return", bg="#a3c7cc", borderwidth=3, relief="groove")    # these lines are creating the return button and placing it
    self.lab6.config(font=("Courier", 20), width=35, height=1)
    self.lab6.grid(row=8, column=1, columnspan=5, pady= 10)

    self.delFileBut.bind("<Button-1>", DelUserFile)
    self.delUserBut.bind("<Button-1>", DelUserFunc)
    self.devUserBut.bind("<Button-1>", DevopFunc)
    self.lab6.bind("<Button-1>", ret)								# this is binding the return button to the function ret
