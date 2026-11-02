import os
import pypdf
print("PDF merger: ")
merge = pypdf.PdfWriter()
directory = os.chdir(input("Enter your directory where are all pdfs for merging: "))
files = os.listdir(directory)
for pdf in files:
    merge.append(pdf)
merge.write('outputPdf.pdf')
print("Success!")
print("File name is: 'outputPdf.pdf'")
