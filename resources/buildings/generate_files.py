import json

buildings = ["HEADQUARTER", "BARRACKS", "STABLE", "WORKSHOP", "ACADEMY", "SMITHY", "RALLY_POINT", "STATUE", "MARKET",
             "TIMBER_CAMP", "CLAY_PIT", "IRON_MINE", "FARM", "WAREHOUSE", "HIDING_PLACE", "WALL"]

requirements = [
    {},
    {"HEADQUARTER": 3},
    {"HEADQUARTER": 10, "BARRACKS": 5, "SMITHY": 5},
    {"HEADQUARTER": 10, "SMITHY": 10},
    {"HEADQUARTER": 20, "SMITHY": 20, "MARKET": 10},
    {"HEADQUARTER": 5, "BARRACKS": 1},
    {},
    {},
    {"HEADQUARTER": 3, "WAREHOUSE": 2},
    {},
    {},
    {},
    {},
    {},
    {},
    {"BARRACKS": 1}
]

levels = [
    [
        [[90, 80, 70, 5], 0.95],
        [[113, 102, 88, 1], 0.91],
        [[143, 130, 111, 1], 0.86],
        [[180, 166, 140, 1], 0.82],
        [[227, 211, 176, 1], 0.78],
        [[286, 270, 222, 2], 0.75],
        [[360, 344, 280, 2], 0.71],
        [[454, 438, 353, 2], 0.68],
        [[572, 559, 445, 3], 0.64],
        [[720, 712, 560, 3], 0.61],
        [[908, 908, 706, 3], 0.58],
        [[1144, 1158, 890, 4], 0.56],
        [[1441, 1476, 1121, 5], 0.53],
        [[1816, 1882, 1412, 5], 0.51],
        [[2288, 2400, 1779, 7], 0.48],
        [[2883, 3060, 2242, 8], 0.46],
        [[3632, 3902, 2825, 9], 0.44],
        [[4577, 4975, 3560, 10], 0.42],
        [[5767, 6343, 4485, 12], 0.40],
        [[7266, 8087, 5651, 15], 0.38],
        [[9155, 10, 311, 7120, 17], 0.36],
        [[11535, 13146, 8972, 19], 0.34],
        [[14534, 16762, 11304, 23], 0.33],
        [[18313, 21371, 14244, 27], 0.31],
        [[23075, 27248, 17947, 31], 0.30],
        [[29074, 34741, 22613, 37], 0.28],
        [[36633, 44295, 28493, 43], 0.27],
        [[46158, 56476, 35901, 51], 0.26],
        [[58159, 72007, 45235, 59], 0.24],
        [[73280, 91809, 56996, 69], 0.23]
    ],
    [
        [[200, 170, 90, 7], 0.63],
        [[252, 218, 113, 1], 0.59],
        [[318, 279, 143, 2], 0.56],
        [[400, 357, 180, 1], 0.53],
        [[504, 456, 227, 2], 0.50],
        [[635, 584, 286, 2], 0.47],
        [[800, 748, 360, 3], 0.44],
        [[1008, 957, 454, 3], 0.42],
        [[1271, 1225, 572, 4], 0.39],
        [[1601, 1568, 720, 4], 0.37],
        [[2017, 2007, 908, 5], 0.35],
        [[2542, 2569, 1144, 5], 0.33],
        [[3202, 3288, 1441, 7], 0.31],
        [[4035, 4209, 1816, 8], 0.29],
        [[5084, 5388, 2288, 9], 0.28],
        [[6406, 6896, 2883, 11], 0.26],
        [[8072, 8827, 3632, 12], 0.25],
        [[10170, 11298, 4577, 15], 0.23],
        [[12814, 14462, 5767, 17], 0.22],
        [[16146, 18511, 7266, 20], 0.21],
        [[20344, 23695, 9155, 24], 0.20],
        [[25634, 30329, 11535, 27], 0.19],
        [[32298, 38821, 14534, 32], 0.17],
        [[40696, 49691, 18313, 38], 0.16],
        [[51277, 63605, 23075, 44], 0.15]
    ],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

data = {
    "requirements": {},
    "levels": []
}

for i, name in enumerate(buildings):
    f = open(f"{name}.json", "w")
    data["requirements"].clear()
    data["requirements"].update(requirements[i])
    data["levels"] = levels[i]
    f.write(json.dumps(data))
    f.close()

