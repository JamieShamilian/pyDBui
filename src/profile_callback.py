#! /usr/bin/env python


import sys
import pyDBui_callback

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
    global profilename
    profilename = tk.StringVar()
    global usertype
    usertype = tk.StringVar()
    global spendingrange
    spendingrange = tk.StringVar()
    global platformtype
    platformtype = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

import query

def open_query():
    print('profile_callback.open_query')
    sys.stdout.flush()
    currentuser = username.get()
    for i in pyDBui_callback.users:
        print ( i.get("username") )
        if i.get("username") == currentuser :
            print(currentuser)
            currentRec = i
            break
    try:
        currentRec
    except NameError:
        print("New name")
        pyDBui_callback.currentuser = currentuser
        print(pyDBui_callback.currentuser)
        currentusertype = usertype.get()
        currentspendingrange = spendingrange.get() #i.get("spendingrange")
        currentplatformtype = platformtype.get()  #i.get("platformtype")
        addrec = { "username": profilename, "usertype" : usertype, "spendingrange": spendingrange, "platformtype" : platformtype }
        pyDBui_callback.currentuser = profilename
        pyDBui_callback.currentspendingrange = currentspendingrange
        pyDBui_callback.currentplatformtype = currentplatformtype
        pyDBui_callback.users.append(addrec)
        w.Label6.config(text='''Type new username''')
        query.create_query(root)
        hide_window()
    else:
        print("name error")
        w.Label6.config(text='''name not available''')
    
def hide_window():
    # Function which hides the window.
    global top_level
    top_level.withdraw()
    

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import profile
    profile.vp_start_gui()





