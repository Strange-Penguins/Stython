import time


def _get_building_level_data(game_data, building_index, level):
    if level > 0:
        return game_data[building_index]["levels"][level - 1]


class Village:

    def __init__(self, game_data, pos=(0, 0)):
        self.position = pos
        self.buildings = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0]
        self.last_update = time.monotonic_ns() / 1_000_000
        self.resources = [400, 400, 400, 0]
        self.last_resource = [0, 0, 0]
        self.population = 0
        self.max_population = 0
        self._calculate_population(game_data)

    def update(self, game_data):
        current_time = time.monotonic_ns() / 1_000_000
        time_diff = current_time - self.last_update
        self.last_update = current_time
        self._update_resources(game_data, time_diff)

    def _update_resources(self, game_data, time_diff):
        # TIMBER_CAMP 9 CLAY_PIT 10 IRON_MINE 11
        self._update_resource(game_data, time_diff, 9, 0)
        self._update_resource(game_data, time_diff, 10, 1)
        self._update_resource(game_data, time_diff, 11, 2)
        return

    def _calculate_population(self, game_data):
        # get max_population from farm level
        self.max_population = _get_building_level_data(game_data, 12, self.buildings[12])[1]
        self.current_population = 0
        for index, building_level in enumerate(self.buildings):
            if building_level == 0:
                continue
            self.current_population += _get_building_level_data(game_data, index, building_level)[0][4]
        # TODO troops and queued buildings
        self.resources[3] = self.max_population - self.current_population

    def _update_resource(self, game_data, time_diff, building_index, resource_index):
        needed_time = self._get_time_for_resource(game_data, building_index)
        time_diff += self.last_resource[resource_index]
        while time_diff > needed_time:
            time_diff -= needed_time
            self.resources[resource_index] += 1

        self.last_resource[resource_index] = time_diff

    def _get_time_for_resource(self, game_data, building_index):
        """returns time in ms for the given building to produce"""
        level = self.buildings[building_index]
        # TODO add speed modifiers
        if level == 0:
            return 450_000
        production = game_data.buildings[building_index]["levels"][level - 1][1]
        return 3_600_000 / production
