import requests

city = input("Enter city name: ")
api_key = "651e85f36f550944c0c554acb2725915"  


url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()


temperature = 30
humidity = 70
weather = "Clear Sky"
wind_speed = 4

print("\nWeather Information")
print("----------------------")
print("City:", city)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Weather Condition:", weather)
print("Wind Speed:", wind_speed, "m/s")

