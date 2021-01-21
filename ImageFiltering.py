from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import cv2 as cv
 
class Filtering:
    WIDTH,HEIGHT=400,320
    img=''

    def __init__(self, master):
        master.title("Praying to God")
        master.geometry("400x320") # set starting size of window
        master.configure(bg='#353b48')
        master.resizable(False, False)
        self.label=Label(master, text='Image Processing', bg='#353b48', font =('Vendana', 15)).pack(side = TOP, pady = 10)
        self.lbl=Label(master, text='Source File', bg='#353b48').pack()
        self.ent=Entry(master, textvariable=t1).pack()
        self.btnBrowse=Button(master, text='Browse', bg='#353b48' , command=self.browseimg).pack(pady=10)
        self.btnPreviewImage=Button(master, text='Preview', command=self.previewimg).pack(pady=10)
        self.btnFilter=Button(master, text='Filter', bg='#353b48' , command=self.Filter).pack(pady=10)
        self.R1=Radiobutton(master, text='3x3', variable=t2, value=3).place(x=125, y=220)
        self.R1=Radiobutton(master, text='5x5', variable=t2, value=5).place(x=125+50, y=220)
        self.R1=Radiobutton(master, text='7x7', variable=t2, value=7).place(x=125+100, y=220)


    def browseimg(self):
        global img
        self.fln=filedialog.askopenfilename(initialdir=os.getcwd(), title='Browse Image File', filetypes=(('JPG Image', '*.jpg'), ('PNG Image', '*.png'), ('All Files', '*.*')))
        t1.set(self.fln)
        img=self.fln
    def previewimg(self):
        self.read=cv.imread(img, cv.IMREAD_UNCHANGED)
        cv.imshow('Source Image', self.read)
        cv.waitKey(0)
    def Filter(self):
        self.read=cv.imread(img)
        self.blur=cv.GaussianBlur(self.read, (t2.get(), t2.get()), cv.BORDER_DEFAULT)
        cv.imshow('Filtering Image', self.blur)
        cv.waitKey(0)
    def saveFilteredImage(self):
        self.fln=filedialog.askopenfilename(initialdir=os.getcwd(), title='Browse Image File', filetypes=(('JPG Image', '*.jpg'), ('PNG Image', '*.png'), ('All Files', '*.*')))


root=Tk()
t1=StringVar()
t2=IntVar()
filter=Filtering(root)
root.mainloop()

