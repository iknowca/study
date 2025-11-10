create table tbl_member
(
    mid   varchar(50) not null
        primary key,
    mpw   varchar(50) not null,
    mname varchar(50) not null,
    uuid  varchar(50) null
);

create table tbl_todo
(
    tno      int auto_increment
        primary key,
    title    varchar(100)      not null,
    dueDate  date              not null,
    finished tinyint default 0 null
);

