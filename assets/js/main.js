$(document).ready(function() {
  $(document).foundation()

  $('a')
    .filter(function() {
      return this.hostname && this.hostname !== location.hostname
    })
    .addClass('external')
    .attr('target', '_blank')

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
