import os

import matplotlib.pyplot as plt


def create_visualizations(keyword_df, cleaned_df):

    os.makedirs("output", exist_ok=True)

    # -------------------------------
    # Top 10 Keywords
    # -------------------------------

    top_keywords = keyword_df.head(10)

    plt.figure(figsize=(10, 6))

    plt.bar(
        top_keywords["keyword"],
        top_keywords["score"]
    )

    plt.xticks(rotation=45)

    plt.title("Top 10 Trending Keywords")

    plt.xlabel("Keyword")

    plt.ylabel("TF-IDF Score")

    plt.tight_layout()

    plt.savefig(
        "output/top_keywords.png"
    )

    plt.close()

    # -------------------------------
    # Tweets Per Hashtag
    # -------------------------------

    hashtag_counts = cleaned_df["hashtag"].value_counts()

    plt.figure(figsize=(10, 6))

    plt.bar(
        hashtag_counts.index,
        hashtag_counts.values
    )

    plt.xticks(rotation=45)

    plt.title("Tweets Collected Per Hashtag")

    plt.xlabel("Hashtag")

    plt.ylabel("Tweet Count")

    plt.tight_layout()

    plt.savefig(
        "output/hashtag_distribution.png"
    )

    plt.close()

    print("\nCharts created successfully.")