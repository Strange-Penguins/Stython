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

data = {
    "requirements": {},
    "levels": []
}

for i, name in enumerate(buildings):
    f = open(f"{name}.json", "w")
    data["requirements"].clear()
    data["requirements"].update(requirements[i])
    f.write(json.dumps(data))
    f.close()
