$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (titles) {
  for (const i of titles.results){
    $('#list_movies').append(`<li>${i.title}</li>`);
  }
});
