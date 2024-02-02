from PyPDF2 import PdfReader 

def exportTextFromPdf(pdf_name,pageno): # Add pdf_name parameter
    """This function gives text extracted from pdf

    Args:
        pdf_name (string): pdf names are passed as parameters
        pageno (int): the page number till which we need to extract the data

    Returns:
        [string]: [returns the text which has been extracted from pdf]
    """
    text = " "
    reader = PdfReader(pdf_name)
    for i in range(0,pageno):
        page = reader.pages[i] 
        text += page.extract_text()
    return text

