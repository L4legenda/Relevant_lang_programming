from programmingLang import lang
import matplotlib.pyplot as plt
import requests
import re

rang = {}

url = 'https://api.hh.ru/vacancies'
par = {'text': 'Программист', 'area': '55', 'per_page': '5'}
r = requests.get(url, params=par)
answer = r.json()
quantity = int(answer["pages"]) - 1


def search(answer):
    langArr = []

    for i in range(5):
        snippet = answer["items"][i]["snippet"]["requirement"]
        valid = re.sub(r"[^1-9A-Za-zА-Яа-я ]+", " ", snippet)

        for l in lang:
            if l in valid.lower().split():
                langArr.append(l)

    return langArr

def addRang(listLang):
    global rang
    for l in listLang:
        if l in rang:
            rang[l] += 1
        else:
            rang[l] = 1

addRang(search(answer))

for i in range(1, quantity):
    par["page"] = str(i)
    r = requests.get(url, params=par)
    answer = r.json()
    addRang(search(answer))

plt.figure(figsize=(13, 3))

for l in rang:
    plt.bar(l, rang[l])
plt.suptitle("Популярные технологии в Кургане")
plt.show()