import tkinter as tk

root = tk.Tk(screenName="My First TKinter")
root.title("Hello World 🌍")

my_first_label = tk.Label(root, text= "Hello World!")
my_first_label.pack()

root.mainloop()