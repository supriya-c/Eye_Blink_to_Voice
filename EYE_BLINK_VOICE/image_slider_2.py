"""Display a slideshow from a list of filenames"""

import os
import tkinter

from itertools import cycle
from PIL import Image, ImageTk
from twilio.rest import Client


class Slideshow(tkinter.Tk):
     
    """Display a slideshow from a list of filenames"""
    def __init__(self, images, slide_interval):
        """Initialize
        
        images = a list of filename 
        slide_interval = milliseconds to display image
        """
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
        """Center the slide window on the screen"""
        self.update_idletasks()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        self.geometry("+%d+%d" % (x, y))

    def set_image(self):
        """Setup image to be displayed"""
        self.image_name = next(self.images)
        filename, ext = os.path.splitext(self.image_name)
        self.image = ImageTk.PhotoImage(Image.open(self.image_name))
        
    def main(self):
        """Display the images"""
        global flag
        self.set_image()
        self.slide.config(image=self.image)
        self.center()
        print(self.image_name)
        file=open("connection.txt","r")
        f= file.read()
        for line in f:
            if line == '1':
                if self.image_name=="food.jpg":
                    print('Blink happened to accept the input')
                    flag=1
                if self.image_name=="water.jpg":
                    print('Blink happened to accept the input')
                    flag=2
                if self.image_name=="snacks.jpg":
                    print('Blink happened to accept the input')
                    flag=3
                if self.image_name=="tv.jpg":
                    print('Blink happened to accept the input')
                    flag=4
                if self.image_name=="call.jpg":
                    print('Blink happened to accept the input')
                    flag=5
                if self.image_name=="restroom.jpg":
                    print('Blink happened to accept the input')
                    flag=6
                if self.image_name=="coffee.png":
                    print('Blink happened to accept the input')
                    flag=7
                if self.image_name=="milk.png":
                    print('Blink happened to accept the input')
                    flag=8
                if self.image_name=="fruits.jpg":
                    print('Blink happened to accept the input')
                    flag=9
                if self.image_name=="juice.jpg":
                    print('Blink happened to accept the input')
                    flag=10
                if self.image_name=="physician.jpg":
                    print('Blink happened to accept the input')
                    flag=11
                if self.image_name=="yes.jpg":
                    print(flag)
                    if flag==1:
                        print("I'm hungry, need food")
                    if flag==2:
                        print("I'm thristy, need some water")
                    if flag==3:
                        print("i need snacks")
                    if flag==4:
                        print("i wanna watch Tv")
                    if flag==5:
                        print("i wanna make a call")
                    if flag==6:
                        print("i need to pee")
                    if flag==7:
                        print("i need coffee")
                    if flag==8:
                        print("i wanna drink milk")
                    if flag==9:
                        print("i want some fruits")
                    if flag==10:
                        print("i want some juice ")
                    if flag==11:
                        print("It's an emergency")                    
                
            else:
                print('############')
                
        file.close()
        file=open("connection.txt","w")
        file.write('0')
        file.close()
        
        self.after(self.slide_interval, self.start)
    
    def start(self):
        """Start method"""
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

    # start the slideshow
    slideshow = Slideshow(images, slide_interval)
    slideshow.start()
