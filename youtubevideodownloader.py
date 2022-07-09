import tkinter as tk
from pytube import YouTube

def Download_Video():
    url =YouTube(str(link.get()))
    video =url.streams.get_highest_resolution()
    video.download()
    tk.Label(window, text = 'Your Video is downloaded!', font = 'arial 15',fg="White",bg="#EC7063").place(x= 10 , y = 140)  


window = tk.Tk()
window.geometry("800x400")
window.resizable(width=False,height=False)
window.title('YouTube Video Downloader')
link = tk.StringVar()
 
tk.Label(window,text = 'Youtube Video Downloader', font ='arial 20 bold',fg="White",bg="Black").pack()
tk.Label(window, text = 'Paste Your YouTube Link Here:', font = 'arial 20 bold',fg="Black",bg="#EC7063").place(x= 200, y = 60)
 
link_enter = tk.Entry(window, width = 53,textvariable = link,font = 'arial 15 bold',bg="lightgreen").place(x = 120, y = 150)
 
tk.Button(window,text = 'DOWNLOAD VIDEO', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video).place(x=320 ,y = 240)
 
window.mainloop()
