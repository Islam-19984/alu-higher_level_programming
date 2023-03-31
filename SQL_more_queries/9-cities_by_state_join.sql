-- script that lists all cities comtained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
       FROM cities
       INNER JOIN states
       ON states.id = cities.state_id
       ORDER BY cities.id;