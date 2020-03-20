import datetime
import fgp
client = fgp.ApiClient(url='http://localhost:8082', application='ada')
df = client.store.get_data(
    device_type='meter',
    store_name='meterPqStore',
    date_from=datetime.datetime(year=2019, month=10, day=1),
    date_to=datetime.datetime(year=2019, month=10, day=2),
    fields=['voltageA', 'currentA'],
    devices=['9000000002_9000000002']
)

print(df)