import requests

# We need coordinates to get weather data
latitude = 6.865   # UNN latitude
longitude = 7.408   # UNN longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

type_of_data = type(data)
print("The type of the data is: ", type_of_data)
print("The data received from the API is: ", data)

data["timezone"]