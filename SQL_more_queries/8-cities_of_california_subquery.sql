SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.if AND states.name = 'California'
ORDER BY cities.id ASC;
