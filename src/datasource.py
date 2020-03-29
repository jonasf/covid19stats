from influxdb import InfluxDBClient


class Datasource:

    def __init__(self):
        self.database_name = 'covid_stats'
        self.db_client = InfluxDBClient(host='localhost', port=8086)
        self.db_client.create_database(self.database_name)

    def save(self, stats):

        data_points = []

        for stat in stats:
            data_points.append(
                {
                    "measurement": stat["Status"],
                    "tags": {
                        "country": stat["Country"]
                    },
                    "time": stat["Date"],
                    "fields": {
                        "cases": stat["Cases"]
                    }
                }
            )

        self.db_client.switch_database(self.database_name)
        self.db_client.write_points(data_points)