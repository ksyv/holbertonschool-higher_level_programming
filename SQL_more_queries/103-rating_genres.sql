-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT g.name AS name, SUM(sr.rate) AS rating
FROM tv_genres AS g
JOIN tv_show_genres AS sg ON sg.genre_id = g.id
JOIN tv_shows AS s ON sg.show_id = s.id
JOIN tv_show_ratings AS sr ON s.id = sr.show_id
GROUP BY name
ORDER BY rating DESC, name;