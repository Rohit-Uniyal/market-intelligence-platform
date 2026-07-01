import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.scraper.browser import get_browser
from src.scraper.constants import BASE_URL, TARGET_TWEETS
from src.scraper.parser import parse_tweet


def build_search_url(hashtag):

    hashtag = hashtag.replace("#", "%23")

    return f"{BASE_URL}?q={hashtag}&src=typed_query&f=live"


def scrape_hashtag(hashtag):

    driver = get_browser()

    url = build_search_url(hashtag)

    print(f"\nOpening {url}")

    driver.get(url)

    # Allow X to fully load
    time.sleep(5)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    all_tweets = []
    unique_tweets = set()

    scroll_count = 0

    while len(all_tweets) < TARGET_TWEETS:

        articles = driver.find_elements(By.TAG_NAME, "article")

        print(f"Visible Tweets : {len(articles)}")

        for article in articles:

            try:

                tweet = parse_tweet(article, hashtag)

                tweet_text = tweet["tweet"].strip()

                if tweet_text and tweet_text not in unique_tweets:

                    unique_tweets.add(tweet_text)

                    all_tweets.append(tweet)

                    if len(all_tweets) % 25 == 0:

                        print(f"Collected Tweets : {len(all_tweets)}")

            except Exception as e:

                continue

        print(f"Current Total : {len(all_tweets)}")

        if len(all_tweets) >= TARGET_TWEETS:

            print("\nTarget reached.")
            break

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        scroll_count += 1

        print(f"Scroll Number : {scroll_count}")

        # Wait for new tweets to load
        time.sleep(3)

        if scroll_count >= 500:

            print("\nMaximum scroll limit reached.")
            break

    driver.quit()

    return all_tweets