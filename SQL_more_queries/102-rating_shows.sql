-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT
s.title AS title, 
SUM(sr.rate) AS rating
FROM
tv_shows AS s
JOIN tv_show_ratings AS sr ON s.id = sr.show_id
GROUP BY title
ORDER BY rating DESC;
