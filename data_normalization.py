import os
from sklearn.preprocessing import MinMaxScaler
from data.path import PATH_DATA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

categorization = {
    1: "laptop",
    2: "phone",
    3: "discs",
    4: "tv"
}

laptops_data = pd.read_csv(os.path.join(PATH_DATA, "laptop.csv"))
laptops_data.insert(1, "category", np.full((laptops_data.shape[0]), 1))
discs_data = pd.read_csv(os.path.join(PATH_DATA, "discs.csv"))
discs_data.insert(1, "category", np.full((laptops_data.shape[0]), 3))
phone_data = pd.read_csv(os.path.join(PATH_DATA, "phone.csv"))
phone_data.insert(1, "category", np.full((laptops_data.shape[0]), 2))
tv_data = pd.read_csv(os.path.join(PATH_DATA, "tv.csv"))
tv_data.insert(1, "category", np.full((laptops_data.shape[0]), 4))

data_frames = [laptops_data, discs_data, phone_data, tv_data]

products_data = pd.concat(data_frames, sort=False)
keys = products_data.keys().values.tolist()
keys.remove("product_id")

scaler = MinMaxScaler()
# normalizuje dane do zakresu 0/1 nie uwzględniając id produktu
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.fit_transform

products_data[keys] = scaler.fit_transform(products_data[keys])

print(products_data.head())

# rysuję macierz powiązań (?) za pomocą pandasa
# https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html

# pd.plotting.scatter_matrix(products_data[keys], alpha=0.2)
# plt.show()

# narazie gówno widać....
X = products_data.iloc[:, 1:-1]


