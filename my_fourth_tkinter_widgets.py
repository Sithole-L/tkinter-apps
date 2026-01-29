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
        self.geometry("500x800")
        self.title("Guest Register")
        self.config(bg="#393D3F", relief='raised')

        # Configure two frames stacked vertically (guest_frame and menu_frame)
        self.guest_frame = ttk.Frame(self, padding= 20)
        self.guest_frame.pack(side="top", fill="both", expand=True)

        self.menu_frame = ttk.Frame(self, padding= 20)
        self.menu_frame.pack(side="top", fill="both", expand=True)

        # Split menu_frame into meal_selection and drinks_selection
        self.meal_selection = ttk.Frame(self.menu_frame, padding= 15, relief='raised')
        self.meal_selection.pack(side='left', fill='both', expand=True)

        self.drinks_selection = ttk.Frame(self.menu_frame, padding= 15, relief='raised')
        self.drinks_selection.pack(side='left', fill='both', expand=True)

        #Define roles, meal options, and drinks options
        self.roles = ["Guest", "Speaker", "Organiser"]

        self.meal_choices = {"Sandwich": "🥪",
                             "Salad": "🥗",
                             "Pizza": "🍕",
                             "Pasta": "🍝"}
        
        self.drinks_choices = {"water": "💧",
                               "Tea": "🍵",
                               "Coffee": "☕",
                               "Fizzy": "🥤",
                               "Juice": "🍹"}
        
        # Initialise variables
        self.selected_role = tk.StringVar(value=self.roles[0])
        self.selected_meal = tk.StringVar(value="Sandwich")
        self.selected_drink = tk.StringVar(value="Water")
        self.guest_name = tk.StringVar()

        # Create and pack the widgets
        self.create_widgets()

    def create_widgets(self):
        
        top_label = tk.Label(self.guest_frame,
                             text="Welcome to the Guest Register",
                             font=("Arial", 20),
                             bg="#F9DBBD")
        top_label.pack(pady=10, fill='x')

        name_frame = ttk.Frame(self.guest_frame)
        name_frame.pack(fill="x", pady=5)
        ttk.Label(name_frame, text="Name: ", font=("Arial", 14)).pack(pady=10)
        tk.Entry(name_frame, textvariable=self.guest_name, font=("Arial", 14)).pack(padx=20, pady=10, fill='x')
        tk.Label(name_frame, text="Choose your Role: ", font=("Arial", 14)).pack(pady=10)

        optionmenu = tk.OptionMenu(name_frame, self.selected_role, *self.roles)
        optionmenu.config(font=("Arial", 14), bg="#ffb38a")
        optionmenu["menu"].config(font=("Arial", 20), bg="#ffb38a")
        optionmenu.pack(pady=10, padx=20)

        meal_frame = ttk.Frame(self.meal_selection)
        meal_frame.pack(fill="both", expand=True)
        ttk.Label(meal_frame, text="Choose your meal: ", font=("Arial", 14)).grid(row=0, column=0, sticky='w', pady=5)
        for idx, (item, emoji) in enumerate(self.meal_choices.items(), start=1):
            tk.Radiobutton(meal_frame, text=f"{emoji} {item}", value=item, variable=self.selected_meal,
                           font=("Arial", 14), bg="#e2e2e2", anchor='w').grid(row=idx, column=0, sticky='w')

        drinks_frame = ttk.Frame(self.drinks_selection) 
        drinks_frame.pack(fill='both', expand=True)
        ttk.Label(drinks_frame, text="Choose your drink: ", font=("Arial", 14)).grid(row=0, column=0, sticky='w', pady=5)
        for idx, (item, emoji) in enumerate(self.drinks_choices.items(), start=1):
            tk.Radiobutton(
                drinks_frame,
                text=f"{emoji} {item}",
                value=item,
                variable=self.selected_drink,
                font=("Arial", 14),
                bg="#e2e2e2",
                anchor='w'
            ).grid(row=idx, column=0, sticky='w', padx=5, pady=2)


        
        tk.Button(self, text="Register", command=self.register_guest, font=("Arial", 20), bg="light green").pack(pady=20)

    def title_case(self, name: str) -> str:
        return name.title()

    def presence_check(self, name: str) -> bool:
        return bool(name)

    def name_length_check(self, name: str) -> bool:
        return 0 < len(name) <= 50

    def format_check(self, name: str) -> bool:
        pattern = re.compile(r"^[a-zA-Z-' ]+$")
        return bool(pattern.match(name))

    def construct_error_message(self, errors: list) -> str:
        return "\n".join(errors)

    def register_guest(self):
        name = self.guest_name.get().strip() 
        name = self.title_case(name)
        role = self.selected_role.get()
        meal = self.selected_meal.get()
        drink = self.selected_drink.get()


        errors = []

        if not self.presence_check(name):
            errors.append("Name cannot be empty!")
        
        if not self.name_length_check(name):
            errors.append("Name should be between 1 and 50 characters long!")
        
        if not self.format_check(name):
            errors.append("Name should only contain letters, dashes, spaces, and apostrophes!")

        if errors:
            messagebox.showerror("Error", self.construct_error_message(errors))
            return
        
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open('guests.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, role, meal, drink, timestamp])

        messagebox.showinfo("Registration Successful", f"{name}, registered as {role}, has chosen {meal} and {drink} for lunch.")


app = GuestRegister()
app.mainloop()


