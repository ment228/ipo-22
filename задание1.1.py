import requests
import json#импорт нужного

r = requests.get("https://swapi.dev/api/films/1/")#получение кода страницы
json_dict = json.loads(r.text)#десериализация JSON
print(json_dict["opening_crawl"])
