-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_genres.name, SUM(tv_show_ratings.rate) as rating
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;
