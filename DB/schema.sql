drop table if exists users;
create table users(
    email varchar(255) primary key NOT NULL,
    passwordhash varchar(50) NOT NULL,
    lastname varchar(255),
    firstname varchar(255)
);

drop table if exists calendars;
create table calendars(
    email varchar(255) NOT NULL,
    calendarID varchar(100) NOT NULL,
    calendarname varchar(255) NOT Null,
    constraint setcalendar primary key(email, calendarID)
); 

drop table if exists creds;
create table creds(
    email varchar(255) NOT NULL,
    token json,
    PRIMARY KEY (email)
);