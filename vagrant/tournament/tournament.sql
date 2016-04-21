-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.


create database tournament

CREATE table Player ( Playername TEXT,
                Rank integer
                Win integer
                Loss integer
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id SERIAL as primary key
              );


CREATE table round  ( Name as foreign key references Playername (Playername),
                Opponent as foreign key references Playername (Playername),
                Playerid as foreign key references id (Playername)
                Opponentid as foreign key references id (Playername)
                round integer,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id SERIAL as primary key
              );

create view allresults as select *
                            from Player join round on id.Player=Playerid.round;



--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


