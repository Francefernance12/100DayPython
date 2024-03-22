import requests
from twilio.rest import Client

# weather api data
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "41e77fa25ba6d92a74004d92083289fa"
latitude = 40.712776
longitude = -74.005974
weather_parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": API_KEY,
    "cnt": 1
}
# twilio data
account_sid = "AC46a31e1675f19d76db98b942f9ca2f8c"
auth_token = "0892f8215affa8dc65128bfe09552091"

# response
weather_response = requests.get(url=OWM_ENDPOINT, params=weather_parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()

for intervals in weather_data['list']:
    id_code = intervals['weather'][0]["id"]
    if int(id_code) < 700:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
             body="It's raining. You should take an umbrella",
             from_='+18889865552',
             to='+14134051810'
            )

        print(message.status)
    else:
        print(id_code)
        print("You do not need an umbrella")