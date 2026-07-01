import pandas as pd


def clean_tweets(df):

    # Remove duplicate tweets
    df = df.drop_duplicates(subset=["tweet"])

    # Remove empty tweets
    df = df[df["tweet"].str.strip() != ""]

    # Remove missing values
    df = df.dropna()

    # Reset index
    df.reset_index(drop=True, inplace=True)

    print(f"Total Tweets After Cleaning : {len(df)}")

    return df