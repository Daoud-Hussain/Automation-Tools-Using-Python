from fpdf import FPDF
Pdf = FPDF()
list_of_images = ["1.jps", "2.jps"]
for i in list_of_images : # list of images vitn filename
    Pdf.addpage()
    Pdf.image(i,x,y,w,h)
    Pdf.output("yourfile.pdf", "F")