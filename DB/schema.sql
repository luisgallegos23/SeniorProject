drop table if exists users;
create table users(
    email varchar(255) primary key NOT NULL,
    password varchar(50) NOT NULL,
    lname varchar(255),
    fname varchar(255)
);

drop table if exists calendars;
create table calendars(
    email varchar(255) NOT NULL,
    calID varchar(100) NOT NULL,
    calname varchar(255) NOT Null,
    constraint setcalendar primary key(email, calID)
); 

drop table if exists creds;
create table creds(
    email varchar(255) NOT NULL,
    token jsonb,
    PRIMARY KEY (email)
);