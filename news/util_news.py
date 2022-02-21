import logging, json, os, pprint

def inherit_logging_config():
    logging.basicConfig(level=logging.CRITICAL, format="%(asctime)s - %(levelname)s - %(message)s")

#Decorator that logs the start and end of a function
def log_start_end_func(func):
    def log(*args, **kwargs):
        inherit_logging_config()
        logging.debug(f"Start of {func.__name__}{args}")
        return_val = func(*args, **kwargs)
        logging.debug(f"End of {func.__name__}{args}, returning {return_val}")
        return return_val
    return log


#decorator that asserts that a function returns a value
@log_start_end_func
def check_if_returns(func):
    def check(*args, **kwargs):
        logging.debug(f"RETURNING {func}{args}")
        if func(*args, **kwargs) == None:
            logging.error(f"{func}{args}{kwargs} returns None!")

#Function that takes a json response and returns a list of the pairs of descriptions to info
@log_start_end_func
def get_news(response):
    #takes a string json response
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
        news_list.append((description, info))
    return news_list

# 
def terminal_size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return w, h


@log_start_end_func
def print_news(news_list):
    #TODO: iterate through the news list, printing every element in the
    # description with the corresponding element in the info
    for description, info in news_list:
        for d, i in zip(description, info):
            pprint.pprint(f"{d}:     {i}")
            #print a delimeter of width of the terminal width - 1
            pprint.pprint("_"*(terminal_size()[0]-1))
        pprint.pprint("="*(2*terminal_size()[0]-2))