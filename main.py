import resources.variables  # noqa: F401
import resources.connections  # noqa: F401
import resources.pools  # noqa: F401
import datetime
import time
import kopf
import prometheus_client as prometheus

prometheus.start_http_server(9000)

@kopf.on.probe(id="now")
def get_current_timestamp(**kwargs):
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
