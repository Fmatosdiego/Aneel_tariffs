import os
import pandas as pd
import logging
from cache_handler import save_to_cache


def load_max_id_from_file():
    try:
        with open('max_id.txt', 'r') as file:
            max_id = int(file.read().strip())
            return max_id
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0


def update_max_id_to_file(max_id):
    with open('max_id.txt', 'w') as file:
        file.write(str(max_id))


def load_existing_data(excel_file_path):
    try:
        if os.path.exists(excel_file_path):
            existing_data = pd.read_excel(excel_file_path)
            return existing_data['_id'].max()
        else:
            logging.info("Excel file does not exist. Creating a new file.")
            return 0
    except (FileNotFoundError, IOError):
        logging.warning("Error reading the Excel file.")
        return 0


def combine_and_save_data(new_data, excel_file_path):
    if new_data:
        new_df = pd.DataFrame(new_data)
        if not new_df.empty:
            existing_data = pd.read_excel(excel_file_path)
            combined_data = pd.concat([existing_data, new_df], ignore_index=True)
            combined_data.to_excel(excel_file_path, index=False)
            logging.info(f"{len(new_df)} new records added.")
        else:
            logging.info("No new data found.")


def update_cache(data):
    if data:
        max_id_in_new_data = max(d['_id'] for d in data)
        # Salva no cache apenas se os dados são mais recentes
        if max_id_in_new_data > load_max_id_from_file():
            save_to_cache(data)
            update_max_id_to_file(max_id_in_new_data)