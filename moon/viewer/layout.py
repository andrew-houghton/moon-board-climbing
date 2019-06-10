import os
import sys
import tkinter as tk

from PIL import Image, ImageTk

from climbset import Climbset

import_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/types"
sys.path.append(import_path)


base_image = Image.open(os.path.dirname(os.path.realpath(__file__)) + "/cleaned.png")


def fix_transparency(climb_image):
    climb_image = climb_image.convert("RGBA")
    datas = climb_image.getdata()

    # Deals one by one with pixels
    # Black goes to transparent
    # White goes to semi transparent black
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((0, 0, 0, 100))
        else:
            newData.append((0, 0, 0, 0))
    climb_image.putdata(newData)
    return climb_image


def format_image(climb_image):
    # Crop the climb
    climb_image = climb_image.crop((0, 0, 11, 18))
    # Resize to match background
    climb_image = climb_image.resize((540, 900), Image.ANTIALIAS)
    # Convert holds to transparent regions
    climb_image = fix_transparency(climb_image)
    # Paste holds onto large transparent canvas (which matches the background size)
    blank = Image.new("RGBA", (650, 1000))
    blank.paste(climb_image, (75, 65))
    # Paste transparent holds onto background
    joined_image = Image.alpha_composite(base_image, blank)

    # return joined_image
    # Finally scale for display
    return joined_image.resize((400, 615), Image.ANTIALIAS)


class ClimbsetNavigator:
    def __init__(self, climbset):
        self.app_root = tk.Tk()
        # Create the variables for managing the display
        self.climb_num = 0
        self.overlay_visible = True
        self.climbset = climbset

        # Bind keypress events
        self.app_root.bind("<Left>", self.left_event)
        self.app_root.bind("<Right>", self.right_event)
        self.app_root.bind("<Escape>", self.close_window)
        self.app_root.bind("<Delete>", self.delete_event)

        # Create the display elements
        self.top_label = tk.Label(
            self.app_root, text="Image 1 of {}".format(len(self.climbset.climbs))
        )
        self.grade_label = tk.Label(self.app_root, text="Grade: ")
        self.left_button = tk.Button(self.app_root, text="<-", command=self.last_image)
        self.right_button = tk.Button(self.app_root, text="->", command=self.next_image)
        self.toggle_button = tk.Button(self.app_root, text="Toggle", command=self.toggle_overlay)
        self.delete_button = tk.Button(self.app_root, text="Delete", command=self.delete_current)
        self.save_button = tk.Button(self.app_root, text="Save Climbs", command=self.save_all)
        self.main_image = tk.Label(self.app_root)

        # Manage the layout
        self.top_label.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

        self.grade_label.grid(column=3, row=0, columnspan=2, padx=10, pady=10)

        self.left_button.grid(column=0, row=1, padx=10, pady=10)
        self.right_button.grid(column=4, row=1, padx=10, pady=10)

        self.toggle_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
        self.delete_button.grid(column=2, row=2, padx=10, pady=10)
        self.save_button.grid(column=3, row=2, columnspan=2, padx=10, pady=10)

        self.main_image.grid(column=1, row=1, columnspan=3, padx=10, pady=10)

        # Manage the initial state of buttons
        self.left_button.config(state=tk.DISABLED)
        if len(self.climbset.climbs) == 1:
            self.right_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)

        self.set_image_from_index()

    def left_event(self, event):
        self.last_image()

    def right_event(self, event):
        self.next_image()

    def close_window(self, event):
        self.app_root.withdraw()

    def delete_event(self, event):
        self.delete_current()

    def save_all(self):
        from pathlib import Path
        import pickle

        save_dir = str(Path().resolve().parent) + "/data/climbsets/"
        save_name = "climbs.pkl"
        with open(save_dir + save_name, "wb") as handle:
            pickle.dump(self.climbset, handle)

    def delete_current(self):
        if len(self.climbset.climbs) > 1:
            self.climbset.climbs.pop(self.climb_num)
            if self.climb_num == 0:
                self.process_image_change()
            else:
                self.last_image()

        if len(self.climbset.climbs) <= 1:
            self.delete_button.config(state=tk.DISABLED)

    def toggle_overlay(self):
        self.overlay_visible = not self.overlay_visible

    def set_image_from_index(self):
        # Change the image which is displayed to match the index
        image = self.climbset.climbs[self.climb_num].as_image()
        image = format_image(image)
        image.save("current.png")
        self.img = ImageTk.PhotoImage(file="current.png")
        self.main_image.configure(image=self.img)

        climb = self.climbset.climbs[self.climb_num]
        self.grade_label.configure(text=f"Grade: {climb.grade} - {climb.grade.grade_number}")

    def run(self):
        # Show the app
        self.app_root.mainloop()

    def next_image(self):
        # Move to next image
        if self.climb_num < len(self.climbset.climbs) - 1:
            self.climb_num += 1
            self.process_image_change()

    def last_image(self):
        # Move to previous image
        if self.climb_num > 0:
            self.climb_num += -1
            self.process_image_change()

    def process_image_change(self):
        self.set_image_from_index()
        self.update_view_state()

    def update_view_state(self):
        # Check that the title at the top and the left and right buttons are in the correct state
        self.top_label.configure(
            text="Image {} of {}".format(self.climb_num + 1, len(self.climbset.climbs))
        )

        if self.climb_num == 0:
            self.left_button.config(state=tk.DISABLED)
        elif self.climb_num >= 1:
            self.left_button.config(state=tk.NORMAL)

        if self.climb_num == len(self.climbset.climbs) - 1:
            self.right_button.config(state=tk.DISABLED)
        elif self.climb_num <= len(self.climbset.climbs):
            self.right_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    example_no_string = ["ChDlHnGjEr", "JbIeDhDjCmEoBr", "FeHhJhHkEjEmEnIhEoDqEr"]
    loaded_climbset = Climbset(example_no_string, "sample")

    app = ClimbsetNavigator(loaded_climbset)
    app.run()
