alter table SMARTEFF_PERSON alter column SHOULD_RECEIVE_NOTIFICATIONS rename to SHOULD_RECEIVE_NOTIFICATIONS__U08744 ^
alter table SMARTEFF_PERSON alter column SHOULD_RECEIVE_NOTIFICATIONS__U08744 set null ;
alter table SMARTEFF_PERSON alter column IS_INSIDE rename to IS_INSIDE__U34357 ^
alter table SMARTEFF_PERSON alter column IS_INSIDE__U34357 set null ;
alter table SMARTEFF_PERSON alter column PERSON_ID rename to PERSON_ID__U74197 ^
alter table SMARTEFF_PERSON alter column PERSON_ID__U74197 set null ;
alter table SMARTEFF_PERSON add column PERSON_ID integer ^
update SMARTEFF_PERSON set PERSON_ID = 0 where PERSON_ID is null ;
alter table SMARTEFF_PERSON alter column PERSON_ID set not null ;
alter table SMARTEFF_PERSON add column IS_INSIDE integer ^
update SMARTEFF_PERSON set IS_INSIDE = 0 where IS_INSIDE is null ;
alter table SMARTEFF_PERSON alter column IS_INSIDE set not null ;
alter table SMARTEFF_PERSON add column SHOULD_RECEIVE_NOTIFICATIONS integer ^
update SMARTEFF_PERSON set SHOULD_RECEIVE_NOTIFICATIONS = 0 where SHOULD_RECEIVE_NOTIFICATIONS is null ;
alter table SMARTEFF_PERSON alter column SHOULD_RECEIVE_NOTIFICATIONS set not null ;
