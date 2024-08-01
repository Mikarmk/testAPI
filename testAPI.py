import requests

response = requests.get("https://randomuser.me/api/")

if response.status_code == 200:
    data = response.json()

    print(data)
else:
    print("Ошибка при получении данных:", response.status_code)
