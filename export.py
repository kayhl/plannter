import os
from fpdf import FPDF
from font_config import FONT_FAMILY, HEADER_SIZE, BASE_SIZE

def export_to_pdf(title, lines, filename="plannter"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    export_dir = os.path.join(script_dir, "exports")
    output_path = os.path.join(export_dir, filename)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font(FONT_FAMILY, size=HEADER_SIZE, style="B")
    pdf.cell(text=title, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    pdf.set_font(FONT_FAMILY, size=BASE_SIZE)
    for line in lines:
        pdf.cell(text=line, new_x="LMARGIN", new_y="NEXT")

    os.makedirs(export_dir, exist_ok=True)
    pdf.output(output_path)