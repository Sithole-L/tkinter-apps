import tkinter as tk
import tkinter.font as tkFont #enables printing all available font families so you can pick one to use


root = tk.Tk(screenName="My First TKinter")
#print(tkFont.families())

root.title("Hello World 🌍")
root.geometry("400x400")
root.configure(bg="light steel blue")

my_first_label = tk.Label(root, text= "Hello World!", font=('Segoe Script', 18), bg="light steel blue")
my_first_label.pack()

my_english_btn = tk.Button(root, text="English 🇬🇧", font=('Segoe Script', 18), bg="steel blue")
my_english_btn.pack(pady=20)

my_russian_btn = tk.Button(root, text="Русский 🇷🇺", font=('Segoe Script', 18), bg="steel blue")
my_russian_btn.pack(pady=20)

my_japanese_btn = tk.Button(root, text="日本語 🇯🇵", font=('Segoe Script', 18), bg="steel blue")
my_japanese_btn.pack(pady=20)

root.mainloop()