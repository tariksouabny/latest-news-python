import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def log_start_end_func(func):
    def log(*args, **kwargs):
        # TODO: Add a way to log **kwargs as well
        logging.debug(f"Start of {func}{args}")
        return_val = func(*args, **kwargs)
        logging.debug(f"End of {func}{args}")
        return return_val
    return log
