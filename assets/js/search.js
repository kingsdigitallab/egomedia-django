$(document).ready(() => {
  // gets the search text
  const paramsString = window.location.search
  const searchParams = new URLSearchParams(paramsString)

  if (!searchParams.get('text')) {
    $('#search-details').html('No query found!')
    return
  }

  const text = searchParams.get('text')
  $('#search-query').html(text)

  if (build) {
    buildAndSearch(text)
  } else {
    loadAndSearch(text)
  }

  function buildAndSearch(text) {
    // create a document index for easy retrieval of the search results
    const docs = data.reduce((acc, doc) => {
      acc[doc.id] = doc
      return acc
    })

    // the search index
    const index = lunr(function () {
      this.ref('id')
      this.field('title')
      this.field('content')

      this.metadataWhitelist = ['position']

      data.forEach(function (doc) {
        this.add(doc)
      }, this)
    })

    search(text, index, docs)
  }

  function loadAndSearch(text) {
    $.getJSON(docsIndexUrl)
      .done((json) => {
        const docs = json

        $.getJSON(indexUrl)
          .done((json) => {
            const index = lunr.Index.load(json)

            search(text, index, docs)
          })
          .fail((jqxhr, status, error) =>
            console.log(`Request Failed: ${status}, ${error}`)
          )
      })
      .fail((jqxhr, status, error) =>
        console.log(`Request Failed: ${status}, ${error}`)
      )
  }

  function search(text, index, docs) {
    // gets the search text
    const paramsString = window.location.search
    const searchParams = new URLSearchParams(paramsString)

    try {
      renderResults(index.search(text), docs)
    } catch (e) {
      if (e instanceof lunr.QueryParseError) {
      } else {
        throw e
      }
    }
  }

  function renderResults(results, docs) {
    const count = $('#count')
    count.html(results.length)

    const ol = $('ol.results')
    ol.empty()

    results.forEach((result) => {
      const doc = docs[result.ref]

      const meta = {}
      meta.content = {}
      meta.content.position = []
      meta.title = {}
      meta.title.position = []

      Array('title', 'content').forEach((field) => {
        Object.values(result.matchData.metadata).forEach((item) => {
          if (item[field]) {
            Array.prototype.push.apply(
              meta[field].position,
              item[field].position
            )
          }
        })

        meta[field].position.sort((a, b) => {
          if (a[0] < b[0]) {
            return -1
          }
          if (a[0] > b[0]) {
            return 1
          }

          return 0
        })

        // merge contiguous highlight positions
        if (meta[field].position && meta[field].position[0] !== undefined) {
          let positions = [meta[field].position[0]]

          meta[field].position.forEach((item, idx) => {
            if (idx > 0) {
              const prevPos = positions.length - 1
              const prev = positions[prevPos]
              const prevEnd = prev[0] + prev[1] + 1

              if (prevEnd == item[0]) {
                positions[prevPos][1] = prev[1] + item[1] + 1
              } else {
                positions.push(item)
              }
            }
          })

          meta[field].position = positions.slice()
        }
      })

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

        if (idx > 0) {
          const prevPos = positions[idx - 1]
          if (start <= prevPos[0] + prevPos[1]) {
            start = prevPos[0] + prevPos[1] + 1
          }
        }
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

    return text.trim()
  }
})
