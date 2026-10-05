import customtkinter as ctk
from veg_data import vegetables
from datetime import timedelta

class SelectionWindow(ctk.CTkToplevel):
    def __init__(self, parent, option, data):
        super().__init__(parent, fg_color="#B8E3C2")
        self.title("Plannter")
        self.geometry("400x1000")
        self.header_font = ctk.CTkFont(family="Helvetica", size=24, weight="bold")
        self.base_font = ctk.CTkFont(family="Helvetica", size=20)
        self.after(10, self.lift)
        self.option = option

        self.header = ctk.CTkLabel(self,
            text="Select vegetables:",
            font=self.header_font,
        )
        self.header.pack(padx=4,pady=8)

        self.checked_state = {}

        for veg in vegetables:
            var = ctk.IntVar()
            checkbox = ctk.CTkCheckBox(
                self, 
                text=veg, 
                variable=var,
                font=self.base_font,
                checkbox_height=18, 
                checkbox_width=18,
                )
            checkbox.pack(padx=4, pady=4,anchor="w", )
            self.checked_state[veg]=var

        self.submit_button = ctk.CTkButton(
            self,
            text="Submit",
            text_color="#000000",
            command=self.generate_plan,
            fg_color="#FFFFFF",
            corner_radius=5,
            font=("Helvetica", 20),
        )
        self.submit_button.pack(padx=4, pady=4)

    def generate_plan(self):
        if self.option == "plant":
            print("\n  =====  Vegetable Harvest  =====  ")
            print("\nPlant these vegetables in March:")
            for veg, var in self.checked_state.items():
                if var.get() == 1:            
                    if 3 in vegetables[veg]["planting"]:
                        print(f"{veg} will be ready to harvest in {vegetables[veg]['days_to_harvest']} days")
            print("\nPlant these vegetables in April:")
            for veg, var in self.checked_state.items():
                if var.get() == 1:            
                    if 4 in vegetables[veg]["planting"]:
                        print(f"{veg} will be ready to harvest in {vegetables[veg]['days_to_harvest']} days")
        elif self.option == "harvest":
            pass
            
        else:
            print("No selection made")