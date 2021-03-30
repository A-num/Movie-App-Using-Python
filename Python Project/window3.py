from tkinter import*
import tkinter as tk
from PIL import Image
from PIL import ImageTk


root = tk.Tk()
root.title("Show Timings")
root.geometry("1388x880")

tk.Radiobutton(root, 
              text="Python",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=tk.W)
