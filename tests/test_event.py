import fgp

def test_update_event(client: fgp.ApiClient):
    client.event.update_event(
        device_type='meter',
        device_name='9000000001_9000000001',
        stream_name='update_event',
        data={
            'eventTs': 1570154400000,
            'deviceName': '9000000001_9000000001',
            'eventState': 'NEW',
            'incidentNo': None,
            'isExported': True,
            'comment': 'You have been updated!'
        }
    )