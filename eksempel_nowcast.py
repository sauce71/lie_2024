import requests

# Eksempel på Nowcast API fra met.no
# https://api.met.no/weatherapi/nowcast/2.0/documentation
# Yr
# https://www.yr.no/nb/v%C3%A6rvarsel/daglig-tabell/1-30795/Norge/Telemark/Skien/Skien
# Tilleget JSON Fromatter for Google Chrome gjør JSON mer leselig
# https://chromewebstore.google.com/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa


# Koordinater for lokasjon
latitude = 59.2102183365655
longitude = 9.603447767110834

headers = {'User-Agent': 'Bydelshuset kurs tom.oyvnd.hogstad@gmail.com'}
url = f'https://api.met.no/weatherapi/nowcast/2.0/complete?lat={latitude}&lon={longitude}'
print(url)
# requests modulen brukes til å hente og sende data på internett med HTTP protokollen (som en nettleser)
r = requests.get(url, headers=headers)

data = r.json() # Data motatt som json gjøres om til en Python "Dict"
#print(data)

latest_timeseries = data['properties']['timeseries'][0] # Plukker fra hverandre mottate data i flere steg
#print(latest_timeseries)
instant_details = latest_timeseries['data']['instant']['details']
#print(instant_details)

# Printer nøkkel , data 
for k in instant_details:
    print(k, instant_details[k])

print()
# Printer bare en av verdiene fra instant_details
print('Temperaturen ute:', instant_details['air_temperature'])


