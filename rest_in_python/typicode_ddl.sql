create table posts
(
    userid integer,
    id     integer,
    title  varchar(500),
    body   varchar(500)
);

alter table posts
    owner to admin;

create table comments
(
    postid integer,
    id     integer,
    name   varchar(500),
    email  varchar(500),
    body   varchar(500)
);

alter table comments
    owner to admin;

create table albums
(
    userid integer,
    id     integer,
    title  varchar(500)
);

alter table albums
    owner to admin;

create table photos
(
    albumid      integer,
    id           integer,
    title        varchar(500),
    url          varchar(500),
    thumbnailurl varchar(500)
);

alter table photos
    owner to admin;

create table todos
(
    userid    integer,
    id        integer,
    title     varchar(500),
    completed varchar(500)
);

alter table todos
    owner to admin;

create table users
(
    id                 integer,
    name               varchar(500),
    username           varchar(500),
    email              varchar(500),
    addressstreet      varchar(500),
    addresssuite       varchar(500),
    addresscity        varchar(500),
    addresszipcode     varchar(500),
    addressgeolat      numeric(10, 4),
    addressgeolng      numeric(10, 4),
    phone              varchar(500),
    website            varchar(500),
    companyname        varchar(500),
    companycatchphrase varchar(500),
    companybs          varchar(500)
);

alter table users
    owner to admin;


