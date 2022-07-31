import requests

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'


class CourseDollar:

    def get_course(url):
        response = requests.get(url)
        data = response.json()
        dollar_exchange_rate = data[25]['rate']
        return dollar_exchange_rate


dollar_rate = CourseDollar.get_course(url)
