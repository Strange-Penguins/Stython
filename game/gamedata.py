import json


class GameData:

    def __init__(self):
        self.buildings = []
        self.buildings_list = ["HEADQUARTER", "BARRACKS", "STABLE", "WORKSHOP", "ACADEMY", "SMITHY", "RALLY_POINT",
                               "STATUE", "MARKET", "TIMBER_CAMP", "CLAY_PIT", "IRON_MINE", "FARM", "WAREHOUSE",
                               "HIDING_PLACE", "WALL"]
        for element in self.buildings_list:
            with open(f"resources/buildings/{element}.json") as f:
                self.buildings.append(json.load(f))
