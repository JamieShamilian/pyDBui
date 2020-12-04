#! /usr/bin/env python


import sys

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

import pyDBui_callback

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    pyDBui_callback.set_Tk_var()
    top = pyDBui (root)
    pyDBui_callback.init(root, top)
    root.mainloop()

w = None
def create_pyDBui(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_pyDBui(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    pyDBui_callback.set_Tk_var()
    top = pyDBui (w)
    pyDBui_callback.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_pyDBui():
    global w
    w.destroy()
    w = None

class pyDBui:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+128+165")
        top.minsize(148, 1)
        top.maxsize(2564, 1415)
        top.resizable(1,  1)
        top.title("pyDBui Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.183, rely=0.378, height=53, width=186)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=pyDBui_callback.open_profile)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Create a username''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.183, rely=0.556, height=53, width=186)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=pyDBui_callback.open_query)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Sign In with Username''')

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.183, rely=0.733, height=53, width=186)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=pyDBui_callback.open_query_guest)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Sign in As Guest''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.1, rely=0.067, height=66, width=402)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 24")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''pyDBui Login Screen''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.567, rely=0.578, height=34, relwidth=0.257)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.configure(textvariable=pyDBui_callback.username)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.2, rely=0.244, height=36, width=152)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''choose a login option''')

if __name__ == '__main__':
    vp_start_gui()





