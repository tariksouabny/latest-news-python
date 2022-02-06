import argparse
import util
import logging

@util.log_start_end_func
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="type_", help="Is the request a search or a retreival for the top headlines?", type=str)
    parser.add_argument(dest="search_keyword", help="Search keyword(s), if possible",nargs="?" , default="")
    arguments = parser.parse_args()
    logging.debug(str(arguments))
    return arguments

parse_arguments()