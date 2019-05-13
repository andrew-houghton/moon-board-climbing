import os
import sys
import tkinter

from PIL import Image, ImageTk

from climb import Climb

import_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/types"
sys.path.append(import_path)


example_climb_info = {
    "Grade": "8A",
    "UserRating": 0,
    "Moves": ["G2", "J7", "J8", "D8", "D10", "A5", "A13", "F6", "D16", "C18"],
}
example_climb = Climb("json", example_climb_info)

climb_image = example_climb.as_image()
climb_image = climb_image.crop((0, 0, 11, 18))

basewidth = 300
wpercent = basewidth / float(climb_image.size[0])
hsize = int((float(climb_image.size[1]) * float(wpercent)))
climb_image = climb_image.resize((basewidth, hsize), Image.ANTIALIAS)
climb_image.save("temp.png")

app_root = tkinter.Tk()

# Setting it up
img = ImageTk.PhotoImage(file="temp.png")

# Displaying it
imglabel = tkinter.Label(app_root, image=img).grid(row=1, column=1)

app_root.mainloop()
