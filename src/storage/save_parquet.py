import os

import pandas as pd


def save_to_parquet(dataframe, file_name):

    os.makedirs("output", exist_ok=True)

    output_path = f"output/{file_name}.parquet"

    dataframe.to_parquet(
        output_path,
        index=False
    )

    print(f"\nParquet file saved : {output_path}")

    return output_path