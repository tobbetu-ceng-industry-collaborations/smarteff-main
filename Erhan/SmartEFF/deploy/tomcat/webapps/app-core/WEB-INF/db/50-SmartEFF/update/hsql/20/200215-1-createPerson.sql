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
);