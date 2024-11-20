fetch('https://swapi-api.hbtn.io/api/films/?format=json').then((response) => response.json()).then((data) => {
    const films = data.results;
    const list = document.getElementById('list_movies');
  
    films.forEach((film) => {
      const item = document.createElement('li');
      item.textContent = film.title;
      list.appendChild(item);
    });
  });
