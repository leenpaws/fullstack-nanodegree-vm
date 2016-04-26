#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#



import psycopg2


class TournamentDB():
    def __init__(self):
        """Connect to the PostgreSQL database.  Returns a database connection."""
        self.Tdb = psycopg2.connect("dbname=tournament")
        self.c = self.Tdb.cursor()
        self.round = 0


    def result(self):
        '''Obtains result of running method'''
        self.result = self.c.fetchall()
        print self.result
        return self.result

    def closeDB(self):
        self.Tdb.commit()
        self.Tdb.close()

    def deleteMatches(self):
        """Remove all the match records from the database."""

        self.c.execute("delete  from round")



    def deletePlayers(self):
        """Remove all the player records from the database."""

        self.c.execute("delete  from Player")



    def countPlayers(self):
        """Returns the number of players currently registered."""
        self.c.execute("select count(id) from Player")
        result = self.c.fetchone()[0]
        print result
        return result

    def registerPlayer(self, name):

        """Adds a player to the tournament database.
        c.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
         c.execute("update posts set content = 'cheese' where content like '%spam%'")
        The database assigns a unique serial id number for the player.  (This
         should be handled by your SQL database schema, not in your Python code.)

        Args:
      name: the player's full name (need not be unique).
    """
        self.c.execute("INSERT INTO Player (name) VALUES (%s)", (name,))
        self.Tdb.commit()
        self.c.execute("select * from player order by id asc")
        self.Tdb.commit()

        # self.c.execute("Insert Rounds into round Values (1))", ())

        #      self.c.execute("update Player")
        #     self.c.execute("update round")
        # result = self.c.fetchall()

        # return result

    def playerStandings(self):
        """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


        self.c.execute("select Win.pid, Win.pname, Win.Win, "
                       "((Win.Win) + (loss.loss)) as Matches "
                       "from Win join loss on Win.pid=Loss.pid "
                       "group by Win.pid, Win.pname, Win.Win, loss.loss "
                       "order by Win.Win desc")

        result = self.c.fetchall()
        print result
        return result





    def reportMatch(self, Winner, Loser):

        """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
        self.c.execute("INSERT INTO round(Winner, Loser) VALUES (%s, %s)", (Winner, Loser,))

    def validpair(self):

        self.c.execute("select Winner, Loser from round")
        result = self.c.fetchall()
        print result
        return result

    @property
    def swissPairings(self):

        # Returns a list of temp_pairs of players for the next round of a match.

        """Assuming that there are an even number of players registered, each player
        appears exactly once in the pairings.  Each player is paired with another
        player with an equal or nearly-equal win record, that is, a player adjacent
        to him or her in the standings.

        Returns:
          A list of tuples, each of which contains (id1, name1, id2, name2)
            id1: the first player's unique id
            name1: the first player's name
            id2: the second player's unique id
            name2: the second player's name"""
        self.round = self.round + 1


        standings = self.playerStandings()
        testpairs = self.validpair()

        temp_pairs = []
        output_pairs=[]
        #for statement using the player standings tuple and enumerating it
        #rank = the playerid so no need to create an extra field
        #using names because who cares if duplicates if you're just going through listtestpair = self.c.execute("select Winner, Loser from round")



        for rank, player in enumerate(standings):
            # checks to see if there are only 2 players
   #         if rank % 2 == 0:
   #             temp_pairs.append(player[0])
   #             temp_pairs.append(player[1])
   #             output_pairs.append(tuple(temp_pairs))
                # here's where pairs are made
   #        else:


            # create list from matches table


            # test to see if the pair is valid by seeing if the pair exists in the matches database
            temp_pairs.append(player[0])

            for winner, loser in enumerate(testpairs):
                if (rank or next(rank) == winner & rank or next(rank) == loser):
                    player[1] = next(player)
                    return player[1]

                temp_pairs.append(player[1])
            output_pairs.append(tuple(temp_pairs))
            temp_pairs = []
        return output_pairs





#           pairs.append((player1[j], player1[j + 1], player2[j], player2[j + 1]))


#            for row in self.c.fetchall():
#               pairs.append(row)
#            print pairs
#            return pairs
