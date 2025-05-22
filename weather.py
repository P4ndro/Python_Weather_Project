from dotenv import load_dotenv
from pprint import pprint
import requests
import os


load_dotenv()

def get_weather(city="New York"):

    request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data



if __name__ == "__main__":
    print("\n *** GET WEATHER *** \n")
    
    city = input("Enter the city name: ")
    if not bool(city.strip()):
        city = "New York"
        print("No city name provided. Defaulting to New York.")

    weather_data = get_weather(city)

    print("\n")
    pprint(weather_data)

