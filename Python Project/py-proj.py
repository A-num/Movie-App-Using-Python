from tkinter import*
import tkinter as tk
from PIL import Image
from PIL import ImageTk


top = tk.Tk()
top.title("Show Timings")
top.geometry("1388x880")

#image background
cwgt=tk.Canvas(top)
cwgt.pack(expand=True, fill=tk.BOTH)
background_image=ImageTk.PhotoImage(file="CinemaBackground.jpg")
cwgt.img=background_image
cwgt.create_image(0,0, anchor=tk.NW, image=background_image)
ImageTk.PhotoImage(file="CinemaBackground.jpg")

#label


#buttons

#b1
def morning():
    f1=tk.Frame(top)
    f1.propagate(0)
    f1.pack()
    window=tk.Toplevel(f1)
    window.configure(bg="white")
    window.geometry("800x500")
    window.title("Movies")
    bm=tk.Button(window,text="Black Panther",bg="white", fg="black",cursor='watch').place(x=300,y=50,width=200,height=40)
    bm=tk.Button(window,text="3 Idiots",bg="white", fg="black",cursor='watch').place(x=300,y=200,width=200,height=40)
    bm=tk.Button(window,text="Shawshank Redemption",bg="white", fg="black",cursor='watch').place(x=300,y=350,width=200,height=40)
    
b1=tk.Button(top,text="Morning",bg="white", fg="black",cursor='watch', command=morning).place(x=600,y=100,width=200,height=40)

#b2
def afternoon():
    f2=tk.Frame(top)
    f2.propagate(0)
    f2.pack()
    window=tk.Toplevel(f2)
    window.configure(bg="white")
    window.geometry("800x500")
    window.title("Movies")
    bm=tk.Button(window,text="Batman",bg="white", fg="black",cursor='watch').place(x=300,y=40,width=200,height=40)
    bm=tk.Button(window,text="Wonder Woman",bg="white", fg="black",cursor='watch').place(x=300,y=200,width=200,height=40)
    bm=tk.Button(window,text="Inception",bg="white", fg="black",cursor='watch').place(x=300,y=350,width=200,height=40)
b2=tk.Button(top,text="Afternoon",bg="white", fg="black",cursor='watch', command=afternoon).place(x=600,y=200,width=200,height=40)

#b3
def evening():
    f3=tk.Frame(top)
    f3.propagate(0)
    f3.pack()
    window=tk.Toplevel(f3)
    window.configure(bg="white")
    window.geometry("800x500")
    window.title("Movies")
    bm=tk.Button(window,text="Intestellar",bg="white", fg="black",cursor='watch').place(x=300,y=200,width=200,height=40)
    bm=tk.Button(window,text="Forrest Gump",bg="white", fg="black",cursor='watch').place(x=300,y=350,width=200,height=40)
    bm=tk.Button(window,text="Black Panther",bg="white", fg="black",cursor='watch').place(x=300,y=40,width=200,height=40)
b3=tk.Button(top,text="Evening",bg="white", fg="black",cursor='watch', command=evening).place(x=600,y=300,width=200,height=40)

#b4
def night():
    f4=tk.Frame(top)
    f4.propagate(0)
    f4.pack()
    window=tk.Toplevel(f4)
    window.configure(bg="white")
    window.geometry("800x500")
    window.title("Movies")
    bm=tk.Button(window,text="The Prestige",bg="white", fg="black",cursor='watch').place(x=300,y=40,width=200,height=40)
    bm=tk.Button(window,text="Fight Club",bg="white", fg="black",cursor='watch').place(x=300,y=200,width=200,height=40)
    bm=tk.Button(window,text="A Beautiful Mind",bg="white", fg="black",cursor='watch').place(x=300,y=350,width=200,height=40)
b4=tk.Button(top,text="Night",bg="white", fg="black",cursor='watch', command=night).place(x=600,y=400,width=200,height=40)

top.mainloop()
