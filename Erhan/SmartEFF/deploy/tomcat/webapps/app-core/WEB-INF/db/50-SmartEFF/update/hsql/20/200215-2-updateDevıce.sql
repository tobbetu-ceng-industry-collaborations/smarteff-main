alter table SMARTEFF_DEVICE alter column IS_ON rename to IS_ON__U64984 ^
alter table SMARTEFF_DEVICE alter column IS_ON__U64984 set null ;
alter table SMARTEFF_DEVICE alter column DEVICE_ID rename to DEVICE_ID__U74388 ^
alter table SMARTEFF_DEVICE alter column DEVICE_ID__U74388 set null ;
-- alter table SMARTEFF_DEVICE add column DEVICE_ID integer ^
-- update SMARTEFF_DEVICE set DEVICE_ID = <default_value> ;
-- alter table SMARTEFF_DEVICE alter column DEVICE_ID set not null ;
alter table SMARTEFF_DEVICE add column DEVICE_ID integer ;
alter table SMARTEFF_DEVICE add column IS_ON integer ^
update SMARTEFF_DEVICE set IS_ON = 0 where IS_ON is null ;
alter table SMARTEFF_DEVICE alter column IS_ON set not null ;
