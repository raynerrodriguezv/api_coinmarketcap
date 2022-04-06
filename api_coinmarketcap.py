from urllib import response
import requests





def get_price(symbol):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
        'symbol' : symbol
    }

    headers = {

        'Accepts': 'application/json', 
        'X-CMC_PRO_API_KEY' : api_key
        
    }

    # with headers
    # X-CMC_PRO_API_KEY
    # without headers
    # CMC_PRO_API_KEY
    
    response = requests.get(url, params=parameters, headers=headers)

    
    return response.json().get('data', {}).get(symbol, {}).get('quote', {}).get('USD', {}).get('price')



# if __name__ == "__main__":
moneda = input("Moneda a revisar: ")  
print(get_price(moneda.upper()))
    