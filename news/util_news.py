import logging
#TODO: rename to util_news.py - std module already named after this flie
#TODO: Download this util_news.py file for task automation later
# TODO: Add a function that can wrap around other functions that are supposed to return a value.
#       However, if they do not return a value, then it logging.error(...)s the issue.  
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
