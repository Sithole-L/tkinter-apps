import tkinter as tk

class EmojiChooser(tk.Tk):
    def __init__(self, screenName = "Emoji Chooser (Drop-Down Control)"):
        super().__init__(screenName)

        self.geometry("500x400")
        self.title("Choose Your Emoji")
        self.config(bg= "light steel blue")

        self.emoji_dict = {"Koala": "🐨",
                           "Dolphin": "🐬",
                           "Flamingo": "🦩",
                           "Peacock": "🦚",
                           "Kangaroo": "🦘",
                           "Rhinoceros": "🦏",
                           "Fox": "🦊",
                           "Unicorn": "🦄",
                           "Tiger": "🐯",
                           "Parrot": "🦜",
                           "Lion": "🦁",
                           "Dragon": "🐉"}
        
        # Create a list of animals
        self.animals_list = list(self.emoji_dict.keys())

        # Set the first animal as the default value in the dropdown
        self.selected_animal = tk.StringVar()
        self.selected_animal.set(self.animals_list[0])

        # Create and pack a label to instruct the user
        self.instructions_label = tk.Label(self,
                                          text= "Choose an animal",
                                          font= ('Arial', 20),
                                          bg= 'steel blue')
        self.instructions_label.pack(pady= 10)

        # Create and pack a dropdown menu for animal selection
        self.dropdown = tk.OptionMenu(self,
                                      self.selected_animal,
                                      *self.animals_list)
        self.dropdown.config(font=("Arial", 20),
                             bg="steel blue")
        
        self.dropdown["menu"].config(font=("Arial", 20),
                                     bg="steel blue")
        
        self.dropdown.pack(padx=20, pady=20)

        # Create a button that will call the show_emoji method when clicked
        self.btn = tk.Button(self,
                             command=self.show_emoji,
                             text = "Get Animal!",
                             font = ('Arial', 20),
                             bg = "steel blue")
        self.btn.pack(pady = 20)
    
        # Create and pack a label to display the selected emoji
        self.label_emoji = tk.Label(self,
                                    text = "",
                                    font = ('Arial', 100),
                                    bg = "light green")
        self.label_emoji.pack(pady = 10)

    def show_emoji(self):
        # Display the corresponding emoji in the label
        animal = self.selected_animal.get()
        animal = self.emoji_dict.get(animal, "")
        self.label_emoji.config(text=animal)


app = EmojiChooser()
app.mainloop()