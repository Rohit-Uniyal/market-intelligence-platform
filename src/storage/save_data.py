import os
import pandas as pd


def save_to_csv(tweets, file_name):

    os.makedirs("output", exist_ok=True)

    output_path = f"output/{file_name}.csv"

    new_df = pd.DataFrame(tweets)

    if os.path.exists(output_path):

        existing_df = pd.read_csv(output_path)

        df = pd.concat(
            [existing_df, new_df],
            ignore_index=True
        )

        df.drop_duplicates(
            subset=["tweet"],
            inplace=True
        )

    else:

        df = new_df

    df.to_csv(
        output_path,
        index=False
    )

    print(f"\nCSV saved successfully : {output_path}")
    print(f"Total Tweets Stored : {len(df)}")

    return df