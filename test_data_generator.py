import random
from typing import List
import numpy as np


def uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1


def unique_id_set(length: int) -> List[int]:
    data_set = []
    for element in range(length):
        data_set.append(next(uniqueid()))
    return ["product_id"] + data_set


os = {"android": 1,
      "ios": 2,
      "linux": 3,
      "windows": 4}
os_match = {"laptop": {2: .1, 3: .1, 4: .8},
            "phone": {1: .7, 2: .3},
            "discs": None,
            "tv": None
            }

storage = {100: 4,
           500: 1,
           1000: 2,
           2000: 3}
storage_match = {"laptop": {1: .3, 2: .4, 3: .2, 4: .1},
                 "phone": {1: .4, 2: .3, 4: .1, 3: .2},
                 "discs": {1: .25, 2: .25, 4: .25, 3: .25},
                 "tv": None
                 }

aspect = {15: 1,
          13: 2,
          17: 3,
          5: 4,
          6: 5,
          24: 6,
          32: 7}
aspect_match = {"laptop": {1: .3, 2: .4, 3: .3},
                "phone": {4: .4, 5: .6},
                "discs": None,
                "tv": {6: .6, 7: .4}
                }

resolution = {3100_1400: 1,  # cell
              2400_1080: 2,  # cell
              1900_1080: 3,  # lap tv
              2500_1060: 4,  # tv lap
              3800_2100: 5}  # tv lap
resolution_match = {"laptop": {3: .6, 4: .3, 5: .1},
                    "phone": {1: .4, 2: .6},
                    "discs": None,
                    "tv": {3: .4, 4: .3, 5: .3}
                    }

colour = {"a": 1,
          "b": 2,
          "c": 3,
          "d": 4,
          "e": 5}
colour_match = {"laptop": "random",
                "phone": "random",
                "discs": "random",
                "tv": "random"
                }

camera = {"100Mpx": 1,
          "200Mpx": 2,
          "300Mpx": 3}
camera_match = {"laptop": None,
                "phone": {1: .3, 2: .3, 3: .4},
                "discs": None,
                "tv": None
                }

interface = {"sata": 1,
             "m2": 2,
             "oth": 3}
interface_match = {"laptop": None,
                   "phone": None,
                   "discs": {1: .2, 2: .6, 3: .2},
                   "tv": None
                   }

smart = {1: 1, 0: 0}
smart_match = {"laptop": None,
               "phone": None,
               "discs": None,
               "tv": "random"
               }


class DataSet(object):
    def __init__(self):
        self.laptop = "laptop"
        self.phone = "phone"
        self.discs = "discs"
        self.tv = "tv"


def generate_from_matching(matching: dict, attributes: dict, category: str, number_of_products: int,
                           attribute_name: str) -> List:
    inverted_attributes = {v: k for k, v in attributes.items()}
    for k, v in matching.items():
        if k == category:
            if v is None:
                continue
            else:
                if "random" in v:
                    random_attributes = []
                    for key in inverted_attributes.keys():
                        random_attributes.append(key)
                    return [attribute_name] + random.choices(random_attributes, k=number_of_products)
                else:
                    attributes_displacement = v
                    attributes_indexes = []
                    attributes_weights = []
                    for k, v in attributes_displacement.items():
                        attributes_indexes.append(k)
                        attributes_weights.append(v * 100)
                    return [attribute_name] + random.choices(population=attributes_indexes, weights=attributes_weights,
                                                             k=number_of_products)


def gen_matrix(set_of_data: List) -> np.matrix:
    tmp = []
    for data_set in set_of_data:
        if data_set:
            tmp.append(data_set)
    return np.transpose(np.array(tmp))


def generate_test_data(categories: List, length: int) -> dict[str: np.matrix]:
    categories_len = len(categories)
    products_in_set = int(length / categories_len)
    result_dict = {}
    for category in categories:
        id_set = unique_id_set(products_in_set)
        os_set = generate_from_matching(os_match, os, category, products_in_set, "os")
        storage_set = generate_from_matching(storage_match, storage, category, products_in_set, "storage")
        aspect_set = generate_from_matching(aspect_match, aspect, category, products_in_set, "aspect")
        resolution_set = generate_from_matching(resolution_match, resolution, category, products_in_set, "resolution")
        smart_set = generate_from_matching(smart_match, smart, category, products_in_set, "smart")
        camera_set = generate_from_matching(camera_match, camera, category, products_in_set, "camera")
        interface_set = generate_from_matching(interface_match, interface, category, products_in_set, "interface")
        colour_set = generate_from_matching(colour_match, colour, category, products_in_set, "colour")
        data_set = [id_set, os_set, storage_set, aspect_set, resolution_set, smart_set, camera_set, interface_set,
                    colour_set]
        result_dict[category] = gen_matrix(data_set)
    return result_dict


def generate_csv(data_dict: dict[str: np.array]) -> None:
    for k, v in data_dict.items():
        print(v)
        import pandas as pd

        df = pd.DataFrame(v)
        df.to_csv(f"{k}.csv", sep=",", index=False, header=False)


data = generate_test_data(["laptop", "phone", "discs", "tv"], 2000)
generate_csv(data)
