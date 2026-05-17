import requests

API_CLIMATE = "861842146dddf40be6a1cb1b551705e2"
city_name = "Luanda"
link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_CLIMATE}&lang=pt_br"
response = requests.get(link)
response_dict = response.json()

response = requests.get(link)


def get_description_climate():
    response_dict = response.json()

    description = response_dict["weather"][0]["description"]

    return description

def get_climate():

    response_dict = response.json()

    temperature = response_dict["main"]["temp"] - 273.15

    return f"{temperature:.2f}°C"

print(get_climate())
