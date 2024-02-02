from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
import time
from utils.logger import logException


import logging
def pdfStoring(url):
    """this is a function to download pdf from the url

    Args:
        url (string): This url is of website from which we need to download PDF's
    """
    try:
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
        time.sleep(3)
    except Exception as e:
        logException(e)

if __name__ == '__main__':
    pdfStoring()
