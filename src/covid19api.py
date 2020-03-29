import requests
import json


class Covid19Api:

    def __init__(self):
        self.api_base_url = "https://api.covid19api.com/"

    def get_stats_for_country(self, country, from_time):
        stats = []
        date_string = from_time.strftime("%Y-%m-%dT%H:%M:%SZ")

        deaths = requests.get(self.api_base_url +
                              "live/country/" +
                              country +
                              "/status/deaths/date/" +
                              date_string)
        stats.extend(json.loads(deaths.text))

        confirmed = requests.get(self.api_base_url +
                                 "live/country/" +
                                 country +
                                 "/status/confirmed/date/" +
                                 date_string)
        stats.extend(json.loads(confirmed.text))

        recovered = requests.get(self.api_base_url +
                                 "live/country/" +
                                 country +
                                 "/status/recovered/date/" +
                                 date_string)
        stats.extend(json.loads(recovered.text))

        return stats
