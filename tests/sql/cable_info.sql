/*
                        Table "public.cable_info"
    Column   |       Type       | Collation | Nullable |      Default
    ------------+------------------+-----------+----------+--------------------
    name       | text             |           | not null |
    begintime  | double precision |           | not null |
    endtime    | double precision |           | not null |
    type       | text             |           |          |
    eleclength | double precision |           |          |
    physlength | double precision |           |          |
    id         | uuid             |           | not null | uuid_generate_v1()
    flavor     | text             |           |          |
    Indexes:
        "cable_info_pk" PRIMARY KEY, btree (id)
        "cable_info_unique" UNIQUE CONSTRAINT, btree (name, begintime)
        "cable_info_begintime" btree (begintime)
        "cable_info_endtime" btree (endtime)
        "cable_info_name" btree (name)
*/

/*
    DESCRIPTION: default view of cable page
    CREATED BY: Nick Clarke
    CREATED ON: 9/09/2021
    LAST EDITED BY: Nick Clarke
    LAST EDITED ON: 17/10/2021
    SCRIPT STATUS: working
    TEST DETAILS:
        STATUS: pass
        BRANCH: main
        DATE-TIME: 17/10/2021
*/

SELECT  name,
        timestamp_gps(begintime) AS "begintime",
        timestamp_gps(endtime) AS "endtime",
        type,
        eleclength,
        physlength,
        flavor
FROM cable_info
    WHERE endtime > gpsnow()
    ORDER BY name
;

