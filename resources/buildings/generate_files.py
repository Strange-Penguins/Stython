import json

buildings = ["HEADQUARTER", "BARRACKS", "STABLE", "WORKSHOP", "ACADEMY", "SMITHY", "RALLY_POINT", "STATUE", "MARKET", "TIMBER_CAMP", "CLAY_PIT", "IRON_MINE", "FARM", "WAREHOUSE", "HIDING_PLACE", "WALL"]

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
    data["levels"].clear()
    data["levels"].append(levels[i])
    f.write(json.dumps(data))
    f.close()
