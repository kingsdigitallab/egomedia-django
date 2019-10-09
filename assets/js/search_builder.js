const fs = require('fs')
const lunr = require('lunr')
const zlib = require('zlib')

fs.readFile('assets/js/search_data.json', (err, data) => {
  if (err) throw err

  const documents = JSON.parse(data)

  const idx = lunr(function() {
    this.ref('id')
    this.field('title')
    this.field('content')

    this.metadataWhitelist = ['position']

    documents.forEach(doc => {
      this.add(doc)
    }, this)
  })

  const searchIndex = JSON.stringify(idx)

  fs.writeFile('assets/js/search_index.json', searchIndex, err => {
    if (err) throw err
    console.log('. generated search index')
  })

  let buffer = Buffer.from(searchIndex, 'utf-8')
  zlib.gzip(buffer, (err, result) => {
    if (err) throw err

    fs.writeFile('assets/js/search_index.json.gz', result, err => {
      if (err) throw err
      console.log('. generated compressed search index')
    })
  })

  const docsIndex = JSON.stringify(
    documents.reduce((acc, doc) => {
      acc[doc.id] = doc
      return acc
    })
  )

  fs.writeFile('assets/js/search_docs_index.json', docsIndex, err => {
    if (err) throw err
    console.log('. generated search documents index')
  })

  buffer = Buffer.from(docsIndex, 'utf-8')
  zlib.gzip(buffer, (err, result) => {
    if (err) throw err

    fs.writeFile('assets/js/search_docs_index.json.gz', result, err => {
      if (err) throw err
      console.log('. generated compressed search documents index')
    })
  })
})
