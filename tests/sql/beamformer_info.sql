/*
                            Table "public.beamformer_info"
        Column     |       Type       | Collation | Nullable |      Default
    ---------------+------------------+-----------+----------+--------------------
    beamformer_id | integer          |           | not null |
    sn            | text             |           |          |
    xdelaysn      | integer          |           |          |
    ydelaysn      | integer          |           |          |
    cpld_sn       | text             |           |          |
    ifrev         | integer          |           |          |
    if_sn         | integer          |           |          |
    begintime     | double precision |           | not null |
    endtime       | double precision |           |          |
    gain_y        | double precision |           |          |
    gain_x        | double precision |           |          |
    id            | uuid             |           | not null | uuid_generate_v1()
    Indexes:
        "beamformer_info_pk" PRIMARY KEY, btree (id)
        "beamformer_info_unique" UNIQUE CONSTRAINT, btree (beamformer_id, begintime)
        "beamformer_info_beamformer_id" btree (beamformer_id)
        "beamformer_info_begintime" btree (begintime)
        "beamformer_info_endtime" btree (endtime)
*/

/*
    DESCRIPTION: The default view for the beamformer page
    CREATED BY: Nick Clarke
    CREATED ON: 9/09/2021
    LAST EDITED BY: Nick Clarke
    LAST EDITED ON: 13/10/2021
    SCRIPT STATUS: working
    TEST DETAILS: 
        STATUS: pass
        BRANCH: main
        DATE-TIME: 17/10/2021
*/

SELECT  beamformer_id,
        timestamp_gps(begintime) AS "begintime",
        timestamp_gps(endtime) AS "endtime",
        gain_y,
        gain_x
FROM beamformer_info
    WHERE endtime > gpsnow()
    ORDER BY beamformer_id
;