import requests


API_CLIMATE = "861842146dddf40be6a1cb1b551705e2"
city_name = "Luanda"
link = f"https://api.openweathermap.org/data/3.0/onecall?q={city_name}&appid={API_CLIMATE }"

response = requests.get(link)

if response.status_code == 200:
    