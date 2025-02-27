import json
from pathlib import Path

import polars as pl
from IPython.core.display_functions import display
from scipy.io import arff


def root_path() -> Path:
    return Path(r"..").resolve().absolute()


def data_path() -> Path:
    return root_path() / "data"


def load_data():
    data, meta = arff.loadarff(data_path() / "speeddating.arff")
    return pl.DataFrame(data), meta


def load_metadata():
    with open(data_path() / "40536.json", 'r') as file:
        data = json.load(file)
    return data


def polars_to_str(dataframe: pl.DataFrame, max_rows: int = -1, max_cols: int = -1) -> str:
    with pl.Config(tbl_rows=max_rows, tbl_cols=max_cols):
        result = str(dataframe)
    return result


def display_polars(dataframe: pl.DataFrame, max_rows: int = -1, max_cols: int = -1) -> None:
    with pl.Config(tbl_rows=max_rows, tbl_cols=max_cols):
        display(dataframe)
