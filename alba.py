import csv
import requests
from bs4 import BeautifulSoup

URL = "http://www.alba.co.kr"

dict = {}
request = requests.get(URL)
soup = BeautifulSoup(request.text, "html.parser")

tables = soup.find("div", {"id": "MainSuperBrand"})
ul = tables.find('ul', {"class": "goodsBox"})
li = ul.find_all(
    'a', {"class": "goodsBox-info"})

for company_link in li:
    company_name = company_link.find("span", {"class": "company"})
    try:
        print(f"{company_name.string}.csv 생성중")
        file = open(f"{company_name.string}.csv", mode="w",
                    encoding='utf-8-sig', newline='')
        writer = csv.writer(file)
        writer.writerow(["place", "title", "time", "pay", "date"])
    except:
        pass

    link = company_link.attrs['href']
    company_request = requests.get(link)
    company_soup = BeautifulSoup(company_request.text, "html.parser")
    div = company_soup.find("div", {"class": "goodsList goodsJob"})
    table_tbody = div.find("table").find("tbody")

    place = table_tbody.find_all("td", {"class": "local first"})
    title = table_tbody.find_all("td", {"class": "title"})
    time = table_tbody.find_all("td", {"class": "data"})
    pay = table_tbody.find_all("td", {"class": "pay"})
    date = table_tbody.find_all("td", {"class": "regDate last"})

    for i in range(len(place)):
        print(f"{company_name.string}.csv의 테이블 생성중")
        dict['place'] = place[i].text
        dict['title'] = (title[i].find(
            "span", {"class": "company"})).string
        dict['time'] = time[i].string
        dict['pay'] = pay[i].text
        dict['date'] = date[i].text
        writer.writerow(list(dict.values()))

    dict = {}

print("완료")
