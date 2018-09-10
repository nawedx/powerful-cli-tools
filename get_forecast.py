import json
import requests
import sys
import time

def forecast_by_city_name(city_name):
	api_key = '00ee1b54d3f3d7a18c97e2a0c0382a93' 
	#api_url = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&units=metric&APPID="+str(api_key)
	
	url = 'https://api.openweathermap.org/data/2.5/weather'

	query_params = {
    	'q': city_name,
    	'units': 'metric',
    	'appid': api_key,
	}

	response = requests.get(url, params=query_params)
	
	json_data = json.loads(response.text)
	print(json_data)
	print("City: "+ str(json_data['name']))
	print(json_data['weather'][0]['description'])
	print("Temp: " + str(json_data['main']['temp'])+" Celcius")
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json_data['dt'])))

if __name__ == '__main__':
    forecast_by_city_name(sys.argv[1])

# Execute using $python3 get_forecast.py Bhubaneswar
