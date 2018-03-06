from PIL import ImageTk
import tkinter as tk

app_root = tk.Tk()

img = ImageTk.PhotoImage(file='temp.png')

top_label = tk.Label(app_root,text = "ClimbNum").grid(column=1,columnspan=2, padx=10,pady=10)
top_label = tk.Button(app_root,text = "<-").grid(row=1, padx=10,pady=10)
top_label = tk.Button(app_root,text = "->").grid(column=3,row=1, padx=10,pady=10)
top_label = tk.Label(app_root,image = img).grid(column=1,row=1,columnspan=2, padx=10,pady=10)
top_label = tk.Button(app_root,text = "Toggle").grid(column=0,row=2,columnspan=2, padx=10,pady=10)
top_label = tk.Button(app_root,text = "Delete").grid(column=2,row=2,columnspan=2, padx=10,pady=10)

app_root.mainloop()