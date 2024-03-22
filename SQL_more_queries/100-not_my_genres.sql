-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT name 
FROM (SELECT * 
    FROM tv_shows 
    JOIN tv_show_genres tsg 
    ON tv_shows.id = tsg.show_id 
    WHERE title = 'Dexter') 
AS dexter_genre RIGHT
JOIN tv_genres 
ON dexter_genre.genre_id = tv_genres.id 
WHERE genre_id IS NULL ORDER BY name;
