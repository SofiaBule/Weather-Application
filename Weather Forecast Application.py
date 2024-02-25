import requests

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    return data['weather'][0]['description']

# Example usage:
city = "New York"
weather = get_weather(city)
print(f"The weather in {city} is {weather}.")
