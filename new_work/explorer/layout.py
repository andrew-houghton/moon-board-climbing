import tkinter as tk
from PIL import ImageTk
from PIL import Image


import os
import sys
import_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/types'
sys.path.append(import_path)
from climbset import Climbset



def format_image(climb_image):
    climb_image = climb_image.crop((0,0,11,18))
    wpercent = (300/float(climb_image.size[0]))
    hsize = int((float(climb_image.size[1])*float(wpercent)))
    climb_image = climb_image.resize((300,hsize), Image.ANTIALIAS)
    return climb_image

class ClimbsetNavigator:

    def __init__(self, climbset):
        self.app_root = tk.Tk()
        self.climb_num = 0
        self.climbset = climbset
        
        top_label = tk.Label(self.app_root, text="ClimbNum").grid(
            column=1, columnspan=2, padx=10, pady=10)
        left_button = tk.Button(self.app_root, text="<-").grid(
            row=1, padx=10, pady=10)
        right_button = tk.Button(self.app_root, text="->").grid(
            column=3, row=1, padx=10, pady=10)
        toggle_overlay = tk.Button(self.app_root, text="Toggle").grid(
            column=0, row=2, columnspan=2, padx=10, pady=10)
        delete_button = tk.Button(self.app_root, text="Delete").grid(
            column=2, row=2, columnspan=2, padx=10, pady=10)

        self.set_image_from_index(0)

    def set_image_from_index(self,index):
        image = self.climbset.climbs[index].as_image()
        image = format_image(image)
        image.save('current.png')
        self.img = ImageTk.PhotoImage(file='current.png')
        self.update_img()

    def update_img(self):
        main_image = tk.Label(self.app_root, image=self.img).grid(
            column=1, row=1, columnspan=2, padx=10, pady=10)

    def run(self):
        self.app_root.mainloop()

example_no_string = ['ChDlHnGjEr', 'JbIeDhDjCmEoBr', 'FeHhJhHkEjEmEnIhEoDqEr']
loaded_climbset = Climbset(example_no_string, 'sample')

app = ClimbsetNavigator(loaded_climbset)
app.run()