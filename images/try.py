from tkinter import *
# from tkinter import tk
# import tkinter as tk
root= Tk()
root.geometry("1520x780+0+0")
frame=Frame(root,bg="#ffffff")

l=["pizza","mic","ee"]

for i in l:
    m=Label(root,text=i)
    m.place(x=3,y=0)
    b=Button(root,text="-")
    b.place(x=0,y=0)
