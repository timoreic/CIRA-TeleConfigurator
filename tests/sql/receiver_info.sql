/*
                                Table "public.receiver_info"
        Column     |           Type           | Collation | Nullable |      Default
    ---------------+--------------------------+-----------+----------+--------------------
    receiver_id   | integer                  |           | not null |
    begintime     | double precision         |           | not null |
    endtime       | double precision         |           |          |
    active        | boolean                  |           |          |
    creator       | text                     |           |          | 'mwa'::text
    modtime       | timestamp with time zone |           |          | now()
    vsib_computer | text                     |           |          |
    adfb1         | integer                  |           |          |
    adfb2         | integer                  |           |          |
    agfo          | integer                  |           |          |
    macaddr       | text                     |           |          |
    sbc_name      | text                     |           |          |
    id            | uuid                     |           | not null | uuid_generate_v1()
    fibre_length  | double precision         |           |          |
    Indexes:
        "receiver_info_pk" PRIMARY KEY, btree (id)
        "receiver_info_unique" UNIQUE CONSTRAINT, btree (receiver_id, begintime)

                            Table "public.tile_connection"
        Column     |       Type       | Collation | Nullable |      Default
    ---------------+------------------+-----------+----------+--------------------
    tile          | integer          |           | not null |
    begintime     | double precision |           | not null |
    endtime       | double precision |           |          |
    receiver_id   | smallint         |           |          |
    receiver_slot | smallint         |           |          |
    wire_length   | double precision |           |          |
    beamformer_id | bigint           |           |          |
    cable_name    | text             |           |          |
    id            | uuid             |           | not null | uuid_generate_v1()
    Indexes:
        "tile_connection_pk" PRIMARY KEY, btree (id)
        "tile_connection_unique" UNIQUE CONSTRAINT, btree (tile, begintime)
        "tile_connection_begintime" btree (begintime)
        "tile_connection_endtime" btree (endtime)
        "tile_connection_tile" btree (tile)
*/

/*
    DESCRIPTION: show the currently active receievers and subsequent connections
    CREATED BY: Nick Clarke
    CREATED ON: 9/09/2021
    LAST EDITED BY: Nick Clarke
    LAST EDITED ON: 17/10/2021
    SCRIPT STATUS: working - but doesn't show receiever if there are no connections
    TEST DETAILS:
        STATUS: pass
        BRANCH: main
        DATE-TIME: 17/20/2021
*/

SELECT  receiver_info.receiver_id AS "receiver_id",
        receiver_info.sbc_name AS "sbc_name",
        receiver_info.fibre_length AS "fibre_length",
        receiver_info.active AS "active",
        tile_connection.receiver_slot AS "slot",
        tile_connection.cable_name AS "cable",
        tile_connection.beamformer_id AS "beamformer",
        tile_connection.tile AS "tile",
        tile_connection.begintime AS "begintime"
FROM receiver_info, tile_connection
    WHERE receiver_info.endtime > gpsnow()
        AND tile_connection.endtime > gpsnow()
        AND receiver_info.receiver_id = tile_connection.receiver_id
    ORDER BY receiver_info.receiver_id, tile_connection.receiver_slot
;
    