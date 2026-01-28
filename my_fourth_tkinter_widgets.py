import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import csv
import re

class GuestRegister(tk.Tk):
    def __init__(self, screenName = "Guest Register"):
        super().__init__(screenName)

        # Configure the main window
        self.geometry("600x500")
        self.title("Guest Register")
        self.config(bg="light slate grey")

        # Configure two frames stacked vertically (guest_frame and menu_frame)
        guest_frame = ttk.Frame(self, padding= 20)
        guest_frame.pack(side="top", fill="both", expand=True)

        menu_frame = ttk.Frame(self, padding= 20)
        menu_frame.pack(side="top", fill="both", expand=True)

        # Split menu_frame into meal_selection and drinks_selection
        meal_selection = ttk.Frame(menu_frame, padding= 15, relief='raised')
        meal_selection.pack(side='left', fill='both', expand=True)

        drinks_selection = ttk.Frame(menu_frame, padding= 15, relief='raised')
        drinks_selection.pack(side='left', fill='both', expand=True)

        #Define roles, meal options, and drinks options
        self.roles = ["Guest", "Speaker", "Organiser"]
        self.meal_choices = {"Sandwich": "🥪",
                             "Salad": "🥗",
                             "Pizza": "🍕",
                             "Pasta": "🍝"}
        
        self.drinks_choices = {"water": "🥛",
                               "Tea": "🍵",
                               "Coffee": "☕",
                               "Fizzy": "🥤",
                               "Juice": "🍹"}
        
        # Initialise variables
        


app = GuestRegister()
app.mainloop()


