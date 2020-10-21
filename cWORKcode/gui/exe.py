import sys
import os
#import win32gui, win32con
#The_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)

place = os.getcwd() + "\\code\\"		# these lines find the login module, import it and load it
sys.path.insert(0, place)
from login_screen import login
login()
