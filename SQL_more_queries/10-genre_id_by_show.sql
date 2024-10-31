-- Import the database dump from hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre.id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
