import os
import airflow_client.client as client

AIRFLOW_HOST = os.getenv("AIRFLOW_HOST")
if not AIRFLOW_HOST:
	raise RuntimeError("Environment variable AIRFLOW_HOST must be set")

AIRFLOW_USERNAME = os.getenv("AIRFLOW_USERNAME")
AIRFLOW_PASSWORD = os.getenv("AIRFLOW_PASSWORD")
AIRFLOW_ACCESS_TOKEN = os.getenv("AIRFLOW_ACCESS_TOKEN")

if AIRFLOW_USERNAME and AIRFLOW_PASSWORD:
	configuration = client.Configuration(host=AIRFLOW_HOST, username=AIRFLOW_USERNAME, password=AIRFLOW_PASSWORD)
elif AIRFLOW_ACCESS_TOKEN:
	configuration = client.Configuration(host=AIRFLOW_HOST, access_token=AIRFLOW_ACCESS_TOKEN)
else:
	raise RuntimeError("Environment variable (AIRFLOW_USERNAME and AIRFLOW_PASSWORD) or AIRFLOW_ACCESS_TOKEN must be set")

api_client = client.ApiClient(configuration=configuration)