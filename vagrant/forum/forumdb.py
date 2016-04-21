#
# Database access functions for the web forum.
# 


import psycopg2


# Database connection

# Get posts from database.
def GetAllPosts():
    db = psycopg2.connect("dbname=forum")
    c = db.cursor()

    '''Get all the posts from the database, sorted with the newest first.
    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    c.execute("SELECT time, content FROM posts ORDER BY time DESC")
    posts = ({'content': str(row[1]), 'time': str(row[0])}
             for row in c.fetchall())
    db.close()
    return posts


# Add a post to the database.
def AddPost(content):

    db = psycopg2.connect("dbname=forum")

    c = db.cursor()
    '''Add a new post to the database.'''
    '''   Args:
      content: The text content of the new post.
    '''

    c.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
    db.commit()
    db.close()
