import sqlite3 as sq3
import os.path


class DatabaseManager:

    def __init__(self):
        # This is the db path
        self.dbpath = "db"
        self.worlds = {}

    def connect_world(self, world):
        if world in self.worlds:
            return True
        if not os.path.isfile(f"db/world{world}.db"):
            return False
        connection = sq3.connect(f"db/world{world}.db", check_same_thread=False)
        connection.row_factory = sq3.Row
        self.worlds[world] = connection
        return True

    def create_world(self, world):
        if world in self.worlds:
            return False
        if os.path.isfile(f"db/world{world}.db"):
            return False
        connection = sq3.connect(f"db/world{world}.db", check_same_thread=False)
        connection.row_factory = sq3.Row
        with open("db/schemas/create_world.sql") as f:
            connection.executescript(f.read())
        return True

    def close_all(self):
        while len(self.worlds) > 0:
            self.close(list(self.worlds.keys())[0])

    def close(self, world):
        if world in self.worlds:
            self.worlds[world].commit()
        self.worlds[world].close()
        self.worlds.pop(world, None)

    def create_village(self, world, player, village):
        if world not in self.worlds:
            return False
        # TODO Insert

    def get_village(self, world, player, village):
        if world not in self.worlds:
            return False
        with self.worlds[world] as village:
            res = village.execute("SELECT * FROM villages WHERE player = ? AND village = ?",
                                  (player, village)).fetchall()
        # TODO: Convert if nessecary
        return res

    def get_villages(self, world, player, village):
        if world not in self.worlds:
            return False
        with self.worlds[world] as village:
            res = village.execute("SELECT * FROM villages WHERE player = ?", (player,)).fetchall()
        # TODO: Convert if nessecary
        return res

    def update_village(self, world):
        if world not in self.worlds:
            return False
        # TODO UPDATE

    def delete_village(self, world):
        if world not in self.worlds:
            return False
        pass
        # TODO DELETE

    # TODO: REPETE FOR MOVEMENTS AND BUILDINGQUEUE
