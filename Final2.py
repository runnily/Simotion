import time
import board
import neopixel
import csv
import RPi.GPIO as IO
import threading

''' tk_image_slideshow3.py
create a Tkinter image repeating slide show
tested with Python27/33  by  vegaseat  03dec2013
'''
from itertools import cycle
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
    
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 24+47

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5
                           , auto_write=False,
                           pixel_order=ORDER)

#red
def set_co(x):
    #6   
    for i in range(10+47,15+47):
        pixels[i]=(x,0,0)
        
    #3
    for i in range(15+47,19+47):
        pixels[i]=(x,0,0)

#purple
def set_no(x):
    #1
    for i in range(0+47,5+47):
        pixels[i]=(x,0,x)
        
    #5
    pixels[16+47]=(x,0,x)

#green
def set_no2(x): 
    #2    
    for i in range(5+47,10+47):
        pixels[i]=(0,x,0)
    #4
    for i in range(+47,24+47):
        pixels[i]=(0,x,0)
        
        
def set_roof(x):
    for i in range(0,47):
        pixels[i]=(0,0,x)

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(19,IO.OUT)

fan=IO.PWM(19,10)
fan.start(100)

no_values=[]
with open("/home/pi/data/nitricOxide.csv") as no_file:
    csv_reader = csv.reader(no_file, delimiter=',')
    
    for row in csv_reader:
        no_values.append(float(f"{row[0]}"))

no2_values=[]
with open("/home/pi/data/nitrogenDioxide.csv") as no2_file:
    csv_reader = csv.reader(no2_file, delimiter=',')
    
    for row in csv_reader:
        no2_values.append(float(f"{row[0]}"))
        
co_values=[]
with open("/home/pi/data/carbonMonoxide.csv") as co_file:
    csv_reader = csv.reader(co_file, delimiter=',')
    
    for row in csv_reader:
        co_values.append(float(f"{row[0]}"))
        
temp_values=[]
with open("/home/pi/data/temperature.csv") as temp_file:
    csv_reader = csv.reader(temp_file, delimiter=',')
    
    for row in csv_reader:
        temp_values.append(float(f"{row[0]}"))
        
hum_values=[]
with open("/home/pi/data/relativeHumidity.csv") as hum_file:
    csv_reader = csv.reader(hum_file, delimiter=',')
    
    for row in csv_reader:
        hum_values.append(float(f"{row[0]}"))


no_min=min(no_values)
no_max=max(no_values)

no2_min=min(no2_values)
no2_max=max(no2_values)

co_min=min(co_values)
co_max=max(co_values)

temp_min=min(temp_values)
temp_max=max(temp_values)

hum_min=min(hum_values)
hum_max=max(hum_values)
    
class App(tk.Tk):
    '''Tk window/label adjusts to size of image'''
    def __init__(self, image_files, x, y, delay):
        # the root will be self
        tk.Tk.__init__(self)
        # set x, y position only
        self.geometry('800x400')
        self.delay = delay
        # allows repeat cycling through the pictures
        # store as (img_object, img_name) tuple
        # top = tk.Tk()
        previous = tk.Button(self, text = 'Play', command =self.show_slides)
        previous.config(height= 2, width=15)
        previous.place( anchor='center')
        previous.pack()
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()

    def show_slides(self):
        '''cycle through the images and show them'''
        # next works with Python26 or higher
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        # shows the image filename, but could be expanded
        # to show an associated description of the image
        self.title(img_name)
        self.after(self.delay, self.show_slides)
        #self.phrasedata()

    def run(self):
        self.mainloop()

def phrasedata():
    while True:
        for i in range(len(no_values)):
            set_no(int(10+((no_values[i]-no_min)/no_max)*244))
            set_no2(int(10+((no2_values[i]-no2_min)/no2_max)*244))
            set_co(int(10+((co_values[i]-co_min)/co_max)*244))
            set_roof(int(10+((hum_values[i]-hum_min)/hum_max)*244))
            pixels.show()
            fan.ChangeDutyCycle((temp_values[i]-temp_min)/temp_max*100)
            time.sleep(0.01)

if __name__ == '__main__':
    # set milliseconds time between slides
    delay = 3300
    # get a series of gif images you have in the working folder
    # or use full path, or set directory to where the images are
    image_files = [
        'carbonmonoxide.png',
        'nitrogendioxide.png',
        'nitricoxide.png',
        'relativehumidity.png',
        'temperature.png'
    ]

    x = 100
    y = 50

    pixels.fill((0,0,0))
    pixels.show()
    leds=threading.Thread(target=phrasedata)
    leds.start()
    app = App(image_files, x, y, delay)
    app.configure(background='white')
    app.run()
    phrasedata()

