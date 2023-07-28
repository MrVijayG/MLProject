import requests

def get_weather_report(location, date_from=None, date_to=None):
  base_url = "http://api.weatherstack.com/"
  api_key = "c63a5b646fc593566b280b2327e9ca51"  # Replace this with your weather API key
  endpoint = "historical" if date_from and date_to else "current"

  if endpoint == "current":
    url = f"{base_url}{endpoint}?access_key={api_key}&query={location}"
  else:
    url = f"{base_url}{endpoint}?access_key={api_key}&query={location}&historical_date_start={date_from}&historical_date_end={date_to}"

  response = requests.get(url)

  if response.status_code == 200:
    result = response.json()
    return result
  else:
    raise Exception(f"Error: {response.status_code}, {response.text}")
  
print(get_weather_report("What is weather report of mumbai"))