import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="type", help="Is the request a search or a retreival for the top headlines?")
    parser.add_argument(dest="search_keyword", help="Search keyword(s). If retreiving top headlines, put in 0")

    arguments = parser.parse_args()
    return arguments