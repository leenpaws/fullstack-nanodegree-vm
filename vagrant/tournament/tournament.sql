-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.


DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;
\c tournament
    CREATE table Player ( name TEXT NOT NULL,
                          id SERIAL primary key
                        );


    CREATE table round  (   rid SERIAL primary key,
                            Winner integer references Player(id) ON DELETE CASCADE,
                            Loser integer REFERENCES Player(id) ON DELETE CASCADE,
                            Rounds integer
                         );

    CREATE VIEW Win AS
    SELECT player.id AS pid,  player.name AS pname, COUNT(round.winner) AS Win
    FROM Player LEFT JOIN round
    ON Player.id = round.winner
    GROUP BY Player.id, round.winner;


    CREATE VIEW loss AS
    SELECT Player.id AS pid, COUNT(round.loser) AS loss
    FROM Player LEFT JOIN round
    ON Player.id = round.loser
    GROUP BY player.id, round.loser;


--

