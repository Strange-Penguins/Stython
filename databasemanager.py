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

    def create_village(self, world, player, coords):
        if world not in self.worlds:
            return False, "World not available"
        with self.worlds[world] as villages:
            # CHECK FOR EXISTING VILLAGES
            if len(villages.execute("SELECT * FROM villages WHERE xCoord = ? AND yCoord = ?", coords).fetchall()) == 0:
                return False, "A Village for you already exists."
            # Fetch player village count
            count = villages.execute("SELECT COUNT(*) FROM villages WHERE player = ?" (player,)).fetchall()[0]
            values = [player, int(count), coords[0], coords[1], 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1] + 11 * [0]
            villages.execute("INSERT INTO villages (player, village, xCord, yCord, HEADQUARTER, BARRACKS, STABLE,"
                             " WORKSHOP, ACADEMY, SMITHY, RALLY_POINT, STATUE, MARKET, TIMBER_CAMP, CLAY_PIT,"
                             " IRON_MINE, FARM, WAREHOUSE, HIDING_PLACE, WALL, Spear, Sword, Axe, Scout, Light, Heavy,"
                             " Ram, Catapult, Paladin, Nobleman) "
                             "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                             tuple(values)).fetchall()
        return True, "Village successful created"

    # Gets a village or all Villages for a specific player.
    def get_village(self, world, player, village=None):
        if world not in self.worlds or not str(village).isnumeric():
            return False
        with self.worlds[world] as villages:
            query = f"SELECT * FROM villages WHERE player = ?{'' if village is not None else 'AND village = ?'}"
            res = villages.execute(query, (player, int(village))).fetchall()
        # TODO: Convert if nessecary
        return res

    def get_villages(self, world, player):
        return self.get_village(world, player)

    def update_village(self, world, player, village):
        if world not in self.worlds:
            return False
        with self.worlds[world] as villages:
            query = ""
            # TODO UPDATE

    def delete_village(self, world, player, village):
        if world not in self.worlds:
            return False
        with self.worlds[world] as villages:
            if len(villages.execute("SELECT * FROM villages WHERE player = ? AND village = ?", (player, village)).fetchall()) != 1:
                return False, "No village found"
            count = villages.execute("SELECT COUNT(*) FROM villages WHERE player = 'computer'").fetchall()[0]
            # DELETE SHOULD CONVERT A VILLAGE TO A BARBARIAN VILLAGE
            # villages.execute("REPLACE INTO villages(player, village) WITH player VALUES(?,?,?,?)")
            # TODO DELETE

    # TODO: REPETE FOR MOVEMENTS AND BUILDINGQUEUE
