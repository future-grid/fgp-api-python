import logging
from controller.client import Client
from controller.store import Store


class ApiClient:
    _client: Client = None
    store: Store = None

    def __init__(self, url, application):
        self._client = Client(url, application)
        self.store = Store(self._client)

if __name__ == 'fgp':
    # create logger
    logger = logging.getLogger('fgp')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    logger.info('Configured logger')