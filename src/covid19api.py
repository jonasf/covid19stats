import requests
import json


class Covid19Api:

    def __init__(self):
        self.api_base_url = "https://api.covid19api.com/"

    def get_stats_for_country(self, country):
        stats = []
        response = requests.get(self.api_base_url + 'total/country/' + country)
        stats.extend(json.loads(response.text))

        print('Fetched ' + str(len(stats)) + ' data points')

        return stats
