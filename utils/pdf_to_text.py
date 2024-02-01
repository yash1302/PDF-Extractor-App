from PyPDF2 import PdfReader 

def exportTextFromPdf(pdf_name,pageno): # Add pdf_name parameter
    text = " "
    reader = PdfReader(pdf_name)
    for i in range(0,pageno):
        page = reader.pages[i] 
        text += page.extract_text()
    return text

