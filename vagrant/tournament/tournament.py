#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#



import psycopg2 #gives out list of tuples

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

<<<<<<< HEAD
        #initial = self.c.execute("select (count(Winner) + count(Loser)) from round")

        self.c.execute("select Win.pid, Win.pname, Win.Win, "
                       "((Win.Win) + (loss.loss)) as Matches "
                       "from Win join loss on Win.pid=Loss.pid "
                       "group by Win.pid, Win.pname, Win.Win, loss.loss "
                       "order by Win.Win desc")

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
=======
        ranks = []
        for row in self.c.fetchall():
                ranks.append(row)
                return ranks
>>>>>>> parent of a590144... update

        print self.c.result

        self.c.close()




    def reportMatch(self, Winner, Loser):


        """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
<<<<<<< HEAD
        self.c.execute("INSERT INTO round(Winner, Loser) VALUES (%s, %s)", (Winner, Loser,))
        self.Tdb.commit()

<<<<<<< HEAD
    def validpair(self):
        self.c.execute("select winner, loser from round")

        result = self.c.fetchall()
        print result
        return result
=======
=======
        self.c.execute("INSERT Winner, Loser INTO round VALUES (%s, %s, %s, %s)", (Winner, Loser,))
        self.c.execute("update round")
>>>>>>> parent of a590144... update

        self.c.result()
        self.c.closeDB()

>>>>>>> parent of 4d9afac... test

    @property
<<<<<<< HEAD
    def swissPairings(self):
=======
    def swissPairings(self,):
>>>>>>> parent of a590144... update

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
<<<<<<< HEAD
            name2: the second player's name"""
<<<<<<< HEAD
        self.round = self.round + 1
        testpair = self.validpair()
        possiblepair = []

        standings = self.playerStandings()

        self.output_pairs = []
        #look up race condition
        temp_pairs = []
        for j in range(0, len(testpair)):
            p1test=testpair[j]
            p1place=testpair[0]
            p2place=testpair[1]

            if p1place > p2place :
                possiblepair.append((p2place, p1place))
            else:
                possiblepair.append((p1place, p2place))


        while len(standings) > 0:
            player1 = standings.pop(0)
            player1_id = player1[0]
            player1_name = player1[1]
            for player in standings :

                if



            for i in range(1, len(standings)):



            player2_id = player2[0]
            player2_name = player2[1]
            #tuple=immutable object that can't be changed, pop takes something out
            pairing_tuple = (player1_id, player1_name, player2_id, player2_name)

            self.output_pairs.append(pairing_tuple)
        return self.output_pairs



=======

        playercount = self.countPlayers()

        numrounds = playercount/2
        numplayers = playercount-1
>>>>>>> parent of 4d9afac... test

=======
            name2: the second player's name
        """

        numrounds = .5*self.c.countPlayers()
        numplayers = self.c.countPlayers()-1
        self.c.pairs = []
>>>>>>> parent of a590144... update


     #   self.c.execute('''
      #      SELECT a.id, a.Player, b.id, b.Player
       #     FROM Player AS a JOIN Player AS b
        #  ''')
<<<<<<< HEAD
        pairs = []
        for i in range(1, numrounds):
            rank = self.playerStandings()

            for j in range(0, numplayers):
                player1 = rank.pop(j)
#                if (i > 1):
#
#                    checkpair = self.c.execute("select Winner, Loser from round")
#                    for x in range(0, checkpair.rowcount):
#                        test = checkpair.pop[x]
#                        if test[0] or test[1] == player1[j] or player2[j]:
#                            j = j + 1
#                       else:
#                            x = x + 1

                player2 = rank.pop(j + 1)
                pairs.append((player1[j], player1[j + 1], player2[j], player2[j + 1]))



<<<<<<< HEAD


        #for statement using the player standings tuple and enumerating it
        #rank = the playerid so no need to create an extra field
        #using names because who cares if duplicates if you're just going through listtestpair = self.c.execute("select Winner, Loser from round")


        #
        # for row in standings:
        #
        #     # checks to see if there are only 2 players
        #     #if len(standings) % 2 == 0:
        #      #   self.output_pairs.append((standings[0], standings[1]))
        #       #  break
        #         #    temp_pairs.append(player[0])
        #         #    temp_pairs.append(player[1])
        #         #    output_pairs.append(tuple(temp_pairs))
        #         # here's where pairs are made
        #         # else:
        #
        #         # create list from matches table
        #
        #
        #         # test to see if the pair is valid by seeing if the pair exists in the matches database
        #
        #
        #
        #
        #         #   if(testpairs.count(tuple(temp_pairs)) == 0):
        #     #else:
        #        temp_pairs.append(standings[0])
        #        temp_pairs.append(standings[1])
        #        self.output_pairs.append({standings[0], standings[1]})
        #        temp_pairs = []
        #
        # print self.output_pairs
        # return self.output_pairs
        #



=======
#            for row in self.c.fetchall():
#               pairs.append(row)
            print pairs
            return pairs
>>>>>>> parent of 4d9afac... test
=======



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
>>>>>>> parent of a590144... update
