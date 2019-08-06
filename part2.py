import sqlite3 as sqlite
import sys

gen = sys.argv[1]
k = sys.argv[2]

print 'Top '+k+' Actors played in most '+gen+' movies :'
print 'Actor, '+gen+' Movies Played in'

with sqlite.connect('si601_w16_hw4.db') as con: 
	cur = con.cursor()
	cur.execute("SELECT movie_actor.actor, COUNT(movie_genre.imdb_id) FROM movie_actor JOIN movie_genre ON movie_actor.imdb_id = movie_genre.imdb_id WHERE movie_genre.genre =(?) GROUP BY movie_actor.actor ORDER BY COUNT(movie_genre.imdb_id) DESC LIMIT (?)", (gen,k))
	rows = cur.fetchall()
	for row in rows:
		print row[0]+', '+str(row[1])