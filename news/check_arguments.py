import os, logging, sys
import util
from util import inherit_logging_config

inherit_logging_config()

class ArgumentTypeNotValidError(BaseException):
    pass

class SearchKeywordNotValid(BaseException):
    pass

@util.log_start_end_func
def print_help_text():

    """
    Prints Help Text
    """

    sys.stderr.write(
        """
        \n
        HELP TEXT:
        Argument 1: type_ - valid values are ["search" and "feed"] - used to indicate whether the user wants to search, or bring up the feed
        Argument 2: search_keyword - valid values are anything - used as a search keyword. If the search keyword spans multiple words, then encase this in quotes, "like this"
        Argument 3: help -  valid values are ["help"] - if one needs to bring up the help text. If one types "help" in any other arguments, the help text still shows up.
        \n
        """
    )


@util.log_start_end_func
def are_arguments_valid(arguments):
    """
    Function that takes CLI arguments; determines if they are valid or not.
    If the arguments are valid, then returns validity and arguments
    If the arguments are not valid, then returns validity

    """
    argument_type_ = arguments.type_
    argument_search_keyword = arguments.search_keyword
    argument_help_ = arguments.help_
    
    valid = True

    # if the user puts in "help" in any of the arguments, then the help text is automatically printed, and returns
    if "help" in [argument_type_, argument_search_keyword, argument_help_]:
        print_help_text()
        valid=None
    
    #check if the argyment type is valid
    try:
        if argument_type_.lower() not in ['feed', "search"]:
            raise ArgumentTypeNotValidError("Please enter either 'search' or 'feed', to search news, or get the top feed\n")
    except ArgumentTypeNotValidError as e:
        sys.stderr.write(str(e))
        valid=False


    try:
        if argument_search_keyword == "" and argument_type_ =="search":
            raise SearchKeywordNotValid("Please enter a search keyword, if you are willing to search\n")
    except SearchKeywordNotValid as e:
        sys.stderr.write(str(e))
        valid=False
    # if any of the cases above ocurred
    if not valid:
        print_help_text()
        return valid

    return valid, argument_type_, argument_search_keyword


