from utils.modularFunc import Function
from utils.logger import logException

def TextExtraction(text): # Add parameter text to this.
    """this function is used to extract the text

    Args:
        text (string): the text returned by pdf_to_text is passed as input to this function

    Returns:
        Dictionary: it returns the dictionary which has PAN number, CIN number, Date, Email, Phone number and website
    """
  
    try:
        scrappedDataDict = {

                "panNumber" : [],
                "CINNumber" : [],
                "scrappedDate" : [],
                "email" : [],
                "phoneNumber" : [],
                "website" : []
        } 
        obj = Function()


        date_list = obj.extractDate(text)
        if len(date_list) != 0:
            scrappedDataDict["scrappedDate"].extend(date_list)



        email_list = obj.extractEmail(text)
        if len(email_list) != 0:
            scrappedDataDict["email"].extend(email_list)


        pan_list = obj.extractPanNumber(text)
        if len(pan_list) != 0:
            scrappedDataDict["panNumber"].extend(email_list)
        
        CIN_list = obj.extractCinNumber(text)
        if len(CIN_list) != 0:
            scrappedDataDict["CINNumber"].extend(CIN_list)

        # to scrape phone number from first pdf
        Phone_list = obj.extractPhoneNmber(text)
        if len(Phone_list) != 0:
            scrappedDataDict["phoneNumber"].extend(Phone_list)

        # to scrape website from first pdf
        website_list = obj.extractWebsite(text)
        if len(website_list) != 0:
            scrappedDataDict["website"].extend(website_list)
        # print(scrappedDataDict)
        return scrappedDataDict
    except Exception as e:
        logException(e) 