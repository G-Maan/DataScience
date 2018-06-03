import pandas as pd
import os
import numpy as np


class CsvDataLoader:
    def __init__(self, data_dirpath):
        self._data_dirpath = data_dirpath

    def csv_to_df(self, filename):
        path = os.path.join(self._data_dirpath, filename)
        df = pd.read_csv(path, sep=',')
        df['region'] = df['region'].apply(str.strip)
        df = df.drop(columns=['Unnamed: 0'])
        df['nieustalona'] = pd.to_numeric(df['nieustalona'], errors='coerce')
        year = int(filename.split('_')[3])
        df = df.assign(year=year)
        c = df.columns.tolist()
        new_col_order = [c[0]] + [c[-1]] + c[1:-1]

        return df[new_col_order]

    def read_datasets(self):
        filenames = [p for p in os.listdir(self._data_dirpath) if p.startswith('regions_pl_uro')]
        return pd.concat([self.csv_to_df(fn) for fn in filenames])


if __name__ == '__main__':
    loader = CsvDataLoader('/home/adek/studia/kod/stopien_2_semestr_1/PUM/task_09/data/')
    df = loader.read_datasets()
    # import ipdb; ipdb.set_trace()
