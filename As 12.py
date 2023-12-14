#Assignment 12
#Using external interfaces

#1
import requests
import json
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print("Random Chuck Norris joke :\n",response["value"])

#2
import requests
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_desc = data['weather'][0]['description']
            temp_kelvin = data['main']['temp']
            temp_celsius = kelvin_to_celsius(temp_kelvin)
            print(f"Weather in {city}: {weather_desc}")
            print(f"Temperature in kelvin : {temp_celsius:.2f} degree")
        else:
            print(f"Error: {response.status_code} - {data['message']}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

def main():
    api_key = '667b16b1f18490a4dbf79cd4c11ecea2'
    city = input("Enter the name of a municipality: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()



