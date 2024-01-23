import os
from sklearn.preprocessing import MinMaxScaler
from data.path import PATH_DATA
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
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


products_data = products_data.replace({np.nan: -1})


# rysuję macierz powiązań (?) za pomocą pandasa
# https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html

# pd.plotting.scatter_matrix(products_data[keys], alpha=0.2)
# plt.show()

# narazie gówno widać....

# buduję dane wejściowe i dane oczekiwane w formie 2 datasetów
X = products_data.iloc[:, 2:-1]
y = products_data.loc[:, 'category']

# tworzę split testowy i do nauki (20%)
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=True)


# test z regersją liniową
# wyuczenie

lr = LinearRegression()
lr.fit(X_train, y_train)

#score_treningu

score = lr.score(X_test, y_test)
print("SCORE: ", score)

#test

prediction = pd.Series(lr.predict(X_test.iloc[:10, :]))
results_expected = pd.Series(y_test.iloc[:10]).reset_index(drop=True)

print(results_expected.compare(prediction, result_names=('expected', 'prediction')))

