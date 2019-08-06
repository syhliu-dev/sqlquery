import json
import sqlite3 as sqlite


# reads the JSON file
data = []
input_file  = open('movie_actors_data.txt', 'rU')
for line in input_file:
	j = json.loads(line)
	data.append(j)

#print data

#create three tables
with sqlite.connect('si601_w16_hw4.db') as con: 
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS movie_genre")
	cur.execute("DROP TABLE IF EXISTS movie")
	cur.execute("DROP TABLE IF EXISTS movie_actor")
	cur.execute("CREATE TABLE movie_genre(imdb_id text, genre text)")
	cur.execute("CREATE TABLE movie(imdb_id text, title text, year integer, rating float)")
	cur.execute("CREATE TABLE movie_actor(imdb_id text, actor text)")

	for row in data:
		imdb_id = row['imdb_id']
		genre = row['genres']
		title = row['title']
		year = row['year']
		rating = row['rating']
		actors = row['actors']

		lot = []
		for movie_genre in genre:
			lot.append((imdb_id, movie_genre))
			#print lot
		cur.executemany("INSERT INTO movie_genre VALUES (?,?)", lot)
		cur.executemany("INSERT INTO movie VALUES (?,?,?,?)", [(imdb_id, title, year, rating)])
		lot = []
		for actor in actors:
			lot.append((imdb_id, actor))
			#print lot
		cur.executemany("INSERT INTO movie_actor VALUES(?,?)", lot)
		con.commit()

	#Write an SQL query to find top 10 genres with most movies and print out the results
	print 'Top 10 genre:'
	print 'Genre, Movies'
	cur.execute("SELECT genre, COUNT(genre) FROM movie_genre GROUP BY genre ORDER BY COUNT(genre) DESC LIMIT 10")
	rows = cur.fetchall()
	for row in rows:
		print row[0]+', '+ str(row[1])

	#Write an SQL query to find number of movies broken down by year in chronological order
	print 'Number of movies broken down by year'
	print 'Year, Movies'
	cur.execute("SELECT year, COUNT(imdb_id) FROM movie GROUP BY year ORDER BY year")
	rows = cur.fetchall()
	for row in rows:
		print str(row[0])+', '+ str(row[1])

	#Write an SQL query to find all Sci-Fi movies order by decreasing rating, then by decreasing year if ratings are the same
	print 'Sci-Fi movies:'
	print 'Title, Year, Rating'
	cur.execute('SELECT movie.title, movie.year, movie.rating FROM movie JOIN movie_genre ON movie.imdb_id = movie_genre.imdb_id WHERE movie_genre.genre = "Sci-Fi" ORDER BY rating DESC, year DESC')
	rows = cur.fetchall()
	for row in rows:
		print row[0]+', '+str(row[1])+', '+str(row[2])

	#In and after year 2000, top 10 actors who played in most movies:
	print 'In and after year 2000, top 10 actors who played in most movies:'
	print 'Actor, Moives'
	cur.execute('SELECT movie_actor.actor, COUNT(movie.imdb_id) AS actmost FROM movie_actor JOIN movie ON movie_actor.imdb_id = movie.imdb_id WHERE movie.year >=2000 GROUP BY movie_actor.actor ORDER BY actmost DESC LIMIT 10')
	rows = cur.fetchall()
	for row in rows:
		print row[0]+', '+str(row[1])


	#Pairs of actors who co-stared in 3 or more movies:
	print 'Pairs of actors who co-stared in 3 or more movies:'
	print 'Actor A, Actor B, Co-stared Movies'
	cur.execute('SELECT a.actor, b.actor, COUNT(a.imdb_id) AS costar FROM movie_actor a JOIN movie_actor b ON a.imdb_id = b.imdb_id WHERE a.actor <> b.actor GROUP BY a.actor, b.actor HAVING costar >=3 AND a.actor<b.actor ORDER BY costar DESC')
	rows = cur.fetchall()
	for row in rows:
		print row[0]+', '+row[1]+', '+str(row[2])



		



