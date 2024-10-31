import PyPDF2

pdfFiles = ["1.pdf", "2.pdf", "sample.pdf"]
pdfMerge = PyPDF2.PdfMerger()
for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    pdfMerge.append(pdfReader)
pdfFile.close()
pdfMerge.write('merged.pdf')