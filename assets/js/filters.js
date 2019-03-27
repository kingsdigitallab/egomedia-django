$(document).ready(function() {
  const $results = $('#results').isotope({
    itemSelector: '.cell',
    layoutMode: 'fitRows'
  });

  $('#results .cell').each(function(i, cell) {
    const tags = cell.querySelectorAll('.tag');

    $(tags).each(function(i, tag) {
      $(cell).addClass($(tag).data('filter'));
    });
  });

  var filters = {};

  $('.filter').change(function() {
    const category = $(this).data('category');
    const value = $(this).val();

    filters[category] = value;

    const filterValue = Object.values(filters).join('').trim();

    if (filterValue.length > 0) {
      $('#clear-filters').removeAttr('disabled');
    } else {
      $('#clear-filters').attr('disabled', true);
    }

    $results.isotope({
      filter: filterValue
    });

    const items = $results.isotope('getFilteredItemElements');
    const availableFilters = [
      ...new Set(items.flatMap(x => x.className.split(' ')))
    ];

    $('.filter option').each(function(i, option) {
      const value = option.value.replace(/\./, '');

      if (value) {
        if (availableFilters.includes(value)) {
          $(option).removeAttr('disabled');
        } else {
          $(option).attr('disabled', true);
        }
      }
    });
  });

  $('#clear-filters').click(function() {
    $(this).attr('disabled', true);

    filters = {};
    $results.isotope({
      filter: '*'
    });

    $('.filter option:disabled').each(function(i, option) {
      $(option).removeAttr('disabled');
    });
    $('.filter').each(function(i, select) {
      select.selectedIndex = 0;
    });
  });
});