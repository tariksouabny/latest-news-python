import os, logging, sys
import util
'''
What we want to know:

    Make sure that the first argument is either 'feed' or 'search'
    if the second argument is an empty string, then the first argument has to be 'feed'
    If the first argument is "search", then the second argument has to have a value
'''
class ArgumentTypeNotValidError(TypeError):
    pass


@util.log_start_end_func
def are_arguments_valid(arguments):
    argument_type_ = arguments.type_
    argument_search_keywowrd = arguments.search_keyword
    valid = True
    
    #check if the argyment type is valid
    try:
        if arguments_type_.lower() not in ['feed', "search"]:
            raise ArgumentTypeNotValidError
    except ArgumentTypeNotValidError("Please enter either 'search' or 'feed', to search news, or get the top feed") as e:
        sys.stderr.write(str(e))

@util.log_start_end_func
def print_help_text():
    return None

print_help_text()
