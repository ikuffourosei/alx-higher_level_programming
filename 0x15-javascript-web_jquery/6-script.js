/* global $ */
function changeHeader () {
  $('header').text('New Header!!!');
}

$('#update_header').on('click', function () {
  changeHeader();
});
