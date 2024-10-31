import requests

# get-метод, запрос на сайт

r = requests.get('https://rbc.ru/')

# Status-code - проверка успешности запроса через код-состояние
if r.status_code == 200:
	print(f'Запрос прошёл успешно, статус: {r}')
else:
	print(f'Запрос не успешный, статус: {r}')

# HTTP-заголовки в ответе для получения данных: инфо о сервере, дата, кодировка, etc.
print(r.headers)

# Метод text возвращает данные в текстовом виде
print(r.text)

# Метод content возвращает данные в байтовом виде
print(r.content)

# Time-out подключения позволяет указывать время ожидания
# ответа сервера через аргумент timeout
# None в качества аргумента - можно сдать вечность.
res = requests.get('https://rbc.ru/', timeout=5)
print(res)

# если бы была лицензия, можно было бы по заданным коордианатам
# получить срез карты, здесь - центра СПб.
response = requests.get("https://static-maps.yandex.ru/1.x/?"
				"ll=59.948244,30.317486&"
				"spn=0.016457,0.00619&"
				"l=map")
print(response)

with open("map.png", "wb") as file:
	file.write(response.content)
