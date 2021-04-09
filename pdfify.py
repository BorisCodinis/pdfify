#!/usr/bin/python3
import argparse
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


parser = argparse.ArgumentParser(description='process pdf files', prog="Pdfify")

parser.add_argument("-v", "--version", action='version', version='%(prog)s 0.1')
parser.add_argument("action", metavar="action", choices=["split", "print"], help="the action you want to start", default="split")
parser.add_argument("file", help="PDF file you want to interact with")
parser.add_argument("-p", "--page", type=int, help="page of pdf you want to interact with")
args = parser.parse_args()

def getFileName():
	pass	


def splitFileAtPage(filePath, page):

	pdfPath = Path(filePath)
	if not pdfPath.is_file():
		print("Pdfify: error: file argument must be a filepath")
		exit()
	
	if not str(pdfPath).endswith(".pdf"):
		print("Pdfify: error: File given must be a PDF")	
		exit()
	print("is pdf File")
	print(pdfPath)
	pdf = PdfFileReader(str(pdfPath))
	
	pdf_writer = PdfFileWriter()
	pdf_writer.addPage(pdf.getPage(page))

	with open("extracted.pdf", "wb") as out:
		pdf_writer.write(out)

if __name__ == "__main__":
	if args.action == "split":
		if args.page == None:
			print("Pdfify: error: page must be given if you want to split a page")
			exit()
		else:
			splitFileAtPage(args.file, args.page)

