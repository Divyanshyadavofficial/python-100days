'''write a program to manipulate pdf files using
pypdf your program should be able to merge multiple pdf files into a single pdf.'''
import pypdf
from pypdf import PdfWriter
merger = PdfWriter()
for pdf in ["abs.pdf","abc.pdf"]:
  merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()
