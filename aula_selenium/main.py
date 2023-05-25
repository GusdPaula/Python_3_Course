from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
)

chrome_browser.get('')

#search_input = WebDriverWait(chrome_browser, 10).until(
#    EC.presence_of_element_located((By.ID, '__tile20'))
#)

time.sleep(30)

select_button = chrome_browser.find_element(By.ID, '')
select_button.click()

time.sleep(10)


#search_input.send_keys('Hello world')
#search_input.send_keys(Keys.ENTER)

