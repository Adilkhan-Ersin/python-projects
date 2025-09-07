from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 48)
        head = "CS50 Shirtificate"
        head_w = self.get_string_width(head)
        doc_w = self.w
        self.set_x((doc_w - head_w) / 2)
        self.set_text_color(128, 0, 0)
        self.cell(head_w, 10, head, align='C')

    def shirt_text(self, name):
        self.name = name
        name_w = self.get_string_width(name)
        doc_w = self.w
        doc_h = self.h
        self.set_y(doc_h / 3)
        self.set_x((doc_w - name_w) / 2)
        self.set_font('helvetica', 'B', 28)
        self.set_text_color(255, 255, 255)
        self.cell(name_w, 10, self.name, align='C')

def main():
    name = input("Name: ") + " took CS50"
    pdf = PDF()
    pdf.add_page()
    pdf.image('shirtificate.png', 15, 40, w = pdf.w - 30)
    pdf.shirt_text(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
