import requests#импорт нужного

r = requests.get('https://browser-info.ru/').text
print(r)

with open ('1.html', 'w',encoding=' utf-8') as file:
    file.write(r)