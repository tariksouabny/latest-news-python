import logging, json

def inherit_logging_config():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def log_start_end_func(func):
    def log(*args, **kwargs):
        # TODO: Add a way to log **kwargs as well
        logging.debug(f"Start of {func.__name__}{args}")
        return_val = func(*args, **kwargs)
        logging.debug(f"End of {func.__name__}{args}, returning {return_val}")
        return return_val
    return log


#decorator to make sure that functions that need to return a vlue do so.
def check_if_returns(func):
    def check(*args, **kwargs):
        logging.debug(f"RETURNING {func}{args}")
        if func(*args, **kwargs) == None:
            logging.error(f"{func}{args}{kwargs} returns None!")


def get_news(response):
    response_dict = json.loads(response)

    articles = response_dict['articles']
    news_list = []
    for article in articles:
        info = [
                article['title'],
                article['author'],
                article['published_date'],
                article['link'],
                article['clean_url'],
                article['summary'],
                article['topic'],
                article['country'],
        ]

        description = [
                "Article Title",
                "Author",
                "Published Date",
                "Link",
                "Source URL",
                "Summary",
                "Topic",
                "Country Code",
        ]
        news_list.append((info, description))
    return news_list


def print_news(news_list):
    #TODO: iterate through the news list, printing every element in the
    #      description with the corresponding element in the info
