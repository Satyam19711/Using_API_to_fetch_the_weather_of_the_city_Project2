import requests

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def get_weather(api_key, city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(base_url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            temperature_celsius = kelvin_to_celsius(temperature)
            print(f"The temperature in {city} is {temperature_celsius:.2f}°C.")
        else:
            print("Invalid data or error in fetching data.")
    
    
    # try and except
    except KeyError:
        print("Invalid data or error in fetching data.")

if __name__ == "__main__":
    api_key = "e361b1d8d8f48167c2f26ca7ce288e8e"  
    city_name = input("Enter the city name: ")

    get_weather(api_key, city_name)








