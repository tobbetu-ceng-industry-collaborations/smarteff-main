alter table SMARTEFF_SCHEDULED_SHUTDOWN alter column SHUTDOWN_TIME rename to SHUTDOWN_TIME__U81106 ^
alter table SMARTEFF_SCHEDULED_SHUTDOWN alter column SHUTDOWN_TIME__U81106 set null ;
alter table SMARTEFF_SCHEDULED_SHUTDOWN alter column PERSON_ID rename to PERSON_ID__U93031 ^
alter table SMARTEFF_SCHEDULED_SHUTDOWN alter column PERSON_ID__U93031 set null ;
alter table SMARTEFF_SCHEDULED_SHUTDOWN alter column SHUTDOWN_ID rename to SHUTDOWN_ID__U20725 ^
alter table SMARTEFF_SCHEDULED_SHUTDOWN alter column SHUTDOWN_ID__U20725 set null ;
-- alter table SMARTEFF_SCHEDULED_SHUTDOWN add column SHUTDOWN_ID integer ^
-- update SMARTEFF_SCHEDULED_SHUTDOWN set SHUTDOWN_ID = <default_value> ;
-- alter table SMARTEFF_SCHEDULED_SHUTDOWN alter column SHUTDOWN_ID set not null ;
alter table SMARTEFF_SCHEDULED_SHUTDOWN add column SHUTDOWN_ID integer ;
-- alter table SMARTEFF_SCHEDULED_SHUTDOWN add column PERSON_ID integer ^
-- update SMARTEFF_SCHEDULED_SHUTDOWN set PERSON_ID = <default_value> ;
-- alter table SMARTEFF_SCHEDULED_SHUTDOWN alter column PERSON_ID set not null ;
alter table SMARTEFF_SCHEDULED_SHUTDOWN add column PERSON_ID integer ;
alter table SMARTEFF_SCHEDULED_SHUTDOWN add column SHUTDOWN_TIME time ^
update SMARTEFF_SCHEDULED_SHUTDOWN set SHUTDOWN_TIME = current_time where SHUTDOWN_TIME is null ;
alter table SMARTEFF_SCHEDULED_SHUTDOWN alter column SHUTDOWN_TIME set not null ;
