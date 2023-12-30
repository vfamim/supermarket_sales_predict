import pandas as pd
from pathlib import Path


def ingest_data(
    user: str,
    password: str,
    hostt: str,
    port: int,
    db: int,
    table_name: str
):
    # path
    csv_name = 'VendasSupermercados+CDI.csv.zip'
    project_path = Path().absolute().parent
    full_path = str(project_path) + '/data/external/'
    file_path = full_path + csv_name
    dataframe_iter = pd.read_csv(
        csv_full_path,
        chunksize=1000
        iterator=True
    )
    df = next(df_iter)
    return df


