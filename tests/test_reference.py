import fgp
from fgp.model.model import FGModel, FGField


def test_get_schema_reference(client: fgp.ApiClient):
    schema = client.reference.get_schema('event_reference')
    assert type(schema) is FGModel


def test_query_reference(client: fgp.ApiClient):
    rows = client.reference.query(
        reference_name='event_reference',
        query='eventState=="NEW";calcConfidence>=0.6;isExported==false',
        order_by="timeKey",
        limit=100,
        page=0
    )
    assert type(rows) is list
