import os, logging, sys
import util
from util import
class ArgumentTypeNotValidError(BaseException):
    pass

class SearchKeywordNotValid(BaseException):
    pass


@util.log_start_end_func
def are_arguments_valid(arguments):
    argument_type_ = arguments.type_
    argument_search_keywowrd = arguments.search_keyword
    valid = True
    
    #check if the argyment type is valid
    try:
        if argument_type_.lower() not in ['feed', "search"]:
            raise ArgumentTypeNotValidError("Please enter either 'search' or 'feed', to search news, or get the top feed")
    except ArgumentTypeNotValidError as e:
        sys.stderr.write(e)
        valid=False

    try:
        if argument_search_keywowrd == "" and argument_type_ =="search":
            raise SearchKeywordNotValid("Please enter a search keyword, if you are willing to search")
    except SearchKeywordNotValid as e:
        sys.stderr.write(e)
        valid=False
    
    if not valid:
        print_help_text()
        

@util.log_start_end_func
def print_help_text():
    pass