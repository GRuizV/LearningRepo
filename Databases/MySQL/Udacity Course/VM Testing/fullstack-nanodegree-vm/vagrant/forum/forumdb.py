# "Database code" for the DB Forum.

import psycopg2, bleach

DBNAME = 'forum'

# POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts() -> list:

  """Return all posts from the 'database', most recent first."""

  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  query = "SELECT content, time FROM posts ORDER BY time DESC;"
  c.execute(query)
  posts = c.fetchall()
  db.close()

  return posts



def add_post(content) -> None:

  """Add a post to the 'database' with the current timestamp."""

  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  query = "INSERT INTO posts VALUES (%s);"
  c.execute(query, (bleach.clean(content),))
  db.commit()
  db.close()


'''
** SQL Injetction Attack:
    with " '); delete from posts; -- "
'''

'''
**Script Injection Attack:

  With:

  <script>
  setTimeout(function() {
      var tt = document.getElementById('content');
      tt.value = "<h2 style='color: #FF6699; font-family: Comic Sans MS'>Spam, spam, spam, spam,<br>Wonderful spam, glorious spam!</h2>";
      tt.form.submit();
  }, 2500);
  </script>
'''


'''
SQL Sentence to clean up the word 'spam':

  - UPDATE posts SET content = 'Cheese' WHERE content LIKE '%spam%';

SQL Sentence to delete all the cheese from the table

  - DELETE FROM posts WHERE content LIKE '%Cheese%';
'''



'Bobby Tables Joke: http://bobby-tables.com/'




















