import tkinter as tk
import fnmatch
import os
from pygame import mixer


canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry('800x800')
canvas.config(bg = 'black')

rootpath= "D:\\Intern Projects\music player\music files"
pattern = "*.mp3"

mixer.init()

def select():
    label.config(text= listBox.get('anchor'))
    mixer.music.load(rootpath + "\\" + listBox.get('anchor'))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0]+ 1
    next_song_name = listBox.get (next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0]-1
    next_song_name = listBox.get (next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pauseButton['text'] == "pause":
        mixer.music.pause()
        pauseButton['text']= "continue"
    else:
        mixer.music.unpause()
        pauseButton["text"] = 'pause'

listBox= tk.Listbox(canvas, fg = 'green' , bg = 'yellow' , width= 100 , font = ('MAKISUPA' , 20))
listBox.pack(padx= 15 , pady= 15)

label=tk.Label(canvas, text = '',bg='black',fg='green',font= ('MAKISUPA' , 20))
label.pack(pady=15)

top=tk.Frame(canvas,bg ='black')
top.pack(padx=10,pady=5,anchor = 'center')

prevButton = tk.Button(canvas,text="previous" , command= play_prev,bg = 'blue')
prevButton.pack(pady=15, in_ = top ,side ='left')

pauseButton = tk.Button(canvas,text="Pause", command= pause_song , bg ='grey')
pauseButton.pack(pady=15, in_ = top ,side ='left')

playButton = tk.Button(canvas,text="Play",command= select)
playButton.pack(pady=15, in_ = top ,side ='left')

stopButton = tk.Button(canvas,text="Stop",command= stop,bg = "red")
stopButton.pack(pady=15, in_ = top ,side ='left')

nextButton = tk.Button(canvas,text="Next",command= play_next,bg = "blue")
nextButton.pack(pady=15, in_ = top ,side ='left')

for root,dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)

canvas.mainloop()
