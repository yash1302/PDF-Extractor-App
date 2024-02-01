from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
from selenium.webdriver.chrome.options import Options
import time

def pdfStoring(url): # add parameters url
    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)
    path = 'C:\\Users\\yashvardhan_Jadhav\\Desktop\\extractPdfText'
    options = Options()
    prefs = {
        "download.default_directory" : path,
        "download.prompt_for_download" : False,
        "download.directory_upgrade" : True,
        "plugins.always_open_pdf_externally" : True
    }
    options.add_experimental_option('prefs',prefs)
    driver = webdriver.Chrome(options=options)    
    driver.get(url)


if __name__ == '__main__':
    pdfStoring()
