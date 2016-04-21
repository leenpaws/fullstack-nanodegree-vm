#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#





import psycopg2


    def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
        db = psycopg2.connect("dbname=tournament")
        c = db.cursor()

    def closeconn():
        c.commit()
        c.close()


    def deleteMatches():
    """Remove all the match records from the database."""

        c.execute("delete * from round")
        for row in c.fetchall():
        print " ", row[0]

    c.closeconn()

    def deletePlayers():
    """Remove all the player records from the database."""

        c.execute("delete * from Player")
        for row in c.fetchall():
        print " ", row[0]

c.closeconn()

    def countPlayers():
    """Returns the number of players currently registered."""
        c.execute("select count(id) from allresults")
        for row in c.fetchall():
            print " ", row[0]

    def registerPlayer(self):

    """Adds a player to the tournament database.
    c.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
    c.execute("update posts set content = 'cheese' where content like '%spam%'")
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
        c.execute("INSERT Playername, Win, Loss INTO Player VALUES (%s, %s, %s)", (Playername, Win, Loss, ))
        c.execute("update Player)
        for row in c.fetchall():
            print " ", row[0]
        c.closeconn()

    def playerStandings():
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
        c.execute("select id, Playername, (Win + Loss) as Matches, "
                                     "Win, Loss from allresults "
                                     "order by win desc")
        for row in c.fetchall():
        print " ", row[0]
        c.closeconn()


    def reportMatch():


    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
        c.execute("INSERT Name, Winner, Loser, round INTO round VALUES (%s, %s, %s, %s)", (Name, Winner, Loser, round, ))
        c.execute("update round")
        for row in c.fetchall():
        print " ", row[0]
        c.closeconn()

    def swissPairings():
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


