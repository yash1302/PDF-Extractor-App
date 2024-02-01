from utils.modularFunc import Function

def TextScrapping(text): # Add parameter text to this.
    # return(pdfText)
    scrappedDataDict = {

            "panNumber" : [],
            "CINNumber" : [],
            "scrappedDate" : [],
            "email" : [],
            "phoneNumber" : [],
            "website" : []
    } 
    obj = Function()

        # to scrape date from first pdf
    date_list = obj.extractDate(text)
    if len(date_list) != 0:
        scrappedDataDict["scrappedDate"].extend(date_list)

    # to scrape email from first pdf
    email_list = obj.extractEmail(text)
    if len(email_list) != 0:
        scrappedDataDict["email"].extend(email_list)

    # to scrape pan number from first pdf
    pan_list = obj.extractPanNumber(text)
    if len(pan_list) != 0:
        scrappedDataDict["panNumber"].extend(email_list)

    # to scrape CIN number from first pdf
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