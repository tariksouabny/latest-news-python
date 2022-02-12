import argparse
import util
import logging
from check_arguments import ArgumentTypeNotValidError, are_arguments_valid
import argparse, logging

util.inherit_logging_config()

@util.log_start_end_func
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="type_", help="Is the request a search or a retreival for the top headlines?", type=str)
    parser.add_argument(dest="search_keyword", help="Search keyword(s), if possible",nargs="?" , default="")
    #add a help text argument
    parser.add_argument(dest="help_", help="Does the user need the help info?", nargs="?", default="")
    arguments = parser.parse_args()
    logging.debug(str(arguments))
    are_arguments_valid(arguments)
    return arguments

parse_arguments()