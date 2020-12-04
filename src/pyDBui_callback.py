#! /usr/bin/env python

import sys

guestrec = {  "username" : "guest", "usertype" : "casual", "spendingrange" : "20", "platformtype" : "*" }

johnrec = {  "username" : "john", "usertype" : "casual", "spendingrange" : "20", "platformtype" : "Xbox" }
                
maryrec = {  "username" : "mary", "usertype" : "hardcore", "spendingrange" : "50", "platformtype" : "Sony" }
         

users = [ ]   
users.append(guestrec)            
users.append(johnrec)
users.append(maryrec)  

currentuser = "guest"
currentusertype = "casual"
currentspendingrange = "50"
currentplatformtype = "*"


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global username
    username = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

import profile

def open_profile():
    print('pyDBui_callback.open_profile')
    w.Label2.config (text='''choose a login option''')
    sys.stdout.flush()
    profile.create_profile(root)
    hide_window()
    
import query

def open_query():
    global currentusertype, currentpsendingrange, currentplatformtype, currentuser, top_level, w
    print('pyDBui_callback.open_query')
    sys.stdout.flush()
    currentuser = username.get()
    for i in users :
        if ( i.get("username") == currentuser ):
            currentRec = i
            break
    try:
        currentRec
    except NameError:
        w.Label2.config (text='''user not found''')
    else:
        print(currentuser)
        currentusertype = i.get("usertype")
        currentspendingrange = i.get("spendingrange")
        currentplatformtype = i.get("platformtype")
        print(currentuser + " " + currentplatformtype)
        w.Label2.config (text='''choose a login option''')
        sys.stdout.flush()
        query.create_query(root)
        hide_window() 
    sys.stdout.flush()

def open_query_guest():
    print('pyDBui_callback.open_query_guest')
    sys.stdout.flush()
    currentuser = "guest"
    for i in users:
        if (i.get("username") == currentuser):
            currentRec = i
            break
    print(currentuser)
    currentusertype = i.get("usertype")
    currentspendingrange = i.get("spendingrange")
    currentplatformtype = i.get("platformtype")
    w.Label2.config (text='''choose a login option''')
    sys.stdout.flush()
    query.create_query(root)
    hide_window() 

def hide_window():
    # Function which closes the window.
    global top_level
    top_level.withdraw()
    
    
def show_window():
    # Function which closes the window.
    global top_level
    top_level.deiconify()
    
    
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import pyDBui
    pyDBui.vp_start_gui()




