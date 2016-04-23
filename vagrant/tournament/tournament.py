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

        #initial = self.c.execute("select (count(Winner) + count(Loser)) from round")

        self.c.execute("select  id, name, count(Winner) as Win, "
                               "(count(Loser) + count(Winner)) as Matches  "
                               "from Player full join round on player.id=round.winner "
                               "group by player.id "
                               "order by Win desc")

        result = self.c.fetchall()
        print result
        return result
        #insert correlation between loser, winner, and player id
        #ranks = []
        #for row in self.c.fetchall():
        #    ranks.append(row)

        #        print ranks
        # return ranks


        #   self.c.head_row =  ({'id': str(row[0]), 'Name': str(row[0]), 'Wins': str(row[0]),'Loss': str(row[0])
        #                   'Matches': str(row[0])}
        #          for row in self.c.fetchall()[0])
        # self.c.remainrow = self.c.fetchall






    def reportMatch(self, Winner, Loser):

        """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
        self.c.execute("INSERT INTO round(Winner, Loser) VALUES (%s, %s)", (Winner, Loser,))




    @property
    def swissPairings(self, ):

        # Returns a list of pairs of players for the next round of a match.

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

        numrounds = .5 * self.c.countPlayers()
        numplayers = self.c.countPlayers() - 1
        self.c.pairs = []

        #   self.c.execute('''
        #      SELECT a.id, a.Player, b.id, b.Player
        #     FROM Player AS a JOIN Player AS b
        #  ''')
        for i in range(1, numrounds):
            rank = self.c.playerStandings()
            for j in range(0, numplayers):
                player1 = rank.pop(j)
                if (i > 1):
                    checkpair = self.c.execute("select Winner, Loser from round")
                    for x in range(0, checkpair.rowcount):
                        test = checkpair.pop(x)
                        if test[0] or test[1] == player1[j] or player2[j]:
                            j = j + 1
                        else:
                            x = x + 1

                        player2 = rank.pop(j + 1)

                player2 = rank.pop(j + 1)
                self.c.pairs.append((player1[j], player1[j + 1], player2[j], player2[j + 1]))
                break
            print self.c.pairs
            return self.c.pairs
