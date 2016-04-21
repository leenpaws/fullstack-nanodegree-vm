-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.


create database tournament

CREATE table Player ( Playername TEXT not null,
                Rank integer
                Win integer
                Loss integer
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id SERIAL as primary key not null
              );


CREATE table round  ( Name as foreign key references Playername (Playername),
                Opponent as foreign key references Playername (Playername),
                Winner as foreign key references id (Playername)
                Loser as foreign key references id (Playername)
                round integer,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id SERIAL as primary key not null
              );

create view allresults as (select *
                            from Player join round on id.Player=Winner.round);



--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


