import requests
import logging
from cache_handler import save_to_cache, load_from_cache
import config

def fetch_data_from_aneel(resource_id, max_id):
    cached_data = load_from_cache()
    if cached_data is not None:
        return cached_data

    base_url = "https://dadosabertos.aneel.gov.br/api/3/action/datastore_search_sql"
    sql_query = f'SELECT * from "{resource_id}" WHERE _id > {max_id}'

    try:
        response = requests.get(base_url, params={'sql': sql_query})
        response.raise_for_status()
        data = response.json()['result']['records']
        save_to_cache(data)
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching data from API: {e}")
        return None
