import requests#импорт нужного

r = requests.get("https://icanhazip.com/")
print(r.text)
