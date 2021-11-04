/*These are the SQL Scripts that where used to create and edit the Configuration_Info Table.*/

/*This Script was used to Created the Table*/
create table configuration_info (
    config_id serial primary key, 
    configuration_name varchar (255) unique not null, 
    active boolean
    )
;

/*This script was used to add the reference_time column*/
alter table configuration_info 
    add column 
        refrence_time double precision
;
