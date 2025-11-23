import kopf
from airflow_client.client.api.connection_api import ConnectionApi
from airflow_client.client.model.connection import Connection
from config import api_client

connections_api = ConnectionApi(api_client=api_client)
@kopf.on.create('airflow.drfaust92', 'v1beta1', 'connections')
def create_connection(meta, spec, namespace, logger, body, **kwargs):
    var_name = meta.get('name')
    var_conn_type = spec.get('connType')
    var_description = spec.get('description', '')

    logger.info(f"Creating Airflow Connection: {var_name} with value: [MASKED] and description: {var_description}")
    try:
        connection = Connection(
            key=var_name,
            value=var_conn_type,
            description=var_description
        )
        connections_api.post_connections(connection)
        return {'message': f'Connection {var_name} created successfully.'}
    except Exception as e:
        logger.error(f"Failed to create Airflow Connection {var_name}: {e}")
        return {'error': f'Failed to create connection {var_name}: {e}'}
    
@kopf.on.delete('airflow.drfaust92', 'v1beta1', 'connections')
def delete_connection(meta, spec, namespace, logger, body, **kwargs):
    var_name = meta.get('name')

    logger.info(f"Deleting Airflow Connection: {var_name}")
    try:
        connections_api.delete_connection(
            connection_key=var_name
            )
        return {'message': f'Connection {var_name} deleted successfully.'}
    except Exception as e:
        # Ignore 404 errors - connection already doesn't exist
        if '404' in str(e) or 'Not Found' in str(e):
            logger.info(f"Connection {var_name} already deleted or doesn't exist")
            return {'message': f'Connection {var_name} already deleted or doesn\'t exist.'}
        logger.error(f"Failed to delete Airflow Connection {var_name}: {e}")
        return {'error': f'Failed to delete connection {var_name}: {e}'}
    
@kopf.on.update('airflow.drfaust92', 'v1beta1', 'connections')
def update_connection(meta, spec, namespace, logger, body, **kwargs):
    var_name = meta.get('name')
    var_conn_type = spec.get('connType')
    var_description = spec.get('description', '')

    logger.info(f"Updating Airflow Connection: {var_name} with value: [MASKED] and description: {var_description}")
    try:
        connection = Connection(
            key=var_name,
            value=var_conn_type,
            description=var_description
        )
        connections_api.patch_connection(
            connection_key=var_name,
            connection=connection
            )
        return {'message': f'Connection {var_name} updated successfully.'}
    except Exception as e:
        logger.error(f"Failed to update Airflow Connection {var_name}: {e}")
        return {'error': f'Failed to update connection {var_name}: {e}'} 