$(document).ready(() => {
  const jump = document.getElementById('jump-to-content')
  document
    .querySelectorAll('.indexpage, .peopleindexpage')
    .forEach(function (card) {
      const parent = card.parentNode
      const link = document.createElement('a')
      link.href = `#${parent.id}`
      link.innerText = link.title = card.getElementsByTagName('h3')[0].innerText
      jump.appendChild(link)
    })

  // add the cards' tags as classes in the cardcontainers for a cleaner isotope filtering
  $('#results .cardcontainer').each(function (i, cardcontainer) {
    const tags = cardcontainer.querySelectorAll('.tag')

    $(tags).each(function (i, tag) {
      $(cardcontainer).addClass($(tag).data('filter'))
    })
  })

  updateSeparatorCards()

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

    updateSeparatorCards()

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

  function updateSeparatorCards() {
    // fill in the separator cards
    const sepCards = [
      { type: 'index', page: 'themepage', label: 'themes' },
      { type: 'index', page: 'projectpage', label: 'projects' },
      { type: 'peopleindex', page: 'researcherpage', label: 'researchers' }
    ]
    sepCards.forEach(function (obj) {
      const id = `${obj.type}_${obj.label}`
      const el = document.getElementById(id)
      el.className = ''
      el.classList.add('cell', 'cardcontainer', id)

      const card = el.getElementsByClassName(`card ${obj.type}page`)[0]
      card.classList.add(obj.page)

      const pages = [...document.querySelectorAll(`.${obj.page}`)]
      pages.slice(1).forEach(function (page) {
        const parent = page.parentNode
        if (parent.style.display !== 'none') {
          const tags = [...new Set([...parent.classList].slice(2))]

          el.classList.add(...tags)
        }
      })
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
    const availableFilters = getAvailableFilters(isotopeObj)

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

  function getAvailableFilters(isotopeObj) {
    const filteredItems = isotopeObj.isotope('getFilteredItemElements')
    return [...new Set(filteredItems.flatMap((x) => x.className.split(' ')))]
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

    updateSeparatorCards()

    showCurrentFilters(filters)

    toggleClearFilters(filterValue)

    disableUnavailableFilters($iso)
  })

  // re-load after back button
  if (window.history && window.history.pushState) {
    $('.filter').trigger('change')
  }
})
