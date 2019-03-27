$(document).ready(function() {
  // add the cards' tags as classes in the cells for a cleaner isotope filtering
  $('#results .cell').each(function(i, cell) {
    const tags = cell.querySelectorAll('.tag');

    $(tags).each(function(i, tag) {
      $(cell).addClass($(tag).data('filter'));
    });
  });

  var filters = {};

  const $results = $('#results').isotope({
    itemSelector: '.cell',
    layoutMode: 'fitRows'
  });

  // apply filters
  $('.filter').change(function() {
    const category = $(this).data('category');
    const value = $(this).val();

    filters[category] = value;

    const filterValue = getFilterValue(filters);

    filterResults($results, filterValue);

    toggleClearFilters(filterValue);

    disableUnavailableFilters($results);
  });

  function getFilterValue(filters) {
    if (!filters) {
      return '';
    }

    return Object.values(filters).join('').trim();
  }

  function filterResults(isotopeObj, filterValue) {
    isotopeObj.isotope({
      filter: filterValue
    });
  }

  function toggleClearFilters(filterValue) {
    if (filterValue.length > 0) {
      $('#clear-filters').removeAttr('disabled');
    } else {
      $('#clear-filters').attr('disabled', true);
    }
  }

  function disableUnavailableFilters(isotopeObj) {
    const filteredItems = isotopeObj.isotope('getFilteredItemElements');
    const availableFilters = [
      ...new Set(filteredItems.flatMap(x => x.className.split(' ')))
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
  }

  // remove filters
  $('#clear-filters').click(function() {
    filters = {};

    const filterValue = getFilterValue(filters);

    filterResults($results, filterValue);

    toggleClearFilters(filterValue);

    resetFilters();
  });

  function resetFilters() {
    $('.filter').each(function(i, select) {
      select.selectedIndex = 0;
    });
    $('.filter option:disabled').each(function(i, option) {
      $(option).removeAttr('disabled');
    });
  }
});