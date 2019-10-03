$(document).ready(() => {
  data.forEach(doc => {
    // remove html markup from the text
    doc.content = $('<div>')
      .html(doc.content)
      .text()

    // removes footnote markers
    doc.content = doc.content.replace(/\[\^[^\]]\]/gi, '')
  })

  // create a document index for easy retrieval of the search results
  const docs = data.reduce((acc, doc) => {
    acc[doc.id] = doc
    return acc
  })

  // the search index
  const index = lunr(function() {
    this.ref('id')
    this.field('title')
    this.field('content')

    this.metadataWhitelist = ['position']

    data.forEach(function(doc) {
      this.add(doc)
    }, this)
  })

  // gets the search text
  const paramsString = window.location.search
  const searchParams = new URLSearchParams(paramsString)

  if (searchParams.has('text')) {
    const text = searchParams.get('text')
    $('#search-query').html(text)

    try {
      renderResults(index.search(`title:${text}^10 content:${text}`))
    } catch (e) {
      if (e instanceof lunr.QueryParseError) {
      } else {
        throw e
      }
    }
  }

  function renderResults(results) {
    const count = $('#count')
    count.html(results.length)

    const ol = $('ol.results')
    ol.empty()

    results.forEach(result => {
      const doc = docs[result.ref]
      const meta = Object.values(result.matchData.metadata)[0]

      let title = doc.title
      if (meta.title !== undefined) {
        title = highlight(title, meta.title.position)
      }

      let content = doc.content
      let contentCount = 0
      if (meta.content !== undefined) {
        positions = meta.content.position
        content = highlight(content, positions, true)
        contentCount = positions.length
      }

      let li = $('<li class="lazyload">')

      let a = $('<a>').html(title)
      a.attr('href', doc.url)

      let h3 = $('<h3>')
      h3.append(a)

      if (contentCount > 0) {
        h3.append($('<span class="badge">').html(contentCount))
      }

      let p = $('<p>').html(content)

      li.append(h3)
      li.append(p)
      ol.append(li)
    })
  }

  function highlight(value, positions, context = false) {
    const gap = ' [...] '
    const offset = 100

    let text = ''
    let start,
      end = 0

    positions.slice(0, 3).forEach((pos, idx) => {
      if (context) {
        start = pos[0] - offset >= 0 ? pos[0] - offset : 0
      }

      if (idx === 0 && start > 0) {
        text = gap
      }

      end = pos[0]

      text = `${text} ${value.substring(
        start,
        end
      )} <span class="highlight">${value.substring(
        pos[0],
        pos[0] + pos[1]
      )}</span> ${context ? gap : ''}`

      start = pos[0] + pos[1] + 1
    })

    if (context) {
      text = `${text} ${value.substring(start, start + offset)} ${gap}`
    } else {
      text = `${text} ${value.substring(start)}`
    }

    return text
  }
})
