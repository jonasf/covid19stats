from influxdb import InfluxDBClient
import os


class Datasource:

    def __init__(self):
        self.database_name = 'covid_stats'
        self.db_client = InfluxDBClient(host=os.environ['INFLUXDB_HOST'], port=os.environ['INFLUXDB_PORT'])
        self.db_client.create_database(self.database_name)

    def save(self, stats):

        data_points = []

        for stat in stats:
            data_points.append(
                {
                    "measurement": "confirmed",
                    "tags": {
                        "country": stat["Country"]
                    },
                    "time": stat["Date"],
                    "fields": {
                        "cases": stat["Confirmed"]
                    }
                })
            data_points.append(
                {
                    "measurement": "recovered",
                    "tags": {
                        "country": stat["Country"]
                    },
                    "time": stat["Date"],
                    "fields": {
                        "cases": stat["Recovered"]
                    }
                })
            data_points.append(
                {
                    "measurement": "deaths",
                    "tags": {
                        "country": stat["Country"]
                    },
                    "time": stat["Date"],
                    "fields": {
                        "cases": stat["Deaths"]
                    }
                })

        print('Saving ' + str(len(data_points)) + ' data points to database')

        self.db_client.switch_database(self.database_name)
        self.db_client.write_points(data_points)
