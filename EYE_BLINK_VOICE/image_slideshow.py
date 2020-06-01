#!/usr/bin/env python3
"""Display a slideshow from a list of filenames"""

import os
import tkinter

from itertools import cycle
from PIL import Image, ImageTk
from twilio.rest import Client

class Slideshow(tkinter.Tk):
    
    def __init__(self, images, slide_interval):
        
        tkinter.Tk.__init__(self)
        self.geometry("+0+0")
        self.slide_interval = slide_interval
        self.images = None
        self.set_images(images)
        
        self.slide = tkinter.Label(self)
        self.slide.pack()

    def set_images(self, images):
         self.images = cycle(images)


    def center(self):
        
        self.update_idletasks()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        self.geometry("+%d+%d" % (x, y))

    def set_image(self):
       
        self.image_name = next(self.images)
        filename, ext = os.path.splitext(self.image_name)
        self.image = ImageTk.PhotoImage(Image.open(self.image_name))
        
        
    def main(self):
       
        global flag
        self.set_image()
        self.slide.config(image=self.image)
        self.title(self.image_name)
        self.center()
        print(self.image_name)
        self.after(self.slide_interval, self.start)
    
    def start(self):
        self.main()
        self.mainloop()


if __name__ == "__main__":
    slide_interval = 3500
    import glob
    images = glob.glob("*.jpg")
    path = "."
    exts = ["jpg", "bmp", "png", "gif", "jpeg",'jfif']
    images = [fn for fn in os.listdir(path) if any(fn.endswith(ext) for ext in exts)]
    print(images)

   
    slideshow = Slideshow(images, slide_interval)
    slideshow.start()
