drop table if exists users;
create table users(
    email varchar(255) primary key,
    passwordhash Binary(64) NOT NULL,
    lastname varchar(255) NULL,
    firstname varchar(255) NULL
);

drop table if exists calendars;
create table calendars(
    email varchar(255) NOT NULL,
    calendarID varchar(100) NOT NULL,
    calendarname varchar(255) NOT Null,
    constraint setcalendar primary key(email, ID)
);

drop table if exists creds;
create table creds(
    credID int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL,
    /* How to store json files
    */
);