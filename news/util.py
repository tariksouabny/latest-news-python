import logging

def inherit_logging_config():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def log_start_end_func(func):
    inherit_logging_config()
    def log(*args, **kwargs):

        #TODO: Add a way to log the **kwargs
        logging.debug(f"Start of {func.__name__}{args}")
        return_val = func(*args, **kwargs) #if kwargs is not None else func(*args)
        logging.debug(f"End of {func.__name__}{args}")
    return log

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def log_start_end_func(func):
    def log(*args, **kwargs):
        # TODO: Add a way to log **kwargs as well
        logging.debug(f"Start of {func}{args}")
        return_val = func(*args, **kwargs)
        logging.debug(f"End of {func}{args}")
        return return_val
    return log
