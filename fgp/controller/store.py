import datetime
import pandas
from typing import List, Dict
from .client import Client
from fgp.utils import datetime_to_ms

class Store:

    _client: Client = None

    def __init__(self, client: Client):
        self._client = client

    @staticmethod
    def parse_store_data(data: Dict[str, Dict]) -> pandas.DataFrame:
        devices = list(data.keys())
        dfs: List[pandas.DataFrame] = list()
        for device_name in devices:
            df = pandas.DataFrame.from_dict(data[device_name].get('data'))
            cols_initial = [k for k in list(df.columns) if k != 'timestamp']
            df['device_name'] = device_name
            df['device_key'] = data[device_name].get('deviceKey')
            cols_final = ['device_name', 'device_key', 'timestamp'] + cols_initial

            dfs.append(df[cols_final])

        return pandas.concat(dfs)

    def get_data(
            self,
            device_type: str,
            store_name: str,
            date_from: datetime.datetime,
            date_to: datetime.datetime,
            fields: List[str],
            devices: List[str]
        ) -> List[Dict[str, str]]:
        payload = {
            'start': datetime_to_ms(date_from),
            'end': datetime_to_ms(date_to),
            'fields': fields,
            'devices': devices
        }
        res = self._client.post(route=f'{device_type}/{store_name}', data=payload)
        data = self.parse_store_data(res.json())
        return data
