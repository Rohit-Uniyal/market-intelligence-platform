import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def analyze_keywords(df):
    """
    Analyze the most important keywords from tweets
    using the TF-IDF algorithm.
    """

    print("\nStarting Keyword Analysis...")

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=50
    )

    tfidf_matrix = vectorizer.fit_transform(df["tweet"])

    feature_names = vectorizer.get_feature_names_out()

    scores = tfidf_matrix.sum(axis=0).A1

    keyword_df = pd.DataFrame({
        "keyword": feature_names,
        "score": scores
    })

    keyword_df = keyword_df.sort_values(
        by="score",
        ascending=False
    )

    keyword_df.to_csv(
        "output/trending_keywords.csv",
        index=False
    )

    print("Keyword analysis completed successfully.")

    return keyword_df