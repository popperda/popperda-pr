import requests

r = requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en").json()
print(r['forecastPeriod'])
print(r['generalSituation'])
print(r['forecastDesc'])
print(r['tcInfo'])
a = requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en").json()
print(a['weatherForecast'])