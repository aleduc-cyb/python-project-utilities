import logging
from configparser import ConfigParser

LOGFILE_NAME = "history.log"

def configure_logger():
    #now we will Create and configure logger 
    logging.basicConfig(filename="history.log", 
					format='%(asctime)s - %(levelname)s - %(message)s', 
					filemode='a') 

    #Let us Create an object 
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger

def clean_logger():
    with open(LOGFILE_NAME, 'w'):
        pass

def read_config(config_file = 'config.ini'):
    config_object = ConfigParser()
    config_object.read(config_file)
    if len(config_object) > 1:
        return config_object
    else:
        return False
