import customtkinter as ctk
from tkinter import font
from veg_data import vegetables

window = ctk.CTk()
window.title("Plannter")
window.geometry("400x1000")
header_font = ctk.CTkFont(family="Helvetica", size=24, weight="bold")
base_font = ctk.CTkFont(family="Helvetica", size=20)

header = ctk.CTkLabel(
    window,
    text="Select vegetables:",
    font=header_font,

)
header.pack(padx=4,pady=8)

checked_state = {}

for veg in vegetables:
    var = ctk.IntVar()
    checkbox = ctk.CTkCheckBox(
        window, 
        text=veg, 
        variable=var,
        font=base_font,
        checkbox_height=18, 
        checkbox_width=18,
        )
    checkbox.pack(padx=4, pady=4,anchor="w")
    checked_state[veg]=var

def generate_plan():
    print("\n  =====  Vegetable Harvest  =====  ")
    for veg, var in checked_state.items():
        if var.get() == 1:
            print(f"{veg} ready to harvest in {vegetables[veg]["days_to_harvest"]} days")

submit_button = ctk.CTkButton(window, text="Submit", command=generate_plan)
submit_button.pack(padx=4, pady=4)

window.mainloop()