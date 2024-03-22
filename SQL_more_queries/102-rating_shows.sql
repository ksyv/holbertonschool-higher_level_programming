-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
USE hbtn_0d_tvshows_rate;
SELECT tv_shows.title, SUM(rate) as rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;