import json
import time
import os
import logging
import config


def save_to_cache(data):
    with open(config.cache_file, 'w') as f:
        json.dump(data, f)


def load_from_cache():
    if os.path.exists(config.cache_file) and time.time() - os.path.getmtime(config.cache_file) < config.cache_timeout:
        logging.info("Loading data from cache.")
        with open(config.cache_file, 'r') as f:
            return json.load(f)
    return None
