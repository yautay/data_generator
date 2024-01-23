import os
from sklearn.preprocessing import MinMaxScaler
from data.path import PATH_DATA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


laptops_data = pd.read_csv(os.path.join(PATH_DATA, "laptop.csv"))
discs_data = pd.read_csv(os.path.join(PATH_DATA, "discs.csv"))
phone_data = pd.read_csv(os.path.join(PATH_DATA, "phone.csv"))
tv_data = pd.read_csv(os.path.join(PATH_DATA, "tv.csv"))

data_frames = [laptops_data, discs_data, phone_data, tv_data]

products_data = pd.concat(data_frames, sort=False)
keys = products_data.keys().values.tolist()
keys.remove("product_id")

scaler = MinMaxScaler()
# normalizuje dane do zakresu 0/1 nie uwzględniając id produktu
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.fit_transform

products_data[keys] = scaler.fit_transform(products_data[keys])

# rysuję macierz powiązań (?) za pomocą pandasa
# https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html

pd.plotting.scatter_matrix(products_data[keys], alpha=0.2)
plt.show()

# narazie gówno widać, muszę dodać klasyfikację


