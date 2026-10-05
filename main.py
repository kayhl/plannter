import customtkinter as ctk
from selection_window import SelectionWindow
from veg_data import vegetables

class Window(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#B8E3C2")
        self.title("Plannter")
        self.geometry("400x200")
        self.header_font = ctk.CTkFont(family="Helvetica", size=24, weight="bold")
        self.base_font = ctk.CTkFont(family="Helvetica", size=20)
        self.selection_window = None

        self.header = ctk.CTkLabel(
            self,
            text="Which plan do you want?",
            font=self.header_font,
        )
        self.header.pack(padx=4,pady=8)

        self.selection_var = ctk.StringVar(value="")

        self.plant_radio = ctk.CTkRadioButton(
            self,
            text="I want to plant together",
            font=("Helvetica", 20),
            value="plant",
            variable=self.selection_var,
            )
        self.plant_radio.pack(anchor="w", padx=20, pady=10)

        self.harvest_radio = ctk.CTkRadioButton(
            self,
            text="I want to harvest together",
            font=("Helvetica", 20),
            value="harvest",
            variable=self.selection_var,
            )
        self.harvest_radio.pack(anchor="w", padx=20, pady=10)

        self.submit_button = ctk.CTkButton(
            self,
            text="Submit",
            text_color="#000000",
            fg_color="#FFFFFF",
            corner_radius=5,
            font=("Arial", 20),
            command=self.selection,
        )
        self.submit_button.pack(padx=4, pady=4)

    def selection(self):
        if self.selection_window is None or not self.selection_window.winfo_exists():
            self.selection_window = SelectionWindow(parent=self, selection=self.selection_var.get(), data=vegetables)
        else:
            self.selection_window.focus()

if __name__ == "__main__":
    window = Window()
    window.mainloop()