import logging

def setup_logger():
    logging.basicConfig(filename='aneel_data_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%('
                                                                                  'message)s')
