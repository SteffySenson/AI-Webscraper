import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(website, keywords):
    print("Launching chrome browser...")

    chrome_driver_path = "./chromedriver.exe" 
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Page loaded...")
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        extracted_data = {}

        for keyword in keywords:
            # Use the correct class name 'attrib'
            name_cell = soup.find('td', class_='attrib', string=lambda text: keyword in text)
            if name_cell:
                data_cell = name_cell.find_next_sibling('td')
                extracted_data[keyword] = data_cell.text.strip() if data_cell else 'N/A'
            else:
                extracted_data[keyword] = 'N/A'

        return extracted_data
    finally:
        driver.quit()