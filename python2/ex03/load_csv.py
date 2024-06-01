import pandas as pd


def load(path: str):
    try:
        df = pd.read_csv(path)
        if df.empty:
            return None
        print("Loading dataset of dimensions ", df.shape)
        return df
    except Exception as e:
        print("Error: ", e)
        return None
