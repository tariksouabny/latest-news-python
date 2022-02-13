import check_arguments, parse_arguments, util
import logging, pprint
#TODO: define a way to get a token from check_arguments that defines whether or not to execute this file
#TODO: define a way to get a token from check_arguments that defines whether to search or give a feed
util.inherit_logging_config()

import requests, json

URL = "https://free-news.p.rapidapi.com/v1/search"

#querystring = {"q":"Jazz","lang":"en"}

HEADERS = {
    'x-rapidapi-host': "free-news.p.rapidapi.com",
    'x-rapidapi-key': "f67acd1fbamsh537007e203f8ab5p12c2b5jsna64615480c4b"
    }

#response = requests.request("GET", url, headers=headers, params=querystring)

def search_func(search_keyword):
    querystring = {"q": f"{search_keyword.lower()}", "lang": "en"}
    response = requests.get("GET", URL, headers=HEADERS, params=querystring)
    response_dict = json.loads(response.text)
    for article in response_dict['articles']:
        print(util.format_search_article(article))


def feed_func():
    pass

def main():
    arguments = parse_arguments.parse_arguments()
    valid, argument_type_, argument_search_keyword = check_arguments.are_arguments_valid(arguments)
    if valid:
        dict_lookup = {
            'search': lambda x: search_func(argument_search_keyword),
            'feed': feed_func,

        }
        logging.debug(dict_lookup[argument_type_])
        dict_lookup[argument_type_](...)
        
if __name__ == "__main__":
    main()

#TODO: Find a way to access a feed