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
);