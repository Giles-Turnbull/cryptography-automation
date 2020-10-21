import os				# these lines are imported libraries needed for the GUI
from tkinter import *
import tkinter.messagebox as tm
import datetime
import tkinter as tk
import shutil

def User_page_run(self, root, LoginFrame, username, password):
    def dest():				# this function is destroying the widgets on the page for when the page is changed
        self.lab.destroy()
        self.eula.destroy()
        self.scroll.destroy()
        self.lab3.destroy()
        self.lab4.destroy()
        self.lab5.destroy()
        self.lab6.destroy()
        self.lab7.destroy()
        self.lab8.destroy()
    def ret(event):			# this function is calling the dest function and and then loading the function main menu onto the page
        dest()
        from mainMENU import main_menu
        main_menu(self, root, LoginFrame, username, password)
    def delACC(event):
        MsgBox = messagebox.askquestion('Delete Account','Are you sure you want delete your account?',icon = 'warning')
        if MsgBox == 'yes':
            path, pathx = os.getcwd().split("\\"), ""                       # these lines find text files and put them in a string
            for i in path: pathx = pathx + i + "\\"
            pathy = pathx + "\\GUIdata\\logins.txt"
            pathx = pathx + "\\userInfo\\" + username
            shutil.rmtree(pathx)
            file, lines, skip = open(pathy, "r"), [], False
            for line in file:                                               # these lines find the login info
                if username in line and skip == False: skip = True
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
                    if username in line: trigger = True
                    else: rewrite.append(line)
                else: trigger = False
            file.close()
            file = open(pathc, "w")
            for line in rewrite:
                file.write(line)
            file.close()
#-----------------------------------------------------------
            root.destroy()
            from login_screen import login                                  # these lines open up a new login window
            login()
        else:
            messagebox.showinfo('Return','action cancelled')
    def logout(event):
        root.destroy()
        from login_screen import login                                  # these lines open up a new login window
        login()
    def changePass(event):
        path, pathx = os.getcwd().split("\\"), ""                       # these lines find the path to the file containing the code
        for i in path: pathx = pathx + i + "\\"
        pathy = pathx + "\\code\\smallModules\\passwordChanger.py"
        import importlib.util
        spec = importlib.util.spec_from_file_location("passwordChanger", pathy)     # these lines open the module
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        foo.changePasswordFunc(username, password)                      # this line runs the module and passes username and password


    self.lab = Label(self, text=("Greetings", username), bg="#b7e0e5")				# these lines are creating a welcome label
    self.lab.config(font=("Courier", 20), width=45, height=2)

    self.scroll = Scrollbar(self)   # these lines create a scroll bar and an area showing text files, then links the scroll bar to the text area
    self.eula = Text(self, yscrollcommand=self.scroll.set, bg="#dee0e2", font=("verdana", 11), relief="sunken")
    self.eula.config(height=15, width=25)
    self.scroll.config(command=self.eula.yview)
#==============================================================================================
    paths = ""
    path, pathx = os.getcwd().split("\\"), ""                       # these lines find text files and put them in a string
    for i in path: pathx = pathx + i + "\\"
    pathx = pathx + "\\userInfo\\" + username                       #### need to add username and password to params
    afiles = os.listdir(pathx)
    for i in afiles: paths = paths + i + "\n"
    self.eula.insert("1.0", paths)
#==============================================================================================
    path, pathx = os.getcwd().split("\\"), ""                       # these lines find text files and put them in a string
    for i in path: pathx = pathx + i + "\\"
    pathx = pathx + "\\userInfo\\" + username + "\\" + username + "Info.txt"
    file = open(pathx, "r")
    for line in file:
        if "activity: " in line: currentTime = line[10:-1]          # these lines retrieve the info from the users text file
        if "laston: " in line: laston = line[8:-1]
    file.close()
    retLO = laston
    laston = laston.split(" ")
    currentTime = currentTime.split(" ")
    
    if laston[4] != currentTime[4]:
        ret = str(int(laston[4])- int(currentTime[4])) + " years"       # these lines calculate the time difference
    elif laston[3] != currentTime[3]: retAC = str(int(laston[3][:-1])- int(laston[3][:-1])) + " days"
    elif laston[2] != currentTime[2]: retAC = "over a month"
    else: retAC = "less than a day"
#==============================================================================================
    self.lab7 = Label(self, text="users files:", bg="#b7e0e5")					# these lines are creating a welcome label
    self.lab7.config(font=("Courier", 10), width=30, height=2)

    # these lines are creating the activity widget, the delete account button and change user button
    self.lab3 = Label(self, text=("Activity\nLast on: " + retLO + "\nTime inbetween: " + retAC), bg="#b7e0e5")			
    self.lab3.config(font=("Courier", 10), width=40, height=3)
    self.lab4 = Label(self, text=("delete Account"), bg="#a3c7cc", borderwidth=5, relief="groove")
    self.lab4.config(font=("Courier", 20), width=20, height=2)
    self.lab5 = Label(self, text=("change Password"), bg="#a3c7cc", borderwidth=5, relief="groove")
    self.lab5.config(font=("Courier", 20), width=20, height=2)

    self.lab6 = Label(self, text="Return", bg="#a3c7cc", borderwidth=3, relief="groove")    # these lines are creating the return and logout buttons
    self.lab6.config(font=("Courier", 20), width=35, height=1)
    self.lab8 = Label(self, text="-- Logout --", bg="#b7e0e5", borderwidth=2, relief="groove")
    self.lab8.config(font=("Courier", 15), width=25, height=1)

    self.lab6.bind("<Button-1>", ret)							    # this line binds the return button to the ret function
    self.lab4.bind("<Button-1>", delACC)
    self.lab5.bind("<Button-1>", changePass)
    self.lab8.bind("<Button-1>", logout)


    self.lab.grid(row=0, column=0, columnspan=100, pady=20, padx=220)		    # these lines are placing the aforementioned widgets on the page
    self.lab3.grid(row=1, column=90)
    self.lab4.grid(row=2, column=90)
    self.lab5.grid(row=3, column=90)
    self.lab6.grid(row=5, column=0, columnspan=100, pady=10)
    self.lab8.grid(row=6, column=0, columnspan=100, pady=5)
    self.lab7.grid(row=1, column=10)
    self.eula.grid(row=2, column=10, rowspan=3)
    self.scroll.grid(row=2, column=11, ipady=100, rowspan=3)
