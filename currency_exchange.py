import json
import requests
import sys
import time

def currency_exchange(from_currency, to_currency):
	api_key = '00ee1b54d3f3d7a18c97e2a0c0382a93'
	url = 'https://api.exchangeratesapi.io/latest'

	query_params = {
		'base': from_currency,
    	'symbols': to_currency,
    	'appid': apikey,
	}



	response = requests.get(url, params=query_params)
	print(response.url)
	

	json_data = json.loads(response.text)
	print(json_data['base'])
	print(json_data['date'])
	print(json_data['rates']['INR'])
	


	print('1 '+str(from_currency)+' = ' + str(json_data['rates'][str(to_currency)]) + " " + str(to_currency))
	
if __name__ == '__main__':
	print(sys.argv[0])
	print(sys.argv[1])
	print(sys.argv[2])
	currency_exchange(sys.argv[1], sys.argv[2])

# Execute using $python3 currency_exchange.py USD INR

# Visit https://exchangeratesapi.io/ for API details
