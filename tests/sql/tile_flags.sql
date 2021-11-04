/*
                            Table "public.tile_flags"
    Column   |         Type          | Collation | Nullable |      Default
    -----------+-----------------------+-----------+----------+--------------------
    starttime | bigint                |           | not null |
    stoptime  | bigint                |           |          |
    tile_id   | integer               |           | not null |
    creator   | text                  |           | not null |
    comment   | text                  |           |          |
    id        | character varying(36) |           | not null | uuid_generate_v1()
    Indexes:
        "tile_flags_pk" PRIMARY KEY, btree (id)
        "tile_flags_starttime" btree (starttime)
        "tile_flags_stoptime" btree (stoptime)
        "tile_flags_tile_id" btree (tile_id)
*/

/*
    DESCRIPTION: show all flags that have not been resolved
    CREATED BY: Nick Clarke
    CREATED ON: 8/09/2021
    LAST EDITED BY: Nick Clarke
    LAST EDITED ON: 17/10/2021
    SCRIPT STATUS: working
    TEST DETAILS:
        STATUS: pass
        BRANCH: main
        DATE-TIME: 17/10/2021
*/
SELECT  timestamp_gps(starttime)    AS "Start Time",
        timestamp_gps(stoptime)     AS "Resolved Time",
        tile_id                     AS "Tile ID",
        creator                     AS "Flagged by:",
        comment                     AS "Comments"
FROM tile_flags
    WHERE stoptime IS NULL
    ORDER BY tile_id
;
