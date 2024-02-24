import requests
import json#импорт нужного
r = requests.get('https://swapi.dev/api/vehicles/4/')#получение кода страницы
json_dict=json.loads(r.text)#десериализация JSON
print(json_dict['cost_in_credits'])