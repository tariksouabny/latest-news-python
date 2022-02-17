
import util_news, parse_arguments, check_arguments, logging
#TODO: Decorate all of these functions with the util.
def if_feed(_):
    pass

def if_search(search_keyword):
    pass

def main():
    arguments = parse_arguments.parse_arguments()
    valid, type_, search_keyword = check_arguments.are_arguments_valid(arguments)
    logging.debug(f"""
        variable valid = {valid}
        variable type_ = {type_}
        variable search_keyword = {search_keyword}
    """)
    if valid:
        lookup_values_feed = {
            "feed": if_feed,
            "search": if_search,

        }

        function_to_be_executed = lookup_values_feed[type_]
        logging.debug(function_to_be_executed)
        function_to_be_executed(search_keyword)




if __name__ == "__main__":
    main()