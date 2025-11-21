import os
import airflow_client.client as client

AIRFLOW_HOST = os.getenv("AIRFLOW_HOST")
if not AIRFLOW_HOST:
	raise RuntimeError("Environment variable AIRFLOW_HOST must be set")

AIRFLOW_USERNAME = os.getenv("AIRFLOW_USERNAME", "admin") # temp until i abstract the auth logic for other vendors as well
AIRFLOW_PASSWORD = os.getenv("AIRFLOW_PASSWORD", "admin") # temp until i abstract the auth logic for other vendors as well

if AIRFLOW_USERNAME and AIRFLOW_PASSWORD:
	configuration = client.Configuration(host=AIRFLOW_HOST, username=AIRFLOW_USERNAME, password=AIRFLOW_PASSWORD)
else:
	raise RuntimeError("Environment variable AIRFLOW_USERNAME and AIRFLOW_PASSWORD must be set")  # temp until i abstract the auth logic for other vendors as well

api_client = client.ApiClient(configuration=configuration)