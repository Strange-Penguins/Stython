-- noinspection SqlNoDataSourceInspectionForFile

CREATE TABLE villages
(
    player       INTEGER NOT NULL,
    village      INTEGER NOT NULL,
    xCord        INTEGER NOT NULL,
    yCord        INTEGER NOT NULL,
    HEADQUARTER  INTEGER NOT NULL,
    BARRACKS     INTEGER NOT NULL,
    STABLE       INTEGER NOT NULL,
    WORKSHOP     INTEGER NOT NULL,
    ACADEMY      INTEGER NOT NULL,
    SMITHY       INTEGER NOT NULL,
    RALLY_POINT  INTEGER NOT NULL,
    STATUE       INTEGER NOT NULL,
    MARKET       INTEGER NOT NULL,
    TIMBER_CAMP  INTEGER NOT NULL,
    CLAY_PIT     INTEGER NOT NULL,
    IRON_MINE    INTEGER NOT NULL,
    FARM         INTEGER NOT NULL,
    WAREHOUSE    INTEGER NOT NULL,
    HIDING_PLACE INTEGER NOT NULL,
    WALL         INTEGER NOT NULL,
    Spear        INTEGER NOT NULL,
    Sword        INTEGER NOT NULL,
    Axe          INTEGER NOT NULL,
    Scout        INTEGER NOT NULL,
    Light        INTEGER NOT NULL,
    Heavy        INTEGER NOT NULL,
    Ram          INTEGER NOT NULL,
    Catapult     INTEGER NOT NULL,
    Paladin      INTEGER NOT NULL,
    Nobleman     INTEGER NOT NULL
);
CREATE TABLE movements
(
    Player       INTEGER NOT NULL,
    StartVillage INTEGER NOT NULL,
    EnemyVillage INTEGER NOT NULL,
    StartTime    INTEGER NOT NULL,
    Duration     INTEGER NOT NULL,
    Spear        INTEGER NOT NULL,
    Sword        INTEGER NOT NULL,
    Axe          INTEGER NOT NULL,
    Scout        INTEGER NOT NULL,
    Light        INTEGER NOT NULL,
    Heavy        INTEGER NOT NULL,
    Ram          INTEGER NOT NULL,
    Catapult     INTEGER NOT NULL,
    Paladin      INTEGER NOT NULL,
    Nobleman     INTEGER NOT NULL
);
CREATE TABLE buildingqueue
(
    player        INTEGER  NOT NULL,
    village       INTEGER  NOT NULL,
    starttime     DATETIME NOT NULL,
    duration      INTEGER  NOT NULL,
    building      INTEGER  NOT NULL
);
