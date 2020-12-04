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

import profile_callback

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    profile_callback.set_Tk_var()
    top = profile (root)
    profile_callback.init(root, top)
    root.mainloop()

w = None
def create_profile(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_profile(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    profile_callback.set_Tk_var()
    top = profile (w)
    profile_callback.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_profile():
    global w
    w.destroy()
    w = None

class profile:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+863+161")
        top.minsize(148, 1)
        top.maxsize(2564, 1415)
        top.resizable(1,  1)
        top.title("Profile Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.133, rely=0.089, height=66, width=272)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 24")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''Profile Screen''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.133, rely=0.333, height=56, width=102)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Username''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.133, rely=0.467, height=36, width=102)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''UserType''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.15, rely=0.578, height=46, width=122)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Spending Range''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.15, rely=0.711, height=46, width=112)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Platform Type''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.483, rely=0.378, height=24, relwidth=0.173)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.configure(textvariable=profile_callback.username)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.167, rely=0.844, height=33, width=56)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=profile_callback.open_query)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Apply''')

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.483, rely=0.489, relheight=0.058
                , relwidth=0.312)
        self.value_list = ['Hardcore','Casual','Mobile','Online','Observer','Armchair',]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=profile_callback.usertype)
        self.TCombobox1.configure(takefocus="")

        self.TCombobox2 = ttk.Combobox(top)
        self.TCombobox2.place(relx=0.483, rely=0.622, relheight=0.058
                , relwidth=0.312)
        self.value_list = ['*','10','20','50','100',]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(textvariable=profile_callback.spendingrange)
        self.TCombobox2.configure(takefocus="")

        self.TCombobox3 = ttk.Combobox(top)
        self.TCombobox3.place(relx=0.483, rely=0.756, relheight=0.058
                , relwidth=0.312)
        self.value_list = ['PC','Sony','Xbox','Switch','Phone',]
        self.TCombobox3.configure(values=self.value_list)
        self.TCombobox3.configure(textvariable=profile_callback.platformtype)
        self.TCombobox3.configure(takefocus="")

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.15, rely=0.222, height=56, width=232)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Type username and combo box''')

if __name__ == '__main__':
    vp_start_gui()





