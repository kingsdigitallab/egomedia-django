$(document).ready(() => {
  // add the cards' tags as classes in the cardcontainers for a cleaner isotope filtering
  $('#results .cardcontainer').each(function (i, cardcontainer) {
    const tags = cardcontainer.querySelectorAll('.tag')

    $(tags).each(function (i, tag) {
      $(cardcontainer).addClass($(tag).data('filter'))
    })
  })
  // fill in the separator cards
  ;[
    { type: 'theme', label: 'themes' },
    { type: 'project', label: 'sections' },
    { type: 'researcher', label: 'contributors' }
  ].forEach(function (obj) {
    document.querySelectorAll(`.${obj.type}page`).forEach(function (page) {
      const tags = [...page.parentNode.classList].slice(2)
      tags.forEach(function (tag) {
        $(`#${obj.type}_${obj.label}`).addClass(tag)
      })
    })
  })

  var filters = {}

  showCurrentFilters(filters)

  const $iso = $('#results').isotope({
    itemSelector: '.cardcontainer',
    layoutMode: 'fitRows'
  })

  $iso.isotope('on', 'arrangeComplete', () => toggleStyle(true))

  // apply filters
  $('.filter').change(function () {
    toggleStyle()

    const category = $(this).data('category')
    const value = $(this).val()

    filters[category] = value

    const filterValue = getFilterValue(filters)

    filterResults($iso, filterValue)

    showCurrentFilters(filters)

    toggleClearFilters(filterValue)

    disableUnavailableFilters($iso)
  })

  function toggleStyle(remove = false) {
    if (remove) {
      $('#results .cardcontainer').each(function () {
        $(this).data('left', $(this).css('left'))
        $(this).data('position', $(this).css('position'))
        $(this).data('top', $(this).css('top'))
        $(this).css('left', '')
        $(this).css('position', '')
        $(this).css('top', '')
      })
    } else {
      $('#results .cardcontainer').each(function () {
        $(this).css('left', $(this).data('left'))
        $(this).css('position', $(this).data('position'))
        $(this).css('top', $(this).data('top'))
      })
    }
  }

  function getFilterValue(filters) {
    if (!filters) {
      return ''
    }

    return Object.values(filters).join('').trim()
  }

  function filterResults(isotopeObj, filterValue) {
    isotopeObj.isotope({
      filter: filterValue
    })
  }

  function showCurrentFilters(filters) {
    $('.remove-filter').parent().remove()

    if (!jQuery.isEmptyObject(filters)) {
      $('.filter option:selected').each(function (i, option) {
        if (option.value) {
          const category = $(option).parent().data('category')
          const text = option.innerText

          let cardcontainer = $('<div class="cell cardcontainer">')

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
      ...new Set(filteredItems.flatMap((x) => x.className.split(' ')))
    ]

    $('.filter option').each(function (i, option) {
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
  $('#clear-filters').click(function () {
    toggleStyle()

    filters = {}

    const filterValue = getFilterValue(filters)

    filterResults($iso, filterValue)

    showCurrentFilters(filters)

    toggleClearFilters(filterValue)

    resetFilters()
  })

  function resetFilters() {
    $('.filter').each(function (i, select) {
      select.selectedIndex = 0
    })
    $('.filter option:disabled').each(function (i, option) {
      $(option).removeAttr('disabled')
    })
  }

  // remove selected filter
  $('#current-filters').on('click', 'button.remove-filter', function () {
    toggleStyle()

    const category = $(this).val()

    $('.filter.' + category)[0].selectedIndex = 0

    delete filters[category]

    const filterValue = getFilterValue(filters)

    filterResults($iso, filterValue)

    showCurrentFilters(filters)

    toggleClearFilters(filterValue)

    disableUnavailableFilters($iso)
  })

  // re-load after back button
  if (window.history && window.history.pushState) {
    $('.filter').trigger('change')
  }
})
