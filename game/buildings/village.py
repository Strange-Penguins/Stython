import time


class Village:

    def __init__(self, game_data, pos=(0, 0)):
        self.position = pos
        self.buildings = [0] * len(game_data.buildings_list)
        self.last_update = time.monotonic_ns() / 1_000_000

    def update(self, game_data):
        current_time = time.monotonic_ns() / 1_000_000
        time_diff = current_time - self.last_update
        self.last_update = current_time

