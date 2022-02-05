import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
def log_start_end_func(func):
    def log(*args, **kwargs):

        #TODO: Add a way to log the **kwargs
        logging.debug(f"Start of {func}{args}")
        return_val = func(*args, **kwargs) if kwargs is not None else func(*args)
        logging.debug(f"End of {func}{args}")
    return log