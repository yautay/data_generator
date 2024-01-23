# Zaczynamy od załadowania bibliotek. Te najpopularniejsze to
# pandas - do pracy z danymi
# matplotlib - do rysowania wykresow
# sklearn - zawierający gotowe funkcje modelujące dane

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

# tutaj ładujemy dane do obiektu data frame z biblioteki pandas
# plik CSV nie posiada nagłówka dlatego header=None
# kolumnom nadajemy nazwy korzystając z parametru names
# W skryptach ML dane trzeba skądś pobrać, stad znajomość polecenia
# read_csv jest super przydatna

iris = pd.read_csv(r"C:\Users\m.pielaszkiewicz\PycharmProjects\test\auto-mpg.csv")

iris.head()

# można sprawdzic rozmiar wczytanego zbioru
# jeśli obiekt ma więcej wymiarów, to można niezależnie sprawdzać każdy z nich
# W skryptach ML, często trzeba zainicjować rozmiary innych obiektów zależnie od
# rozmiaru danych wejściowych. Robi się to korzystając własnie z właściwości shape

iris.shape
iris.shape[0]
iris.shape[1]

#
#
# # Zamiast analizować każdą parę niezależnie można generować tzw. scatter matrix,
# # czyli gotową macierz z wykresami dla każdej pary właściwości
# # tutaj wykorzystujemy funkcję scatter_matrix zaimplementowaną w pandas...
# # Do wyznaczenia koloru skorzystaliśmy z funkcji apply. Pozwala ona wywołać prostą funkcję na rzecz
# # każdego wiersza z data frame lub serii danych
# pd.plotting.scatter_matrix(iris, figsize=(8, 8),
#                            color=iris['species'].apply(lambda x: colors[x]))
# plt.show()
#
# # ... a tutaj podobny wykres generowany przez funkcję pairplot z modułu seaborn
# import seaborn as sns
#
# sns.set()
# sns.pairplot(iris, hue="species")
