import json


class GameData:

    def __init__(self):
        self.buildings = []
        self.max_building_queue_length = 2
        self.buildings_list = ["HEADQUARTER", "BARRACKS", "STABLE", "WORKSHOP", "ACADEMY", "SMITHY", "RALLY_POINT",
                               "STATUE", "MARKET", "TIMBER_CAMP", "CLAY_PIT", "IRON_MINE", "FARM", "WAREHOUSE",
                               "HIDING_PLACE", "WALL"]
        self.buildings_map = {
            "HEADQUARTER": 0,
            "BARRACKS": 1,
            "STABLE": 2,
            "WORKSHOP": 3,
            "ACADEMY": 4,
            "SMITHY": 5,
            "RALLY_POINT": 6,
            "STATUE": 7,
            "MARKET": 8,
            "TIMBER_CAMP": 9,
            "CLAY_PIT": 10,
            "IRON_MINE": 11,
            "FARM": 12,
            "WAREHOUSE": 13,
            "HIDING_PLACE": 14,
            "WALL": 15
        }
        for element in self.buildings_list:
            with open(f"resources/buildings/{element}.json") as f:
                self.buildings.append(json.load(f))
