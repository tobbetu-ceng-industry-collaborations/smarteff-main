-- begin SMARTEFF_SCHEDULED_SHUTDOWN
create table SMARTEFF_SCHEDULED_SHUTDOWN (
    ID varchar(36) not null,
    VERSION integer not null,
    CREATE_TS timestamp,
    CREATED_BY varchar(50),
    UPDATE_TS timestamp,
    UPDATED_BY varchar(50),
    DELETE_TS timestamp,
    DELETED_BY varchar(50),
    --
    SHUTDOWN_ID integer not null,
    PERSON_ID integer not null,
    DEVICE_ID varchar(255) not null,
    DEVICE_NAME varchar(255) not null,
    SHUTDOWN_TIME time not null,
    --
    primary key (ID)
)^
-- end SMARTEFF_SCHEDULED_SHUTDOWN
-- begin SMARTEFF_DEVICE
create table SMARTEFF_DEVICE (
    ID varchar(36) not null,
    VERSION integer not null,
    CREATE_TS timestamp,
    CREATED_BY varchar(50),
    UPDATE_TS timestamp,
    UPDATED_BY varchar(50),
    DELETE_TS timestamp,
    DELETED_BY varchar(50),
    --
    DEVICE_ID integer not null,
    DEVICE_NAME varchar(255) not null,
    IS_ON integer not null,
    --
    primary key (ID)
)^
-- end SMARTEFF_DEVICE
-- begin SMARTEFF_PERSON
create table SMARTEFF_PERSON (
    ID varchar(36) not null,
    VERSION integer not null,
    CREATE_TS timestamp,
    CREATED_BY varchar(50),
    UPDATE_TS timestamp,
    UPDATED_BY varchar(50),
    DELETE_TS timestamp,
    DELETED_BY varchar(50),
    --
    PERSON_ID integer not null,
    PERSON_NAME varchar(255) not null,
    IS_INSIDE integer not null,
    SHOULD_RECEIVE_NOTIFICATIONS integer not null,
    --
    primary key (ID)
)^
-- end SMARTEFF_PERSON
