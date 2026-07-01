from src.scraper.constants import HASHTAGS, TARGET_TWEETS
from src.scraper.twitter_scraper import scrape_hashtag

from src.storage.save_data import save_to_csv
from src.storage.save_parquet import save_to_parquet

from src.processing.clean_data import clean_tweets

from src.analysis.keyword_analysis import analyze_keywords
from src.analysis.visualization import create_visualizations


def main():

    print("=" * 60)
    print("MARKET INTELLIGENCE PLATFORM")
    print("=" * 60)

    all_tweets = []

    for hashtag in HASHTAGS:

        if len(all_tweets) >= TARGET_TWEETS:

            break

        print("\n" + "=" * 60)
        print(f"Searching : {hashtag}")
        print("=" * 60)

        tweets = scrape_hashtag(hashtag)

        all_tweets.extend(tweets)

        print(f"\nCurrent Total Tweets : {len(all_tweets)}")

    print("\nSaving Data...")

    raw_df = save_to_csv(
        all_tweets,
        "twitter_market_data"
    )

    cleaned_df = clean_tweets(raw_df)

    cleaned_df.to_csv(
        "output/twitter_market_data_cleaned.csv",
        index=False
    )

    save_to_parquet(
        cleaned_df,
        "twitter_market_data"
    )

    keyword_df = analyze_keywords(
        cleaned_df
    )

    create_visualizations(
        keyword_df,
        cleaned_df
    )

    print("\nTop 10 Trending Keywords\n")

    print(keyword_df.head(10))

    print("\nProject Completed Successfully")


if __name__ == "__main__":
    main()