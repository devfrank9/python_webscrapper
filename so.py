import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs/companies?q=react"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    print(soup)


def get_jobs():
    last_page = get_last_page()
    return []
