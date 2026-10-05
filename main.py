import customtkinter as ctk
from selection_window import SelectionWindow
from veg_data import vegetables

class Window(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#B8E3C2")
        self.title("Plannter")
        self.geometry("420x400")
        self.header_font = ctk.CTkFont(family="Helvetica", size=24, weight="bold")
        self.base_font = ctk.CTkFont(family="Helvetica", size=20)
        self.selection_window = None
        self.date_input = None

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
        if self.selection_var.get() == "plant":
            if self.selection_window is None:
                self.selection_window = SelectionWindow(parent=self, option=self.selection_var.get(), data=vegetables)
            else:
                self.selection_window.focus()
        elif self.selection_var.get() == "harvest":
            if self.date_input is None:
                self.input_header = ctk.CTkLabel(
                    self, 
                    text="Input the date you want to harvest on:",
                    font=self.base_font,
                    )
                self.input_header.pack(pady=10)
                self.date_input = ctk.CTkEntry(
                    self,
                    placeholder_text="Input date dd/mm/yyyy",
                    font=self.base_font,
                    )
                self.date_input.pack(pady=10)
            else:
                pass

if __name__ == "__main__":
    window = Window()
    window.mainloop()