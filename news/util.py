import logging
#TODO: rename to util_news.py - std module already named after this flie

def inherit_logging_config():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def log_start_end_func(func):
    def log(*args, **kwargs):
        # TODO: Add a way to log **kwargs as well
        logging.debug(f"Start of {func.__name__}{args}")
        return_val = func(*args, **kwargs)
        logging.debug(f"End of {func.__name__}{args}")
        return return_val
    return log
