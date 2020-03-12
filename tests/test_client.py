import json
import fgp
from fgp.controller.client import Client
from fgp.model.application import Application


def test_init():
    c = Client('http://some-url', 'myapp')
    assert c.base_url == 'http://some-url'
    assert c.application == 'myapp'


def test_application():
    with open('tests/data/application-adalon.json', 'rt') as f:
        d = json.load(f)
    a = Application.from_dict(d)

    assert a.name == 'adalon'
    assert len(a.references) == 3
    assert len(a.devices) == 4
