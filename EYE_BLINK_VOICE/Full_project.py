#!/usr/bin/env python3
"""Display a slideshow from a list of filenames"""
#for python3 and above version "import tkinter"
import os
import Tkinter

from itertools import cycle
from PIL import Image, ImageTk
from twilio.rest import Client

account_sid = "TWILIO_ACCOUNT_SID"
auth_token = "TWILIO_AUTH_TOKEN"
client = Client(account_sid, auth_token)


class Slideshow(Tkinter.Tk):
    
    def __init__(self, images, slide_interval):
        
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
                if self.image_name=="curdrice.jpg":
                    print('Blink happened to accept the input')
                    flag=12
                if self.image_name=="idli.png":
                    print('Blink happened to accept the input')
                    flag=13
                if self.image_name=="ragi_malt.png":
                    print('Blink happened to accept the input')
                    flag=14
                if self.image_name=="khichdi.png":
                    print('Blink happened to accept the input')
                    flag=15
                if self.image_name=="yes.jpg":
                    if flag==1:
                        print("I'm hungry, need food")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="Iam Hungry!!!Feed me")
                    call = client.calls.create(
                        twiml='<Response><Say>Iam Hungry!Feed me food.</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==2:
                        print("I'm thristy, need some water")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="Iam Thirsty")
                    call = client.calls.create(
                        twiml='<Response><Say>Iam thristy,need water</Say></Response>',
                        to='+91-7899391634', 
                        from_='+12067410072')
                    print(call.sid)
                    if flag==3:
                        print("I need snacks")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want Snacks")
                    call = client.calls.create(
                        twiml='<Response><Say>Snack time, give me chrunchy things!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==4:
                        print("I wanna watch TV")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want to watch TV")
                    call = client.calls.create(
                        twiml='<Response><Say>I need to watch Television</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==5:
                        print("I wanna make a call")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want to make a call")
                    call = client.calls.create(
                        twiml='<Response><Say>I wanna make a call!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==6:
                        print("I need to pee")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want to use washroom")
                    call = client.calls.create(
                        twiml='<Response><Say>I need to pee!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==7:
                        print("I need coffee")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want to drink coffee or tea")
                    call = client.calls.create(
                        twiml='<Response><Say>I want to drink coffee or tea</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                   print(call.sid)
                    if flag==8:
                        print("I wanna drink milk")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want to drink milk")
                    call = client.calls.create(
                        twiml='<Response><Say>I want to drink milk</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==9:
                        print("I want some fruits")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want fruits")
                    call = client.calls.create(
                        twiml='<Response><Say>I want fruits!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==10:
                        print("I want some juice")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want juice")
                    call = client.calls.create(
                        twiml='<Response><Say>I want juice!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==11:
                        print("It's an emergency")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="Emergency!Call the doctor")
                    call = client.calls.create(
                        twiml='<Response><Say>Its an Emergency!Please call the doctor!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==12:
                        print("I want curd rice")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want curdrice to eat")
                    call = client.calls.create(
                        twiml='<Response><Say>Its an Emergency!Please call the doctor!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==13:
                        print("I want idli sambar")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want idli sambar to eat")
                    call = client.calls.create(
                        twiml='<Response><Say>I want idli sambar to eat!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==14:
                        print("I want ragi malt")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want ragi malt")
                    call = client.calls.create(
                        twiml='<Response><Say>I want ragi malt!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
                    if flag==15:
                        print("I want khichdi to eat")
                        client.api.account.messages.create(to="CONTACT_NO",from_="TWILIO_NO",body="I want khichdi to eat")
                    call = client.calls.create(
                        twiml='<Response><Say>I want khichdi to eat!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072')
                    print(call.sid)
      
        else:
                print('############')
                
        file.close()
        file=open("connection.txt","w")
        file.write('0')
        file.close()
        
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

    # start the slideshow
    slideshow = Slideshow(images, slide_interval)
    slideshow.start()
