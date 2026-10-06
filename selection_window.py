import customtkinter as ctk
from font_config import FONT_FAMILY, HEADER_SIZE, BASE_SIZE
from veg_data import vegetables
from datetime import datetime, timedelta
from export import export_to_pdf

class SelectionWindow(ctk.CTkToplevel):
    def __init__(self, parent, option, data):
        super().__init__(parent, fg_color="#B8E3C2")
        self.title("Plannter")
        self.geometry("450x600")
        self.header_font = ctk.CTkFont(family=FONT_FAMILY, size=HEADER_SIZE, weight="bold")
        self.base_font = ctk.CTkFont(family=FONT_FAMILY, size=BASE_SIZE)
        self.after(10, self.lift)
        self.option = option
        self.date_input = None
        self.data = data

        self.header = ctk.CTkLabel(self,
            text="Select vegetables:",
            font=self.header_font,
        )
        self.header.pack(padx=4,pady=8)

        self.selection_frame = ctk.CTkScrollableFrame(self, width=450, height=400, fg_color="#B8E3C2")
        self.selection_frame.pack(padx=4, pady=4, fill="both", expand=True)

        self.checked_state = {}

        for veg in sorted(self.data):
            var = ctk.IntVar()
            checkbox = ctk.CTkCheckBox(
                self.selection_frame, 
                text=veg, 
                variable=var,
                font=self.base_font,
                checkbox_height=18, 
                checkbox_width=18,
                )
            checkbox.pack(padx=4, pady=4,anchor="w", )
            self.checked_state[veg]=var

        if self.option == "harvest":
            self.input_header = ctk.CTkLabel(
                self, 
                text="Input date to harvest on:",
                font=self.base_font,
                )
            self.input_header.pack(pady=10)
            self.date_input = ctk.CTkEntry(
                self,
                placeholder_text="mm/dd/yyyy",
                font=self.base_font,
                width=250,
                )
            self.date_input.pack(pady=10)

        self.submit_button = ctk.CTkButton(
            self,
            text="Submit",
            text_color="#000000",
            command=self.generate_plan,
            fg_color="#FFFFFF",
            corner_radius=5,
            font=self.base_font,
        )
        self.submit_button.pack(padx=4, pady=4)

    def generate_plan(self):
        pdf_lines = []

        if self.option == "plant":
            title = f"  =====  Harvest Schedule  =====  "
            print(title)
            if not any(var.get() == 1 for var in self.checked_state.values()):
                print("No vegetables selected")
                return
            march = "Plant these vegetables in March:"
            print(march)
            pdf_lines.append(" ")
            pdf_lines.append(march)
            for veg, var in self.checked_state.items():
                if var.get() == 1:            
                    if 3 in self.data[veg]["planting"]:
                        line = f"{veg} will be ready to harvest in {self.data[veg]['days_to_harvest']} days"
                        print(line)
                        pdf_lines.append(line)
            april = "Plant these vegetables in April:"
            print(april)
            pdf_lines.append(" ")
            pdf_lines.append(april)
            for veg, var in self.checked_state.items():
                if var.get() == 1:            
                    if 4 in self.data[veg]["planting"]:
                        line = f"{veg} will be ready to harvest in {self.data[veg]['days_to_harvest']} days"
                        print(line)
                        pdf_lines.append(line)

        elif self.option == "harvest":
            title = f"  =====  Planting Schedule  =====  "
            print(title)
            if not any(var.get() == 1 for var in self.checked_state.values()):
                print("No vegetables selected")
                return
            given_date = self.date_input.get()
            try:
                formatted_date = datetime.strptime(given_date, "%m/%d/%Y")
                selected_date = formatted_date.strftime("%m/%d/%Y")
                date_line = f"To be ready for harvest on {selected_date}"
                print(date_line)
                pdf_lines.append(date_line)
                pdf_lines.append(" ")
                for veg, var in self.checked_state.items():
                    if var.get() == 1:
                        plant_date = formatted_date - timedelta(days=self.data[veg]["days_to_harvest"])
                        output_date = plant_date.strftime("%m/%d/%Y")
                        line = f"{veg} should be planted on {output_date}"
                        print(line)
                        pdf_lines.append(line)
                    else:
                        pass
            except ValueError:
                print("Expected date format - mm/dd/yyyy")
                return

        else:
            print("No selection made")
            return

        export_to_pdf(title, pdf_lines)