-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.


CREATE Player ( Playername TEXT,
                Rank integer
                Matchesplayed integer
                Win integer
                Loss integer
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id SERIAL as primary key
              );


CREATE round  ( Name as foreign key references Playername (Playername),
                Opponent as foreign key references Playername (Playername),
                Playerid as foreign key references id (Playername)
                Opponentid as foreign key references id (Playername)
                round integer,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id SERIAL as primary key
              );



--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


