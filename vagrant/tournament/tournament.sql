-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.


create database tournament

CREATE table Player ( Playername TEXT
                      time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                      id SERIAL as primary key
                    );


CREATE table round  (
                Winner as foreign key references id (Playername)
                Loser as foreign key references id (Playername)
                Rounds integer,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id SERIAL as primary key
              );



--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


