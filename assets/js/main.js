$(document).ready(function() {
  $(document).foundation()

  $('a')
    .filter(function() {
      return this.hostname && this.hostname !== location.hostname
    })
    .addClass('external')
    .attr('target', '_blank')

  $('.anchor-link').click(function() {
    try {
      let $field = $('<input>', {
        'class': 'to-copy',
        'type': 'text',
        'value': location.href.replace(location.hash, '') + '#' + $(
            this)
          .attr('id')
      })

      $(this).append($field)
      $field.focus()
      $field.select()

      document.execCommand('copy')

      $field.remove()

      $('#message-success').attr('style', '')
      $('#message-success').removeClass('hide')
    } catch (err) {
      $('#message-aler').attr('style', '')
      $('#message-alert').removeClass('hide')
      console.log('copy execCommand failed', err)
    }
  })

  // Expande / Collapse
  $('.toggler').on('click', function() {
    $(this)
      .siblings('.sub')
      .slideToggle(400)
      .toggleClass('hide show')
    $(this).toggleClass('close open')

    return false
  })

  // Cookie disclaimer
  if (!Cookies.get('ego-cookie')) {
    $('#cookie-disclaimer').removeClass('hide')
  }
  // Set cookie and hide the box
  $('#cookie-disclaimer .close').on('click', function() {
    Cookies.set('ego-cookie', 'ego-cookie-set', {
      expires: 30
    })
    $('#cookie-disclaimer').addClass('hide')
  })
})
