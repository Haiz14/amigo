import os
from pathlib import Path
import pandas as pd

def return_file_name(path):
    return os.path.splitext(Path(path).name)[0]


def return_suffix(path):
    return Path(path).suffix

def read_pandas(file_path):
    
    suffix = return_suffix(file_path)

    if suffix == '.csv':
        df = pd.read_csv(file_path)
    elif suffix == '.xlsx':
        df = pd.read_excel(file_path)
    else : 
        print("unknown format \n", file_path)
        print("\n program quit")

    return df


if __name__ == "__main__":
    print(return_file_name
            ('tail/zimco.csv'))

