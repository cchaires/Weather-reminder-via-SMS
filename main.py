from twilio.rest import Client
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="twilio.env")

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
api_key = os.environ['API_KEY']
client = Client(account_sid, auth_token)

tj = (32.5010188, -116.964662)

PARAMETERS = {
    "lat": tj[0],
    "lon": tj[1],
    "appid": api_key,
    "exclude": "current,daily,minutely",
    "units": "metric"
}

OMW_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

response = requests.get(OMW_Endpoint, params=PARAMETERS)
response.raise_for_status()
data = response.json()
# print(data)

is_raining = False

weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
    if hour_data['weather'][0]['id'] < 700:
        is_raining = True

if is_raining:
    message = client.messages \
        .create(
        body="It's going to rain. Remember to bring an umbrella ☔",
        from_="+16315199788",
        to="DESTINATION NUMBER"
    )
    print(message.status)
else:
    message = client.messages \
        .create(
        body="Theres no rain for us today☀️!",
        from_="+16315199788",
        to="DESTINATION NUMBER"
    )
    print(message.status)
