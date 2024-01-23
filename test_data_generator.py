import os.path
import random
from typing import List
import numpy as np
import pandas as pd
from data.config import DataSeriesConfig as dc
from data.path import PATH_DATA


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
        os_set = generate_from_matching(dc.os_match, dc.os, category, products_in_set, "os")
        storage_set = generate_from_matching(dc.storage_match, dc.storage, category, products_in_set, "storage")
        aspect_set = generate_from_matching(dc.aspect_match, dc.aspect, category, products_in_set, "aspect")
        resolution_set = generate_from_matching(dc.resolution_match,dc. resolution, category, products_in_set, "resolution")
        smart_set = generate_from_matching(dc.smart_match, dc.smart, category, products_in_set, "smart")
        camera_set = generate_from_matching(dc.camera_match, dc.camera, category, products_in_set, "camera")
        interface_set = generate_from_matching(dc.interface_match, dc.interface, category, products_in_set, "interface")
        colour_set = generate_from_matching(dc.colour_match, dc.colour, category, products_in_set, "colour")
        data_set = [id_set, os_set, storage_set, aspect_set, resolution_set, smart_set, camera_set, interface_set,
                    colour_set]
        result_dict[category] = gen_matrix(data_set)
    return result_dict


def generate_csv(data_dict: dict[str: np.array]) -> None:
    for k, v in data_dict.items():
        df = pd.DataFrame(v)
        df.to_csv(os.path.join(PATH_DATA, f"{k}.csv"), sep=",", index=False, header=False)


data = generate_test_data(["laptop", "phone", "discs", "tv"], 4000)
generate_csv(data)
