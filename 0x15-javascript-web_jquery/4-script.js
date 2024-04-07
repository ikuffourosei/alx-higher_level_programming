/* global $ */
function toggle (item) {
  if ($(item).hasClass('red')) {
    $(item).removeClass('red');
    $(item).addClass('green');
  } else if ($(item).hasClass('green')) {
    $(item).removeClass('green');
    $(item).addClass('red');
  }
}

$('#toggle_header').on('click', function () {
  toggle('header');
});
