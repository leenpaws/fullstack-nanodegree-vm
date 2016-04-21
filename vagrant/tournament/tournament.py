#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#





import psycopg2


# def __init__(self, movie_title, movie_storyline,
#              poster_image, trailer_youtube):

# type: (title, storyline, posterimage, trailery) -> Movie
# self.title = movie_title
# self.storyline = movie_storyline
# self.poster_image_url = poster_image
# self.trailer_youtube_url = trailer_youtube

class db():

    def __init__(self, c):
    """Connect to the PostgreSQL database.  Returns a database connection."""
     self = psycopg2.connect("dbname=tournament")
     c = self.cursor()

    def closeconn(self):
     self.c.commit()
     self.c.close()

class sql_query(db):

    def deleteMatches(self):
    """Remove all the match records from the database."""

    self = db.c.execute("delete * from round")
    self.closeconn()

    def deletePlayers(self, name):
    """Remove all the player records from the database."""

    self = db.c.execute("delete * from Player")


    self.closeconn()


    def countPlayers(self):
    """Returns the number of players currently registered."""
    self = db.c.execute("select count(id) from Player")

    def registerPlayer(self, name):
    """Adds a player to the tournament database.
    c.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
    c.execute("update posts set content = 'cheese' where content like '%spam%'")
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    self = db.c.execute("INSERT INTO Player (Player) VALUES (%s)", (Playername,))
    self = db.c.execute("update posts set content = 'cheese' where content like '%spam%'")

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


    def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
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


