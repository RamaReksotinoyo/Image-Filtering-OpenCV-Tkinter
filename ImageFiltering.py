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

# from tkinter import *
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import os
# import cv2 as cv
 
# root = Tk()
# root.title("Praying to God")
# root.geometry("400x320") # set starting size of window
# root.configure(bg='#353b48')
# root.resizable(False, False)

# label=Label(root, text='Image Processing', bg='#353b48', font =('Vendana', 15)).pack(side = TOP, pady = 10)

# img=''
# def browseimg():
#     global img
#     fln=filedialog.askopenfilename(initialdir=os.getcwd(), title='Browse Image File', filetypes=(('JPG Image', '*.jpg'), ('PNG Image', '*.png'), ('All Files', '*.*')))
#     t1.set(fln)
#     img=fln
# def previewimg():
#     read=cv.imread(img, cv.IMREAD_UNCHANGED)
#     cv.imshow('Source Image', read)
#     cv.waitKey(0)

# def Filter():
#     read=cv.imread(img)
#     blur=cv.GaussianBlur(read, (t2.get(), t2.get()), cv.BORDER_DEFAULT)
#     cv.imshow('Filtering Image', blur)
#     cv.waitKey(0)

# def saveFilteredImage():
#     fln=filedialog.askopenfilename(initialdir=os.getcwd(), title='Browse Image File', filetypes=(('JPG Image', '*.jpg'), ('PNG Image', '*.png'), ('All Files', '*.*')))


# t1=StringVar()
# t2=IntVar()

# lbl=Label(root, text='Source File', bg='#353b48').pack()
# ent=Entry(root, textvariable=t1).pack()
# btnBrowse=Button(root, text='Browse', bg='#353b48' , command=browseimg).pack(pady=10)
# btnPreviewImage=Button(root, text='Preview', command=previewimg).pack(pady=10)
# btnFilter=Button(root, text='Filter', bg='#353b48' , command=Filter).pack(pady=10)

# R1=Radiobutton(root, text='3x3', variable=t2, value=3).place(x=125, y=220)
# R1=Radiobutton(root, text='5x5', variable=t2, value=5).place(x=125+50, y=220)
# R1=Radiobutton(root, text='7x7', variable=t2, value=7).place(x=125+100, y=220)

# # for kernel, val in value:
# #     R1=Radiobutton(root, text=kernel, variable=t2, value=val).pack()

# root.mainloop()
