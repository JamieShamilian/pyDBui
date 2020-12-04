#! /usr/bin/env python


import sys

import requests
import json
import csv

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
    global gamelist
    gamelist = tk.StringVar()
    global daterange
    daterange = tk.StringVar()
    global costrange
    costrange = tk.StringVar()
    global gameplatform
    gameplatform = tk.StringVar()
    global gametype
    gametype = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    daterange.set("*")
    spend = pyDBui_callback.currentspendingrange
    costrange.set(spend)
    #print(costrange);
    platform = pyDBui_callback.currentplatformtype
    gameplatform.set(platform)
    print('query_callback init ')
    print(platform+spend)
    gametype.set("*")

# use postman access token good for 60 days
#https://id.twitch.tv/oauth2/token?client_id=abcdefg12345&client_secret=hijklmn67890&grant_type=client_credentials

game1list = "game1 2\rgame2 g22\rgame3\ngame1\ngame2\ngame3\ngame1\ngame2\ngame3\ngame1\ngame2\ngame3\n"

from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult

def start_query():
    #print('query_callback.start_query')
    gamelist.set("")
    sys.stdout.flush()
    limit = 30   
    platform = gameplatform.get()
    if platform == 'Xbox':
        platformnum = 49
    if platform == 'Sony':
        platformnum = 48
    if platform == 'Switch':
        platformnum = 130
    if platform == 'Phone':
        platformnum = 34
    if platform == 'PC':
        platformnum = 6          
    if platform == "*":
        query = "fields name; limit 30; "
    else:
        query = "fields name; where platforms = " + str(platformnum) + "; limit "+ str(limit) + "; "
    #
    # 48 - PS4, 49 - Xbox one, 130 - switch, 34 - android , 39 - ios , windows - 6
    #
    # token good for 60 days.
    wrapper = IGDBWrapper("ab149we1sss225z73u22uknald6tkx","oeliv17vvkt778iesj0n7m3kvo807t")
    byte_array = wrapper.api_request(
            'games',
            query
            )
    #print(type(byte_array))
    #print(byte_array)
    jdata = json.loads(byte_array)
        
    #rtnlist = ""
    #for i in range(0,limit) :
    #    rtnlist += ( jdata[i]['name'] +"\n" ) 
    #print (rtnlist)
        
    for i in range(0,limit) :
        w.Scrolledlistbox1.insert(i+1,jdata[i]['name'])
   
    #data = json.dumps(jdata)
    #print(type(data))
    #print(data)
    #games_message = GameResult()
    #
    #   bug in google protobuf code/config
    #  
    #games_message.ParseFromString(byte_array) # Fills the protobuf message object with the response

    

def stop_query():
    global top_level
    print('query_callback.stop_query')
    #top_level.deiconify()
    pyDBui_callback.show_window()
    hide_window()
    sys.stdout.flush()

def hide_window():
    # Function which closes the window.
    global top_level
    top_level.withdraw()

import pyDBui_callback

def exitall():
    print('query_callback.exitall')
    sys.stdout.flush()
    pyDBui_callback.destroy_window()

def destroy_window():
    # Function which closes the window.
    global top_level
    pyDBui_callback.destroy_window()
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import query
    query.vp_start_gui()





