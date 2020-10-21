import os							# these lines are imported libraries needed for the GUI
from tkinter import *
import tkinter.messagebox as tm
import datetime
from mainMENU import main_menu

### os.mkdir("H:/Alevel/Computer Science/cWORKcode/gui/userInfo/test")

def login():						        # these lines are creating a function within a class within a function
    class LoginFrame(Frame):
        def __init__(self, master):
            super().__init__(master)
#===================================================================================================================
            path, pathx = os.getcwd().split("\\"), ""               # these lines find the file and put the data into variable info
            for i in path: pathx = pathx + i + "\\"
            pathy = pathx + "\\GUIdata\\GUI_options.txt"            # these lines find the colour and font in the GUI_options file
            file = open(pathy, "r")
            for line in file:
                if "background: " in line: colour = line[12:-1]
                if "font: " in line: font = line[6:-1]        # this line turns the string into a tuple
            file.close()
            LoginFrame.configure(self, background=colour)
#===================================================================================================================
            su, sp = "", ""
            path, pathx = os.getcwd().split("\\"), ""                       # these lines find the file and put the data into variable info
            for i in path: pathx = pathx + i + "\\"
            pathy = pathx + "\\GUIdata\\currentUP.txt"
            pathx = pathx + "\\GUIdata\\Var.txt"
            self.file = open(pathx, "r")
            for line in self.file:
                if "check: " in line: self.info = line[7:-1]                # this line finds the info in Var.txt
            if self.info == "True":
                self.Cvalue = IntVar(value=1)
                file = open(pathy, "r")
                for line in file:
                    if "username: " in line: su = line[10:-1]               # if the check button is checked then it subs in found username and passoword
                    if "password: " in line: sp = line[10:-1]
                file.close()
            else: self.Cvalue = IntVar(value=0)
#===================================================================================================================

#===================================================================================================================
            self.gap = Label(self, height=1, width=10, bg=colour)	        # these lines are creating the username and password labels and entries
            self.userLab = Label(self, text="username:", bg=colour)
            self.userEnt = Entry(self)
            self.passLab = Label(self, text="password:", bg=colour)
            self.passEnt = Entry(self, show="*")

            self.loginBUT = Button(self, text="Login", command=self.loginCLICKED)	# these lines are creating the login button, signup button and check box
            self.signupBUT = Button(self, text="signup?", command=self.sugnUP)		# they are linked with commands to their respective functions
            self.logedin = Checkbutton(self, text="Keep logged in", variable = self.Cvalue, command=self.kli, bg=colour)

            self.userEnt.insert(0, su)
            self.passEnt.insert(0, sp)

            self.gap.grid(row=0, column=0)						# these lines are placing the username and password labels and entries on the screen
            self.userLab.grid(row=0, column=1)
            self.userEnt.grid(row=0, column=2, columnspan=2)
            self.passLab.grid(row=1, column=1, pady=1)
            self.passEnt.grid(row=1, column=2, pady=1, columnspan=2)
            self.logedin.grid(row=2, column=1)
            self.loginBUT.grid(row=2, column=2)
            self.signupBUT.grid(row=2, column=3)
            self.pack(side="left", padx=5)
#===================================================================================================================
        def loginCLICKED(self):
            def activity():
                path, pathx = os.getcwd().split("\\"), ""                       # these lines find the file and put the data into variable info
                for i in path: pathx = pathx + i + "\\"
                pathy = pathx + "\\userInfo\\" + username + "\\" + username + "Info.txt"
                file, lines = open(pathy, "r"), []
                for line in file:                                               # these lines open the user info file
                    if "activity: " in line:
                        activityVar = line[10:-1]                               # these lines change the laston line to activity and activity to current dt
                        lines.append("activity: " + str(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")) + "\n")
                    elif "laston: " in line: lines.append("laston: " + activityVar + "\n")
                    else: lines.append(line)
                file.close()                                                    # these lines write it to the file
                file = open(pathy, "w")
                for x in lines: file.write(x)
                file.close()
#===================================================================================================================
            try:								# this line is for an incorrect login attempt
                username = self.userEnt.get()
                password = self.passEnt.get()
                usernames, passwords = [], []
                path, pathx = os.getcwd().split("\\"), ""                       # these lines find the file and put the data into lists
                for i in path: pathx = pathx + i + "\\"
                pathx = pathx + "\\GUIdata\\Logins.txt"
                file = open(pathx, "r")
                for line in file:
                    if "username: " in line: usernames.append(line[10:-1])
                    if "password: " in line: passwords.append(line[10:-1])
                file.close()
                
                if usernames.index(username) == passwords.index(password): # if they are in the same place in text file showing correspondence
                    activity()
                    #############################
                    self.userLab.destroy()					        # these lines are for destroying the widgets on the page for the welcome page to be loaded
                    self.userEnt.destroy()
                    self.passLab.destroy()
                    self.passEnt.destroy()
                    self.loginBUT.destroy()
                    self.signupBUT.destroy()
                    self.logedin.destroy()
                    self.gap.destroy()
                    main_menu(self, root, LoginFrame, username, password) 													# this line loads the menu function
                    #############################
            except ValueError: tm.showerror("Login error", "Incorrect login details")		# this line shows an error if the login details are invalid
#===================================================================================================================
        def sugnUP(self):                                                           		# signup function
            path, pathx = os.getcwd().split("\\"), ""                       # these lines find the path to the file containing the code
            for i in path: pathx = pathx + i + "\\"
            pathy = pathx + "\\code\\smallModules\\signup.py"
            import importlib.util
            spec = importlib.util.spec_from_file_location("signup", pathy)     # these lines open the module
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
            foo.signupPage()
#===================================================================================================================
        def kli(self):																# the checkbox function 
            path, pathx = os.getcwd().split("\\"), ""               # these lines find the file and put the data into variable info
            for i in path: pathx = pathx + i + "\\"
            pathy = pathx + "\\GUIdata\\currentUP.txt"
            pathx = pathx + "\\GUIdata\\Var.txt"
            file = open(pathx, "r")
            for line in file:
                if "check: " in line: info = line[7:-1]
            if info == "True":
                fileTwo = open(pathx, "w")
                fileTwo.write("check: False\n")                             # these lines change the value of the variable info
                fileTwo.close()
            else:
                fileTwo = open(pathx, "w")
                fileTwo.write("check: True\n")                  # these lines changes the saved username and passowrd in currentUP
                fileTwo.close()
                fileThree = open(pathy, "w")
                fileThree.write("username: " + self.userEnt.get() + "\npassword: " + self.passEnt.get() + "\n") 
                file.close()
            file.close()
#===================================================================================================================
    path, pathx = os.getcwd().split("\\"), ""               # these lines find the file and put the data into variable info
    for i in path: pathx = pathx + i + "\\"
    pathy = pathx + "\\GUIdata\\GUI_options.txt"            # these lines find the colour in the GUI_options file
    file = open(pathy, "r")
    for line in file:
        if "background: " in line: colour = line[12:-1]
        if "font: " in line: font = line[6:-1]
    file.close()

    root = Tk()						# these lines are creating the tkinter window and configuring it
    root.configure(pady=10, background=colour)
    root.geometry("1200x600")
    root.title('personal gui')
    lf = LoginFrame(root)
    root.mainloop()
