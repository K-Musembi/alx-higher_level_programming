/* global $ */
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const $list = $('<ul>');
    $.each(movies, function (idx, movie) {
      $list.append('<li>' + movie.title + '</li>');
    });
    $('#list_movies').empty().append($list);
  });
});
