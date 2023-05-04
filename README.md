# Weather Alert via Twilio
This Python script checks if it's going to rain in Tijuana, Mexico using the OpenWeatherMap API. If rain is expected, it sends an SMS message using Twilio's API to remind the user to bring an umbrella.

To use this script, you will need to obtain API keys for OpenWeatherMap and Twilio and save them in a twilio.env file. The file should contain the following variables:

- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `API_KEY`

Make sure to replace DESTINATION NUMBER and your TWILIO PHONE NUMBER with your actual phone numbers.

Note: This script requires the `requests`, `os`, `dotenv`, and `twilio` libraries.
