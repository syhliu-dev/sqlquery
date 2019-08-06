# Query data in a SQL Database to analyze movie-related questions
Use python to query data in SQL database 


Part 1 
The provided ‘movie_actors_data.txt’ file contains a JSON string on each line. For example, the first line is:
{"rating": 9.3, "genres": ["Crime", "Drama"], "rated": "R", "filming_locations": "Ashland, Ohio, USA", "language": ["English"], "title": "The Shawshank Redemption", "runtime": ["142 min"], "poster": "http://img3.douban.com/lpic/s1311361.jpg", "imdb_url": "http://www.imdb.com/title/tt0111161/", "writers": ["Stephen King", "Frank Darabont"], "imdb_id": "tt0111161", "directors": ["Frank Darabont"], "rating_count": 894012, "actors": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler", "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore", "Jeffrey DeMunn", "Larry Brandenburg", "Neil Giuntoli", "Brian Libby", "David Proval", "Joseph Ragno", "Jude Ciccolella"], "plot_simple": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "year": 1994, "country": ["USA"], "type": "M", "release_date": 19941014, "also_known_as": ["Die Verurteilten"]}

The fields we are interested in are imdb_id , title , rating, genres, actors, and year. You will parse the JSON strings, and load the data into three tables in SQLite, and then write SQL queries to retrieve the data specified.


You will create three tables:
• The “movie_genre” table, which has two columns: imdb_id and genre. A movie typically has multiple genres, and in this case, there should be one row for each genre. If some movie does not have any genre, ignore that movie.
• The “movies” table, which has four columns: imdb_id, title, year, rating
• The “movie_actor” table, which has two columns imdb_id and actor. A movie typically has
multiple actors, and in this case, there should be one row for each actor.
1. Parse input file to get needed data for the three tables and load them into appropriate Python data structure.
2. Create the movie_genre table and load data into it
3. Create the movies table and load data into it
4. Create the movie_actor table and load data into it
5. Write an SQL query to find top 10 genres with most movies and print out the results
6. Write an SQL query to find number of movies broken down by year in chronological order
7. Write an SQL query to find all Sci-Fi movies order by decreasing rating, then by decreasing year if ratings are the same.
8. Write an SQL query to find the top 10 actors who played in most movies in and after year 2000. In case of ties, sort the rows by actor name.
9. Write an SQL query for finding pairs of actors who co-stared in 3 or more movies. The pairs of names must be unique. This means that ‘actor A, actor B’ and ‘actor B, actor A’ are the same pair, so only one of them should appear.

In each pair of actors you print out, the two actors must be ordered alphabetically. The pairs are ordered in decreasing number of movies they co-stared in. In case of ties, the rows are ordered by actors’ names.

