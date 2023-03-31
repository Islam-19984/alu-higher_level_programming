-- list all shows in hbtn_0d_tvsows that have at leaste 1 genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
       FROM tv_shows
       INNER JOIN tv_shows_genres
       ON tv_show.id = tv_show_genres.show_id
       ORDER BY tv_show.title, tv_show_genres.genre_id;
