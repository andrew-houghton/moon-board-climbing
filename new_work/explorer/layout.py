import tkinter as tk
from PIL import ImageTk
from PIL import Image


import os
import sys
import_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/types'
sys.path.append(import_path)
from climbset import Climbset


def format_image(climb_image):
    climb_image = climb_image.crop((0, 0, 11, 18))
    wpercent = (300 / float(climb_image.size[0]))
    hsize = int((float(climb_image.size[1]) * float(wpercent)))
    climb_image = climb_image.resize((300, hsize), Image.ANTIALIAS)
    return climb_image


class ClimbsetNavigator:

    def __init__(self, climbset):
        self.app_root = tk.Tk()
        self.climb_num = 0
        self.climbset = climbset

        self.top_label = tk.Label(self.app_root, text="ClimbNum")
        self.left_button = tk.Button(self.app_root, text="<-")
        self.right_button = tk.Button(self.app_root, text="->", command=self.next_image)
        self.toggle_button = tk.Button(self.app_root, text="Toggle", command=self.last_image)
        self.delete_button = tk.Button(self.app_root, text="Delete")

        self.top_label.grid(column=1, columnspan=2, padx=10, pady=10)
        self.left_button.grid(row=1, padx=10, pady=10)
        self.right_button.grid(column=3, row=1, padx=10, pady=10)
        self.toggle_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
        self.delete_button.grid(column=2, row=2, columnspan=2, padx=10, pady=10)

        self.set_image_from_index()

    def set_image_from_index(self):
        image = self.climbset.climbs[self.climb_num].as_image()
        image = format_image(image)
        image.save('current.png')
        self.img = ImageTk.PhotoImage(file='current.png')
        self.update_img()

    def update_img(self):
        self.main_image = tk.Label(self.app_root, image=self.img).grid(
            column=1, row=1, columnspan=2, padx=10, pady=10)

    def run(self):
        self.app_root.mainloop()

    def next_image(self):
        if self.climb_num < len(self.climbset.climbs) - 1:
            self.climb_num += 1
            self.set_image_from_index()
        if self.climb_num == len(self.climbset.climbs)-1:
            self.right_button.config(state=tk.DISABLED)

    def last_image(self):
        if self.climb_num > 0:
            self.climb_num += -1
            self.set_image_from_index()
        if self.climb_num == 0:
            self.left_button.config(state=ENABLED)


example_no_string = ['ChDlHnGjEr', 'JbIeDhDjCmEoBr', 'FeHhJhHkEjEmEnIhEoDqEr']
loaded_climbset = Climbset(example_no_string, 'sample')

app = ClimbsetNavigator(loaded_climbset)
app.run()
