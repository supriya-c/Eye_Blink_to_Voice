#!/usr/bin/env python3
"""Display a slideshow from a list of filenames"""

import os
import Tkinter
import time
from itertools import cycle
from PIL import Image, ImageTk
from twilio.rest import Client

account_sid = "AC0c7e826cedb7edf4aaa8a7ef56fa501d"
auth_token = "e0989ce732ceabe95e75647eaff97353"

client = Client(account_sid, auth_token)


class Slideshow(Tkinter.Tk):
    """Display a slideshow from a list of filenames"""
    def __init__(self, images, slide_interval):
        """Initialize
        
        images = a list of filename 
        slide_interval = milliseconds to display image
        """
        Tkinter.Tk.__init__(self)
        self.geometry("+0+0")
        self.slide_interval = slide_interval
        self.images = None
        self.set_images(images)
        
        self.slide = Tkinter.Label(self)
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
        self.set_image()
        self.slide.config(image=self.image)
        self.title(self.image_name)
        self.center()
        print(self.image_name)
        file=open("connection.txt","r")
        f= file.read()
        for line in f:
            if line == '1':
                print('Blink happened to accept the input')
                if self.image_name=="food.jpg":
                    print('Hungry')
                    client.api.account.messages.create(to="+91-7899391634",from_="+12067410072",body="Iam Hungry!!!Feed me")
                    call = client.calls.create(
                        twiml='<Response><Say>Iam Hungry!Feed me food.</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                time.sleep(2.0)
                if self.image_name=="water.jpg":
                    print('Thirsty')
                    client.api.account.messages.create(to="+91-7899391634",from_="+12067410072",body="Iam Thirsty")
                    '''call = client.calls.create(
                        twiml='<Response><Say>Iam thristy,need water</Say></Response>',
                        to='+91-7899391634', 
                        from_='+12067410072')
                    print(call.sid)'''
                time.sleep(2.0)
                if self.image_name=="snacks.jpg":
                    print('Time for Snacks')
                    client.api.account.messages.create(to="+91-7899391634",from_="+12067410072",body="I want Snacks")
                    call = client.calls.create(
                        twiml='<Response><Say>Snack time, give me chrunchy things!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                time.sleep(2.0)
                if self.image_name=="tv.jpg":
                    print(' Time for Entertainment')
                    client.api.account.messages.create(to="+91-7899391634",from_="+12067410072",body="I want to watch TV")
                    '''call = client.calls.create(
                        twiml='<Response><Say>I need to watch Television</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)'''
                time.sleep(2.0)
                if self.image_name=="call.jpg":
                    print('Make a call')
                    client.api.account.messages.create(to="+91-7899391634",from_="+12067410072",body="I want to make a call")
                    call = client.calls.create(
                        twiml='<Response><Say>I wanna make a call!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                time.sleep(2.0)
                if self.image_name=="restroom.jpg":
                    print('Want to use Restroom')
                    client.api.account.messages.create(to="+91-7899391634",from_="+12067410072",body="I want to use washroom")
                    call = client.calls.create(
                        twiml='<Response><Say>I need to pee!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                time.sleep(2.0)
                if self.image_name=="fruits.jpg":
                    print('Want fruits')
                    client.api.account.messages.create(to="+91-7899391634",from_="+12067410072",body="I want fruits")
                    call = client.calls.create(
                        twiml='<Response><Say>I want fruits!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                time.sleep(2.0)
                if self.image_name=="juice.jpg":
                    print('Want juice')
                    client.api.account.messages.create(to="+91-7899391634",from_="+12067410072",body="I want juice")
                    call = client.calls.create(
                        twiml='<Response><Say>I want juice!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                time.sleep(2.0)
                if self.image_name=="physician.jpg":
                    print('Emergency')
                    client.api.account.messages.create(to="+91-7899391634",from_="+12067410072",body="Emergency!Call the doctor")
                    call = client.calls.create(
                        twiml='<Response><Say>Its an Emergency!Please call the doctor!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                time.sleep(2.0)
            else:
                print('############')
                print(line)
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
    
    # use a list
    #images = ["image1.jpg",
              #"image2.jpeg",
              #"/home/pi/image3.gif",
              #"/home/pi/images/image4.png",
              #"images/image5.bmp"]
    
    # all the specified file types in a directory 
    # "." is the directory the script is in.
    # exts is the file extentions to use.  it can be any extention that pillow supports
    # http://pillow.readthedocs.io/en/3.3.x/handbook/image-file-formats.html
    import glob
    images = glob.glob("*.jpg")
    path = "."
    exts = ["jpg", "bmp", "png", "gif", "jpeg",'jfif']
    images = [fn for fn in os.listdir(path) if any(fn.endswith(ext) for ext in exts)]
    print(images)

    # start the slideshow
    slideshow = Slideshow(images, slide_interval)
    slideshow.start()
