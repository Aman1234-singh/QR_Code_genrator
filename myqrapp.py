#Common Logic Starts
from tkinter import *
from tkinter.ttk import * #Optional - To support modern Theme/UI

#Step I: Define ADT/Class
class QRGUI:
    #Constructor - Parameterized Constructor
    def __init__(self,window):  #Parameterized Constructor [CwB]
        self.window = window    #self - instance/object of class (C++/Java: this)
        window.title("TecDev QR App")

        self.label = Label(window, text="Enter String to generate QR Code")
        self.label.pack() #Grid Sytem or Pack System
        self.inputstring=StringVar()
        self.txtString=Entry(window, width=100, textvariable=self.inputstring)
        self.txtString.pack()
        self.button = Button(window, text="Generate QR Code", command=self.generateClick)
        self.button.pack()

        self.close_button = Button(window, text="Close", command=self.window.quit)
        self.close_button.pack()
     #CwB - Properties of OOPS -Encapsulation
    def generateClick(self):
        #Code to generate QRCode [Based on 29-May]
        import pyqrcode 
        import png 
        from pyqrcode import QRCode   #QRCode is a class
        from PIL import Image, ImageTk         #Python Image Library

        # String which represents the QR code 
        string = self.inputstring.get()

        # Generate QR code 
        url = pyqrcode.create(string)
        #Dynamically generate filename based on input String
        filename1=string + ".svg" #Scalable Vector Graphics
        filename2=string + ".png" #Portable Network Graphics
        # Create and save the svg file naming "myqr.svg" 
        url.svg(filename1, scale = 8)  #Creates svg file

        # Create and save the png file naming "myqr.png" 
        url.png(filename2, scale = 6) #Creates png file
        canvas1 = Canvas(self.window, width = 300, height = 300)  
        canvas1.pack()
        #Using ImageTk class to Open Photo with given filename
        img = ImageTk.PhotoImage(Image.open(filename2))
        #Imp: To draw image on canvas use create_image fn
        canvas1.create_image(20, 20, anchor=NW, image=img) #x,y
        #window.mainloop()
        #self.window.update()
        self.window.mainloop()

#Program Execution Entry Point
def main():         #CwB - Creating Main Fn in Python
    window = Tk()       #Creating Object of Tk 
    ui = QRGUI(window)   #Step II Calling PC and passing window object
    window.mainloop()

if __name__=="__main__":
    main()      # Program Entry Point
