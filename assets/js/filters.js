$(document).ready(() => {
  // add the cards' tags as classes in the cardcontainers for a cleaner isotope filtering
  $('#results .cardcontainer').each(function(i, cardcontainer) {
    const tags = cardcontainer.querySelectorAll('.tag')

    $(tags).each(function(i, tag) {
      $(cardcontainer).addClass($(tag).data('filter'))
    })
  })

  var filters = {}

  showCurrentFilters(filters)

  const $results = $('#results').isotope({
    itemSelector: '.cardcontainer',
    layoutMode: 'fitRows'
  })

  // $results.isotope( 'on', 'arrangeComplete', function() {
  //   $('#results .cardcontainer').each(function() {
  //     // $(this).removeAttr("style")
  //     $(this).css('position', '')
  //            .css('left', '')
  //            .css('top', '');
  //   });
  // });

  // apply filters
  $('.filter').change(function() {
    const category = $(this).data('category')
    const value = $(this).val()

    filters[category] = value

    const filterValue = getFilterValue(filters)

    filterResults($results, filterValue)

    showCurrentFilters(filters)

    toggleClearFilters(filterValue)

    disableUnavailableFilters($results)
  })

  function getFilterValue(filters) {
    if (!filters) {
      return ''
    }

    return Object.values(filters)
      .join('')
      .trim()
  }

  function filterResults(isotopeObj, filterValue) {
    isotopeObj.isotope({
      filter: filterValue
    })
  }

  function showCurrentFilters(filters) {
    $('.remove-filter')
      .parent()
      .remove()

    if (!jQuery.isEmptyObject(filters)) {
      $('.filter option:selected').each(function(i, option) {
        if (option.value) {
          const category = $(option)
            .parent()
            .data('category')
          const text = option.innerText

          let cardcontainer = $('<div class="cardcontainer">')

          let button = $(
            '<button type="button" class="button expanded remove-filter">'
          )
          button.addClass(category)
          // button.html(category + ': ' + text);
          button.html(text)
          button.val(category)

          cardcontainer.append(button)

          $('#current-filters').append(cardcontainer)
        }
      })
    }
  }

  function toggleClearFilters(filterValue) {
    if (filterValue.length > 0) {
      $('#clear-filters').removeAttr('disabled')
    } else {
      $('#clear-filters').attr('disabled', true)
    }
  }

  function disableUnavailableFilters(isotopeObj) {
    const filteredItems = isotopeObj.isotope('getFilteredItemElements')
    const availableFilters = [
      ...new Set(filteredItems.flatMap(x => x.className.split(' ')))
    ]

    $('.filter option').each(function(i, option) {
      const value = option.value.replace(/\./, '')

      if (value) {
        if (availableFilters.includes(value)) {
          $(option).removeAttr('disabled')
        } else {
          $(option).attr('disabled', true)
        }
      }
    })
  }

  // remove all filters
  $('#clear-filters').click(function() {
    filters = {}

    const filterValue = getFilterValue(filters)

    filterResults($results, filterValue)

    showCurrentFilters(filters)

    toggleClearFilters(filterValue)

    resetFilters()
  })

  function resetFilters() {
    $('.filter').each(function(i, select) {
      select.selectedIndex = 0
    })
    $('.filter option:disabled').each(function(i, option) {
      $(option).removeAttr('disabled')
    })
  }

  // remove selected filter
  $('#current-filters').on('click', 'button.remove-filter', function() {
    const category = $(this).val()

    $('.filter.' + category)[0].selectedIndex = 0

    delete filters[category]

    const filterValue = getFilterValue(filters)

    filterResults($results, filterValue)

    showCurrentFilters(filters)

    toggleClearFilters(filterValue)

    disableUnavailableFilters($results)
  })

  // re-load after back button
  if (window.history && window.history.pushState) {
    $('.filter').trigger('change')
  }
})
