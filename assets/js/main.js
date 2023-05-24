$(function () {
  $(document).foundation()

  $('a:not(header a):not(.sup-footer a)')
    .filter(function () {
      return this.hostname && this.hostname !== location.hostname
    })
    .addClass('external')
    .attr('target', '_blank')

  $('.anchor-link').on('click', function () {
    try {
      navigator.clipboard.writeText(
        `${location.href.replace(location.hash, '')}#${$(this).attr('id')}`
      )

      $('#message-success').attr('style', '')
      $('#message-success').removeClass('hide')
    } catch (err) {
      $('#message-alert').attr('style', '')
      $('#message-alert').removeClass('hide')
      console.error('copy link to clipboard failed', err)
    }
  })
})
