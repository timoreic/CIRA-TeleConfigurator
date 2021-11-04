/*
                                Table "public.tile_info"
        Column     |           Type           | Collation | Nullable |      Default
    ----------------+--------------------------+-----------+----------+--------------------
    tile_id        | integer                  |           | not null |
    begintime      | double precision         |           | not null |
    endtime        | double precision         |           |          |
    tile_pos_east  | real                     |           |          |
    tile_pos_north | real                     |           |          |
    tile_altitude  | real                     |           |          |
    beamformer_id  | integer                  |           |          |
    modtime        | timestamp with time zone |           |          | now()
    id             | uuid                     |           | not null | uuid_generate_v1()
    Indexes:
        "tile_info_pk" PRIMARY KEY, btree (id)
        "tile_info_unique" UNIQUE CONSTRAINT, btree (tile_id, begintime)
        "tile_info_begintime" btree (begintime)
        "tile_info_endtime" btree (endtime)
        "tile_info_tile_id" btree (tile_id)
*/

/*
    DESCRIPTION: The default view for the tile page
    CREATED BY: Nick Clarke
    CREATED ON: 8/09/2021
    LAST EDITED BY: Nick Clarke
    LAST EDITED ON: 13/10/2021
    SCRIPT STATUS: Working
    TEST DETAILS:
        STATUS: Pass
        BRANCH: main
        DATE-TIME: 17/10/2021
*/
SELECT  tile_id,
        timestamp_gps(begintime) AS "begintime",
        timestamp_gps(endtime) AS "endtime",
        tile_pos_east,
        tile_pos_north,
        tile_altitude,
        beamformer_id
FROM tile_info
    WHERE endtime > gpsnow()
    ORDER BY tile_id
;

