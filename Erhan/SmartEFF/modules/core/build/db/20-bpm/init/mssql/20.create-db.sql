-- begin BPM_PROC_DEFINITION
alter table BPM_PROC_DEFINITION add constraint FK_BPM_PROC_DEFINITION_MODEL_ID foreign key (MODEL_ID) references BPM_PROC_MODEL(ID)^
create clustered index IDX_BPM_PROC_DEFINITION_CREATE_TS on BPM_PROC_DEFINITION (CREATE_TS)^
create index IDX_BPM_PROC_DEFINITION_MODEL on BPM_PROC_DEFINITION (MODEL_ID)^
-- end BPM_PROC_DEFINITION
-- begin BPM_PROC_ROLE
alter table BPM_PROC_ROLE add constraint FK_BPM_PROC_ROLE_PROC_DEFINITION_ID foreign key (PROC_DEFINITION_ID) references BPM_PROC_DEFINITION(ID)^
create clustered index IDX_BPM_PROC_ROLE_CREATE_TS on BPM_PROC_ROLE (CREATE_TS)^
create index IDX_BPM_PROC_ROLE_PROC_DEFINITION on BPM_PROC_ROLE (PROC_DEFINITION_ID)^
-- end BPM_PROC_ROLE
-- begin BPM_PROC_INSTANCE
alter table BPM_PROC_INSTANCE add constraint FK_BPM_PROC_INSTANCE_PROC_DEFINITION_ID foreign key (PROC_DEFINITION_ID) references BPM_PROC_DEFINITION(ID)^
alter table BPM_PROC_INSTANCE add constraint FK_BPM_PROC_INSTANCE_STARTED_BY_ID foreign key (STARTED_BY_ID) references SEC_USER(ID)^
create clustered index IDX_BPM_PROC_INSTANCE_CREATE_TS on BPM_PROC_INSTANCE (CREATE_TS)^
create index IDX_BPM_PROC_INSTANCE_PROC_DEFINITION on BPM_PROC_INSTANCE (PROC_DEFINITION_ID)^
create index IDX_BPM_PROC_INSTANCE_STARTED_BY on BPM_PROC_INSTANCE (STARTED_BY_ID)^
-- end BPM_PROC_INSTANCE
-- begin BPM_PROC_ACTOR
alter table BPM_PROC_ACTOR add constraint FK_BPM_PROC_ACTOR_USER_ID foreign key (USER_ID) references SEC_USER(ID)^
alter table BPM_PROC_ACTOR add constraint FK_BPM_PROC_ACTOR_PROC_INSTANCE_ID foreign key (PROC_INSTANCE_ID) references BPM_PROC_INSTANCE(ID)^
alter table BPM_PROC_ACTOR add constraint FK_BPM_PROC_ACTOR_PROC_ROLE_ID foreign key (PROC_ROLE_ID) references BPM_PROC_ROLE(ID)^
create clustered index IDX_BPM_PROC_ACTOR_CREATE_TS on BPM_PROC_ACTOR (CREATE_TS)^
create index IDX_BPM_PROC_ACTOR_PROC_ROLE on BPM_PROC_ACTOR (PROC_ROLE_ID)^
create index IDX_BPM_PROC_ACTOR_USER on BPM_PROC_ACTOR (USER_ID)^
create index IDX_BPM_PROC_ACTOR_PROC_INSTANCE on BPM_PROC_ACTOR (PROC_INSTANCE_ID)^
-- end BPM_PROC_ACTOR
-- begin BPM_PROC_TASK
alter table BPM_PROC_TASK add constraint FK_BPM_PROC_TASK_PROC_INSTANCE_ID foreign key (PROC_INSTANCE_ID) references BPM_PROC_INSTANCE(ID)^
alter table BPM_PROC_TASK add constraint FK_BPM_PROC_TASK_PROC_ACTOR_ID foreign key (PROC_ACTOR_ID) references BPM_PROC_ACTOR(ID)^
create clustered index IDX_BPM_PROC_TASK_CREATE_TS on BPM_PROC_TASK (CREATE_TS)^
create index IDX_BPM_PROC_TASK_PROC_ACTOR on BPM_PROC_TASK (PROC_ACTOR_ID)^
create index IDX_BPM_PROC_TASK_PROC_INSTANCE on BPM_PROC_TASK (PROC_INSTANCE_ID)^
-- end BPM_PROC_TASK
-- begin BPM_PROC_ATTACHMENT_TYPE
create clustered index IDX_BPM_PROC_ATTACHMENT_TYPE_CREATE_TS on BPM_PROC_ATTACHMENT_TYPE (CREATE_TS)^
-- end BPM_PROC_ATTACHMENT_TYPE
-- begin BPM_PROC_ATTACHMENT
alter table BPM_PROC_ATTACHMENT add constraint FK_BPM_PROC_ATTACHMENT_FILE_ID foreign key (FILE_ID) references SYS_FILE(ID)^
alter table BPM_PROC_ATTACHMENT add constraint FK_BPM_PROC_ATTACHMENT_TYPE_ID foreign key (TYPE_ID) references BPM_PROC_ATTACHMENT_TYPE(ID)^
alter table BPM_PROC_ATTACHMENT add constraint FK_BPM_PROC_ATTACHMENT_PROC_INSTANCE_ID foreign key (PROC_INSTANCE_ID) references BPM_PROC_INSTANCE(ID)^
alter table BPM_PROC_ATTACHMENT add constraint FK_BPM_PROC_ATTACHMENT_PROC_TASK_ID foreign key (PROC_TASK_ID) references BPM_PROC_TASK(ID)^
alter table BPM_PROC_ATTACHMENT add constraint FK_BPM_PROC_ATTACHMENT_AUTHOR_ID foreign key (AUTHOR_ID) references SEC_USER(ID)^
create clustered index IDX_BPM_PROC_ATTACHMENT_CREATE_TS on BPM_PROC_ATTACHMENT (CREATE_TS)^
create index IDX_BPM_PROC_ATTACHMENT_AUTHOR on BPM_PROC_ATTACHMENT (AUTHOR_ID)^
create index IDX_BPM_PROC_ATTACHMENT_TYPE on BPM_PROC_ATTACHMENT (TYPE_ID)^
create index IDX_BPM_PROC_ATTACHMENT_FILE on BPM_PROC_ATTACHMENT (FILE_ID)^
create index IDX_BPM_PROC_ATTACHMENT_PROC_TASK on BPM_PROC_ATTACHMENT (PROC_TASK_ID)^
create index IDX_BPM_PROC_ATTACHMENT_PROC_INSTANCE on BPM_PROC_ATTACHMENT (PROC_INSTANCE_ID)^
-- end BPM_PROC_ATTACHMENT
-- begin BPM_PROC_MODEL
create unique index IDX_BPM_PROC_MODEL_UNIQ_NAME on BPM_PROC_MODEL (NAME, DELETE_TS) ^
create clustered index IDX_BPM_PROC_MODEL_CREATE_TS on BPM_PROC_MODEL (CREATE_TS)^
-- end BPM_PROC_MODEL
-- begin BPM_PROC_TASK_USER_LINK
alter table BPM_PROC_TASK_USER_LINK add constraint FK_BPTUL_PROC_TASK foreign key (PROC_TASK_ID) references BPM_PROC_TASK (ID)^
alter table BPM_PROC_TASK_USER_LINK add constraint FK_BPTUL_USER foreign key (USER_ID) references SEC_USER (ID)^
-- end BPM_PROC_TASK_USER_LINK
-- begin BPM_STENCIL_SET
create unique index IDX_BPM_STENCIL_SET_UNIQ_NAME on BPM_STENCIL_SET (NAME, DELETE_TS) ^
-- end BPM_STENCIL_SET
