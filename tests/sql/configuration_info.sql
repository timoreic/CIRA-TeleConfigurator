/*
                                             Table "public.configuration_info"
       Column       |          Type          | Collation | Nullable |                        Default
--------------------+------------------------+-----------+----------+-------------------------------------------------------
 config_id          | integer                |           | not null | nextval('configuration_info_config_id_seq'::regclass)
 configuration_name | character varying(255) |           | not null |
 active             | boolean                |           |          |
 refrence_time      | double precision       |           |          |
Indexes:
    "configuration_info_pkey" PRIMARY KEY, btree (config_id)
    "configuration_info_configuration_name_key" UNIQUE CONSTRAINT, btree (configuration_name)
*/

/*
    DESCRIPTION: Shows all the configurations saved in the database 
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

SELECT  config_id,
        configuration_name,
        active,
        refrence_time
FROM configuration_info
    ORDER BY config_id
;