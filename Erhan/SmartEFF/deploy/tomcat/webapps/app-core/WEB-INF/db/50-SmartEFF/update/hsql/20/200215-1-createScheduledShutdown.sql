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
    SHUTDOWN_TIME varchar(255) not null,
    --
    primary key (ID)
);