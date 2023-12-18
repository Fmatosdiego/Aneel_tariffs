from data_fetcher import fetch_data_from_aneel
from data_processing import load_max_id_from_file, combine_and_save_data, update_max_id_to_file, update_cache
from send_email import send_email
from logger_config import setup_logger
import config


def main():
    setup_logger()
    max_id = load_max_id_from_file()
    new_data = fetch_data_from_aneel(config.resource_id, max_id)

    # Em main.py

    if new_data:
        max_id_in_new_data = max(d['_id'] for d in new_data)
        if max_id_in_new_data > max_id:
            update_cache(new_data)
            combine_and_save_data(new_data, config.excel_file_path)
            update_max_id_to_file(max_id_in_new_data)

            # Exemplo: Obtendo SigAgente do primeiro registro de new_data
            sig_agente_info = new_data[0]['SigAgente'] if 'SigAgente' in new_data[0] else "Não disponível"

            send_email("Novas Tarifas Cadastradas", f"{len(new_data)} novas tarifas cadastradas.",
                       "diego.matos@tradener.com.br", sig_agente_info)


if __name__ == "__main__":
    main()
