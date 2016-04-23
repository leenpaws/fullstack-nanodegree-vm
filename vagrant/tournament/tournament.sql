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


    CREATE table round  (   id SERIAL primary key,
                            Winner integer NOT NULL references Player(id) ON DELETE CASCADE,
                            Loser integer NOT NULL REFERENCES Player(id) ON DELETE CASCADE,
                            Rounds integer
                         );



--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


