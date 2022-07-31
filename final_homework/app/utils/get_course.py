import requests

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
response = requests.get(url)
data = response.json()
dollar_exchange_rate = data[25]['rate']
print(dollar_exchange_rate)

