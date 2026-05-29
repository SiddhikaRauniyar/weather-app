import requests

def get_weather(city):
    api_key = "b423c353ce2b105ade8688ef151e70a1"  # paste your key here
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        
        print(f"\n📍 {city_name}, {country}")
        print(f"🌡️  Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"🌤️  {description.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
    else:
        print("City not found. Try again.")

city = input("Enter city name: ")
get_weather(city)