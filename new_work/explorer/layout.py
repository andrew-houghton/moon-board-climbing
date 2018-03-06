from PIL import ImageTk
import tkinter as tk


class ClimbsetNavigator:

    def __init__(self):
        self.app_root = tk.Tk()

        self.img = ImageTk.PhotoImage(file='temp.png')

        
        top_label = tk.Label(self.app_root, text="ClimbNum").grid(
            column=1, columnspan=2, padx=10, pady=10)
        
        left_button = tk.Button(self.app_root, text="<-").grid(
            row=1, padx=10, pady=10)
        
        right_button = tk.Button(self.app_root, text="->").grid(
            column=3, row=1, padx=10, pady=10)
        
        main_image = tk.Label(self.app_root, image=self.img).grid(
            column=1, row=1, columnspan=2, padx=10, pady=10)
        
        toggle_overlay = tk.Button(self.app_root, text="Toggle").grid(
            column=0, row=2, columnspan=2, padx=10, pady=10)
        
        delete_button = tk.Button(self.app_root, text="Delete").grid(
            column=2, row=2, columnspan=2, padx=10, pady=10)

    def run(self):
        self.app_root.mainloop()


app = ClimbsetNavigator()
app.run()