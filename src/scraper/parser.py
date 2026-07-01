from selenium.webdriver.common.by import By


def parse_tweet(article, hashtag):
    """
    Extract tweet information from a single article element.
    """

    try:
        tweet_text = article.text.strip()
    except Exception:
        tweet_text = ""

    try:
        username = article.find_element(By.XPATH, ".//div[@dir='ltr']/span").text
    except Exception:
        username = ""

    try:
        timestamp = article.find_element(By.TAG_NAME, "time").get_attribute("datetime")
    except Exception:
        timestamp = ""

    return {
        "hashtag": hashtag,
        "username": username,
        "timestamp": timestamp,
        "tweet": tweet_text
    }