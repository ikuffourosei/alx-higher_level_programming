/* global $ */
function addItem () {
  const item = $('<li></li>').text('Item');
  $('UL.my_list').append(item);
}

$('#add_item').on('click', function () {
  addItem();
});
