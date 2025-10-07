import requests
import pandas as pd
from bs4 import BeautifulSoup #импортируем библиотеку BeautifulSoup

#ссылка на сайт, с которого осуществляется парсинг данных
URL = "https://realpython.github.io/fake-jobs/"
#проверка доступности сайта
page = requests.get(URL)

#объявляем массивы
title = []
company = []
location = []

#получаем код сайта
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

#разбиваем сайт на карточки с данными
job_elements = results.find_all("div", class_="card-content")

#получаем данные с сайта и добавляем их массивы
for job in job_elements:
    title_element = job.find("h2", class_="title")
    company_element = job.find("h3", class_="company")
    location_element = job.find("p", class_="location")
    title.append(title_element.text.strip())
    company.append(company_element.text.strip())
    location.append(location_element.text.strip())

#записываем и выводим датафрейм
df = pd.DataFrame({'Должности': title, 'Компании': company, 'Локации': location})

# выводим 10 первых строк
print("Первые 10 вакансий:")
print(df.head(10))