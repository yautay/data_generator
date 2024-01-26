import os
import time
from functools import wraps
from alive_progress import alive_bar
from sklearn.preprocessing import MinMaxScaler
from data.path import PATH_DATA
import pandas as pd
import json

import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def parse_netcorner_json_data_to_df(path: str, to_csv: str or None = None) -> pd.DataFrame:
    with open(path, "r") as json_file:
        ai_test_data_json = json.load(json_file)
        parsed_ai_test_data = []
        for element in ai_test_data_json:
            attributes = element.pop("attributes")
            for attribute in attributes:
                element[attribute["name"]] = attribute["value"]
            parsed_ai_test_data.append(element)
        ai_test_data_frame = pd.DataFrame(parsed_ai_test_data)
        if to_csv:
            ai_test_data_frame.to_csv(to_csv)
        return ai_test_data_frame


@timeit
def generate_df_value_indexes(dataframe: pd.DataFrame) -> dict:
    value_index = {}
    index = 1
    keys = dataframe.keys()
    for key in keys:
        unique_values = dataframe[key].unique()
        for value in unique_values:
            if value not in value_index:
                if value == "nan":
                    value_index[value] = None
                value_index[value] = index
            index += 1
    return value_index


@timeit
def serialize_data(df: pd.DataFrame, index_dict: dict, to_csv: str or None = None) -> pd.DataFrame:
    keys = df.keys()
    total_items = df.shape[0] * df.shape[1]
    with alive_bar(total_items) as bar:
        for key in keys:
            for item in df[key].values:
                if item in index_dict.keys():
                    df.loc[df[key] == item, key] = index_dict[item]
                bar()
            df[key].fillna(0, inplace=True)
    if to_csv:
        df.to_csv(to_csv)
    return df


# test_data_frame = parse_netcorner_json_data_to_df(os.path.join(PATH_DATA, "ai_test_data.json"))
test_data_frame = pd.read_csv(os.path.join(PATH_DATA, "parsed_ai-test-data.csv"), low_memory=False)
value_indexes = generate_df_value_indexes(test_data_frame.iloc[:, 3:])
serialized_df = serialize_data(test_data_frame, value_indexes, to_csv=os.path.join(PATH_DATA, "indexed_ai-test-data.csv"))

#
# data_frames = [laptops_data, discs_data, phone_data, tv_data]
#
# products_data = pd.concat(data_frames, sort=False)
# keys = products_data.keys().values.tolist()
# keys.remove("product_id")
#
# scaler = MinMaxScaler()
# # normalizuje dane do zakresu 0/1 nie uwzględniając id produktu
# # https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.fit_transform
#
# products_data[keys] = scaler.fit_transform(products_data[keys])
#
# print(products_data.head())
#
# # rysuję macierz powiązań (?) za pomocą pandasa
# # https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html
#
# # pd.plotting.scatter_matrix(products_data[keys], alpha=0.2)
# # plt.show()
#
# # narazie gówno widać....
# X = products_data.iloc[:, 1:-1]


