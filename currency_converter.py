import requests

class CurrencyConverter:

    def __init__(self, url, api_key):
        # Set up the query parameters with the API key
        params = {
            'access_key': api_key  # Adjust the query parameter name if needed
        }
        # Make the request with the API key
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            info = response.json()
            if 'rates' in info:
                self.rates = info['rates']
            else:
                raise KeyError("'rates' key not found in the API response")
        else:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

    def convert_currency(self, currency_from, currency_to, amount):
        if currency_from == currency_to:
            print('{} {} = {} {}'.format(amount, currency_from, amount, currency_to))
            return
        
        # Handle conversion assuming base currency is USD
        initial = amount
        if currency_from != 'USD':
            if currency_from not in self.rates:
                raise KeyError(f"Currency '{currency_from}' not found in rates")
            amount = amount / self.rates[currency_from]
        
        if currency_to not in self.rates:
            raise KeyError(f"Currency '{currency_to}' not found in rates")
        
        amount = round(amount * self.rates[currency_to], 2)
        print('{} {} = {} {}'.format(initial, currency_from, amount, currency_to))

if __name__ == "__main__":
    url = 'http://api.exchangeratesapi.io/v1/latest'
    api_key = 'aaa99ef30ca7684426a1abf5f3197a65'
    
    c = CurrencyConverter(url, api_key)
    currency_from = input("From: ")
    currency_to = input("To: ")
    amount = int(input("Amount: "))

    try:
        c.convert_currency(currency_from, currency_to, amount)
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
