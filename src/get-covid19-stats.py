from covid19api import Covid19Api
from datasource import Datasource
from datetime import datetime, timedelta

api = Covid19Api()
datasource = Datasource()
print('Downloading stats')
stats = api.get_stats_for_country('sweden',
                                  datetime.utcnow()
                                  - timedelta(hours=6, minutes=0))
print('Downloading stats completed')
print('Saving stats')
datasource.save(stats)
print('Saving stats completed')
