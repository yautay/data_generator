class DataSeriesConfig(object):
    os = {"android": 1, "ios": 2, "linux": 3, "windows": 4}
    os_match = {
        "laptop": {2: 0.1, 3: 0.1, 4: 0.8},
        "phone": {1: 0.7, 2: 0.3},
        "discs": None,
        "tv": None,
    }

    storage = {100: 4, 500: 1, 1000: 2, 2000: 3}
    storage_match = {
        "laptop": {1: 0.3, 2: 0.4, 3: 0.2, 4: 0.1},
        "phone": {1: 0.4, 2: 0.3, 4: 0.1, 3: 0.2},
        "discs": {1: 0.25, 2: 0.25, 4: 0.25, 3: 0.25},
        "tv": None,
    }

    aspect = {15: 1, 13: 2, 17: 3, 5: 4, 6: 5, 24: 6, 32: 7}
    aspect_match = {
        "laptop": {1: 0.3, 2: 0.4, 3: 0.3},
        "phone": {4: 0.4, 5: 0.6},
        "discs": None,
        "tv": {6: 0.6, 7: 0.4},
    }

    resolution = {
        3100_1400: 1,  # cell
        2400_1080: 2,  # cell
        1900_1080: 3,  # lap tv
        2500_1060: 4,  # tv lap
        3800_2100: 5,
    }  # tv lap
    resolution_match = {
        "laptop": {3: 0.6, 4: 0.3, 5: 0.1},
        "phone": {1: 0.4, 2: 0.6},
        "discs": None,
        "tv": {3: 0.4, 4: 0.3, 5: 0.3},
    }

    colour = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    colour_match = {
        "laptop": "random",
        "phone": "random",
        "discs": "random",
        "tv": "random",
    }

    camera = {"100Mpx": 1, "200Mpx": 2, "300Mpx": 3}
    camera_match = {
        "laptop": None,
        "phone": {1: 0.3, 2: 0.3, 3: 0.4},
        "discs": None,
        "tv": None,
    }

    interface = {"sata": 1, "m2": 2, "oth": 3}
    interface_match = {
        "laptop": None,
        "phone": None,
        "discs": {1: 0.2, 2: 0.6, 3: 0.2},
        "tv": None,
    }

    smart = {1: 1, 0: 0}
    smart_match = {"laptop": None, "phone": None, "discs": None, "tv": "random"}
