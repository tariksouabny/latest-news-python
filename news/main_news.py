import util_news, parse_arguments, check_arguments, logging, requests
@util_news.log_start_end_func
def if_feed(_):
    """
    Feed - Generates the top results without a need to search

    Operates by the normal search function, but instead of using a user-supplied
    search keyword, the feed function searches for the top articles containing the letter "a"
    
    Yes, it's very creative.
    """
    
    if_search("a")
@util_news.log_start_end_func
def if_search(search_keyword):
    url = "https://free-news.p.rapidapi.com/v1/search"
    querystring = {"q": str(search_keyword),"lang":"en"}
    headers = {
        'x-rapidapi-host': "free-news.p.rapidapi.com",
        'x-rapidapi-key': "f67acd1fbamsh537007e203f8ab5p12c2b5jsna64615480c4b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    news_list = util_news.get_news(response._content)
    util_news.print_news(news_list)

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