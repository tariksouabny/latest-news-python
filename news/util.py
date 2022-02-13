import logging

#TODO: Make the logging config inheritable

def inherit_logging_config():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def log_start_end_func(func):
    inherit_logging_config()
    def log(*args, **kwargs):
        # TODO: Add a way to log **kwargs as well
        logging.debug(f"Start of {func.__name__}{args}")
        return_val = func(*args, **kwargs)
        logging.debug(f"End of {func.__name__} returning {return_val}")
        return return_val
    return log
@log_start_end_func
def format_search_article(article):
    #make sure the article in in dictionary form
    try:
        if type(article) != dict:
            raise TypeError(
                f"Article must be of type dict, not of type {type(dict)}"
            )
    except TypeError as e:
        print(e)

    def make_authors_text():
        authors_text = "Authors: "
        for author in article['authors']:
            authors_text += author
        return authors_text
    make_authors_text()

    country_text = "Country: " + article['country']

    source_text = "Source: " + article['clean_url']

    link_text = "Link: " + article['link']

    published_date_text = "Date: " + article['published_date']

    title_text = "Title: " + article["title"]

    topic_text = "Topic: " + article['topic']

    summary_text = "Summary: \n" + article['summary']

    full_article_text = ""
    for text in [country_text, source_text, link_text, published_date_text, title_text, topic_text, summary_text]:
        full_article_text+=text
        full_article_text+="\n"
    full_article_text+='\n'*4
    return full_article_text