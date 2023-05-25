import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/doc/essays/blurb/#:~:text=Python%20is%20an%20interpreted%2C%20object-oriented%2C%20high-level%20programming%20language,or%20glue%20language%20to%20connect%20existing%20components%20together.'

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

text_python = parsed_html.select_one('#content > div > section > article > p:nth-child(3)')

if text_python is not None:
    parent_text_python = text_python.parent

    if parent_text_python is not None:
        for p in parent_text_python.select('p'):
            print(p.text)