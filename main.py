import json
from utils import extractText, pdfDownload,pdf_to_text,logger

def main():

    
    try:
        with open("C:\\Users\\yashvardhan_Jadhav\\Desktop\\extractPdfText\\config.json","r") as file:
            json_loaded = json.load(file)
        logger.logMessage("input from Json file is loaded")
        url_data = json_loaded['urls']
        page_no = json_loaded['page_count']
        final_data = {}

        for count,url in enumerate(url_data):
            pdfDownload.pdfStoring(url)
            logger.logMessage("pdf has been downloaded")

            SplittedUrl = url.split("/")[-1]
            logger.logMessage("url has been splitted")

            pdfText = pdf_to_text.exportTextFromPdf(SplittedUrl,page_no)
            logger.logMessage("pdf has been converted into text")

            final_data[count] = extractText.TextExtraction(pdfText)
            logger.logMessage("data has been scrapped and stored into dictionary")

        json_object = json.dumps(final_data, indent=4)
        with open("output.json", "w") as outfile:
            outfile.write(json_object)
        logger.logMessage("output has been uploaded to output.json file")

    except Exception as e:
        logger.logException(e)
        



if __name__ == '__main__':
    main()