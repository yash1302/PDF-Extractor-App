import re
from utils.pdf_to_text import exportTextFromPdf

class Function:
    def __init__(self):
        pass

    def extractDate(self, text: str) -> list:
        return re.findall(r"\d\d[/-]\d\d[/-]\d\d\d\d", text)

    def extractEmail(self,text:str) -> list:
        return re.findall(r"\S+@\S+",text)
    
    def extractPanNumber(self,text:str) ->list:
        return re.findall(r"[A-Z]{5}[0-9]{4}[A-Z]",text)
    
    def extractPhoneNmber(self,text:str) ->list:
        return re.findall(r"\d{11}",text)
    
    def extractCinNumber(self,text:str)->list:
        return re.findall(r"[A-Z][0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}",text)
    
    def extractWebsite(self,text:str)->list:
        return re.findall(r"[w]{3}[.]\S+[].]\S+",text)
    
    