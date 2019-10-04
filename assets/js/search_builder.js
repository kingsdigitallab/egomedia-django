const fs = require('fs')
const lunr = require('lunr')

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

  fs.writeFile('assets/js/search_index.json', JSON.stringify(idx), err => {
    if (err) throw err
    console.log('Generated search index!')
  })
})
