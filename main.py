import customtkinter

APP_NAME = "CharacterPlanner Version 1.0.0-PreAlpha"

class MainScreenFrame(customtkinter.CTkFrame):
    def __init__(self, master, switch_frame_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.switch_frame_callback = switch_frame_callback  # Callback to switch frames
        self.add_character_bttn = customtkinter.CTkButton(self, text="Add Character Stories", command=lambda: self.switch_frame_callback(1))
        self.add_character_bttn.pack(padx=20, pady=20)
        self.view_character_bttn = customtkinter.CTkButton(self, text="View Character Stories", command=lambda: self.switch_frame_callback(2))
        self.view_character_bttn.pack(padx=30, pady=30)
        self.remove_character_story = customtkinter.CTkButton(self, text="Remove Character Stories", command=lambda: self.switch_frame_callback(3))
        self.remove_character_story.pack(padx=40, pady=40)

class AddCharacterFrame(customtkinter.CTkFrame):
    def __init__(self, master, switch_frame_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.switch_frame_callback = switch_frame_callback  # Callback to switch frames

        # Label and Entry for Character's Name
        self.char_name_label = customtkinter.CTkLabel(self, text="Please enter your character's name")
        self.char_full_name = customtkinter.CTkEntry(self, width=200, placeholder_text="'Eirkas Longbottom'")

        # Label and Entry for Character's Race
        self.char_race_label = customtkinter.CTkLabel(self, text="Please enter your character's race")
        self.char_race = customtkinter.CTkEntry(self, width=200, placeholder_text="'Half-Elf'")

        # Label and Entry for Character's Class
        self.char_class_label = customtkinter.CTkLabel(self, text="Please enter your character's class")
        self.char_class = customtkinter.CTkEntry(self, width=200, placeholder_text="'Ranger'")

        # Label and Entry for Character's Alignment
        self.char_alignment_label = customtkinter.CTkLabel(self, text="Please enter your character's alignment")
        self.char_alignment = customtkinter.CTkEntry(self, width=200, placeholder_text="'Chaotic-Neutral'")

        # Label and Entry for Character's eXP Level
        self.char_eXP_label = customtkinter.CTkLabel(self, text="Please enter your character's eXP level")
        self.char_eXP = customtkinter.CTkEntry(self, width=200, placeholder_text="'400xP'")

        # Label and Textbox for Character's Backstory
        self.char_backstory_label = customtkinter.CTkLabel(self, text="Please enter your character's backstory")
        self.char_backstory = customtkinter.CTkTextbox(self, width=800, corner_radius=0)

        # Setting each input control onto the actual frame with the grid layout
        self.char_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.char_full_name.grid(row=1, column=0, padx=10, pady=5)

        self.char_race_label.grid(row=2, column=0, padx=10, pady=5)
        self.char_race.grid(row=3, column=0, padx=10, pady=5)

        self.char_class_label.grid(row=4, column=0, padx=10, pady=5)
        self.char_class.grid(row=5, column=0, padx=10, pady=5)

        self.char_alignment_label.grid(row=6, column=0, padx=10, pady=5)
        self.char_alignment.grid(row=7, column=0, padx=10, pady=5)

        self.char_eXP_label.grid(row=8, column=0, padx=10, pady=5)
        self.char_eXP.grid(row=9, column=0, padx=10, pady=5)

        self.char_backstory_label.grid(row=10, column=0, padx=10, pady=5)
        self.char_backstory.grid(row=11, column=0, padx=10, pady=5)

        #Submit Button when all fields are filled out.
        self.SubmitButton = customtkinter.CTkButton(self, text="Submit")
        self.SubmitButton.grid(row=12,column=0)

    def save_character_process(self):
        print("This will be a tough one haha")




class UserInterfaceManager(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title(APP_NAME)

        # Initialize current_frame as None, will set later
        self.current_frame = None

        # Set grid row and column weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Start by displaying the main screen frame
        self.switch_frame(0)

    def switch_frame(self, frame_id):
        # If a frame exists, destroy it
        if self.current_frame is not None:
            self.current_frame.destroy()

        # Switch between frames based on frame_id
        if frame_id == 0:
            self.current_frame = MainScreenFrame(master=self, switch_frame_callback=self.switch_frame)
        elif frame_id == 1:
            self.current_frame = AddCharacterFrame(master=self, switch_frame_callback=self.switch_frame)

        # Place the new frame in the grid
        self.current_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Instantiate and run the app
app = UserInterfaceManager()
app.mainloop()
