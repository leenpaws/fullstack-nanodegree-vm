#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#



import psycopg2

class TournamentDB():

    def __init__(self):
        """Connect to the PostgreSQL database.  Returns a database connection."""
        Tdb = psycopg2.connect("dbname=tournament")
        self.c = Tdb.cursor()

    def result(self):
        '''Obtains result of running method'''
        self.c.result = self.c.fetchall()
        print self.c.result
        return self.c.result

    def closeDB(self):
        self.c.commit()
        self.c.close()


    def deleteMatches(self):
       """Remove all the match records from the database."""

       self.c.execute("delete  from round")
       self.c.result()
       self.c.closeDB()

    def deletePlayers(self):
       """Remove all the player records from the database."""

       self.c.execute("delete  from Player")
       self.c.result()
       self.c.closeDB()



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
      self.c.execute("INSERT INTO Player (name) VALUES (%s)", (name, ))

# self.c.execute("Insert Rounds into round Values (1))", ())

      self.c.execute("update Player")
      self.c.execute("update round")
      self.c.result()
      self.c.closeDB()


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
        self.c.execute("select id, Playername, Win as (select count(Winner) from round), "
                       "(Win + (select count(Loser) from round) as Matches, "
                       "from Player"
                       "order by Win desc")
     #   self.c.head_row =  ({'id': str(row[0]), 'Name': str(row[0]), 'Wins': str(row[0]),'Loss': str(row[0])
      #                   'Matches': str(row[0])}
       #          for row in self.c.fetchall()[0])
       # self.c.remainrow = self.c.fetchall

        ranks = []
        for row in self.c.fetchall():
                ranks.append(row)
                return ranks

        print self.c.result

        self.c.close()




    def reportMatch(self, Winner, Loser):


        """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
        self.c.execute("INSERT Winner, Loser INTO round VALUES (%s, %s, %s, %s)", (Winner, Loser,))
        self.c.execute("update round")

        self.c.result()
        self.c.closeDB()

    @property
    def swissPairings(self,):

        """Returns a list of pairs of players for the next round of a match.

        Assuming that there are an even number of players registered, each player
        appears exactly once in the pairings.  Each player is paired with another
        player with an equal or nearly-equal win record, that is, a player adjacent
        to him or her in the standings.

        Returns:
          A list of tuples, each of which contains (id1, name1, id2, name2)
            id1: the first player's unique id
            name1: the first player's name
            id2: the second player's unique id
            name2: the second player's name
        """

        numrounds = .5*self.c.countPlayers()
        numplayers = self.c.countPlayers()-1
        self.c.pairs = []


     #   self.c.execute('''
      #      SELECT a.id, a.Player, b.id, b.Player
       #     FROM Player AS a JOIN Player AS b
        #  ''')



        for i in range (1,numrounds):
            rank = self.c.playerStandings()
            for j in range(0, numplayers):
                player1=rank.pop(j)
                if(i>1):
                        checkpair = self.c.execute("select Winner, Loser from round")
                        for x in range(0, checkpair.rowcount):
                            test=checkpair.pop(x)
                            if test[0] or test [1] == player1[j] or player2[j]:
                                j=j+1
                            else:
                                x=x+1

                            player2=rank.pop(j+1)

                player2 = rank.pop(j + 1)
                self.c.pairs.append((player1[j], player1[j+1], player2[j], player2[j+1]))
                break
            print self.c.pairs
            return self.c.pairs
