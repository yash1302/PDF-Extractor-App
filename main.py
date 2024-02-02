import json
from utils import pdfDownload,pdf_to_text,scrapeText

def main():
    # 1. load json file into dictionary named json_data.
    # 2. Get urls from json_data like json_data['urls'] in list named urls.
    # 3. Declare final_data dictionary.
    # 4. Start a for loop which will iterate through urls like for url in urls.
        # 5. pass url to pdfStoring() function.
        # 6. Split url with "/". Get the last element. This will be your pdf name.
        # 7. Pass the PDF Name to exportTextFromPdf(). This will return the text extracted from the pdf. 
            # pdfText = exportTextFromPdf(pdf_name) 
        # 8. Using that function call the necessary function and pass pdfText (variable declared above) to it.
        # 9. Store the data in the final_data.
    # 10. Save final_data to json file.
    with open("C:\\Users\\yashvardhan_Jadhav\\Desktop\\extractPdfText\\config.json","r") as file:
        jsonloaded = json.load(file)
    json_data = jsonloaded['urls']
    page_no = jsonloaded['page_count']
    # print(jsonloaded['page_count'])
    # print(json_data)
    final_data = {}

    for count,url in enumerate(json_data):
        pdfDownload.pdfStoring(url)
        SplittedUrl = url.split("/")[-1]
        # print(SplittedUrl)
        pdfText = pdf_to_text.exportTextFromPdf(SplittedUrl,page_no)
        final_data[count] = scrapeText.TextScrapping(pdfText)
        # print(final_data)
    json_object = json.dumps(final_data, indent=4)
    with open("output.json", "w") as outfile:
        outfile.write(json_object)

    # print(final_data)


if __name__ == '__main__':
    main()