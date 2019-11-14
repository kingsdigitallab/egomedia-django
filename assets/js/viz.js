$(document).ready(() => {
  // 1. prepare the data
  let data = {
    indexByName: new Map(),
    nameByIndex: new Map(),
    matrix: []
  }

  let n = 0

  const getKey = item =>
    `${item.class}:::${item.id}:::${item.title}:::${item.url}`
  const getGroup = idx => data.nameByIndex.get(idx).split(':::')[0]
  const getTitle = idx => data.nameByIndex.get(idx).split(':::')[2]
  const getUrl = idx => data.nameByIndex.get(idx).split(':::')[3]

  // creates a unique index for each object
  vizData.forEach(d => {
    if (!data.indexByName.has((d = getKey(d)))) {
      data.nameByIndex.set(n, d)
      data.indexByName.set(d, n++)
    }
  })

  // creates a square matrix counting related objects
  vizData.forEach(d => {
    const source = data.indexByName.get(getKey(d))
    let row = data.matrix[source]

    if (!row) row = data.matrix[source] = Array.from({ length: n }).fill(0)

    d.related.forEach(d => {
      row[data.indexByName.get(getKey(d))]++
    })
  })

  // 2. d3: settings
  const height = (width = 920)
  const outerRadius = Math.min(width, height) * 0.5
  const innerRadius = outerRadius - 254

  const color = {
    project: '#245d88',
    researcher: '#256019',
    theme: '#ed7a3e'
  }

  const ribbon = d3.ribbon().radius(innerRadius)

  // 3. legend
  // const legend = document.getElementById('viz-legend')

  // for (const property in color) {
  //   const li = document.createElement('li')
  //   li.appendChild(document.createTextNode(property))
  //   li.className = `${property}`
  //   legend.appendChild(li)
  // }

  // 4. d3: render the svg
  const svg = d3
    .select('#viz')
    .append('svg')
    .attr('viewBox', [-width / 2, -height / 2, width, height])
    .attr('font-size', 14)
    .style('width', '100%')
    .style('height', 'auto')

  const chord = d3
    .chord()
    .padAngle(0.04)
    .sortSubgroups(d3.descending)
    .sortChords(d3.descending)

  const chords = chord(data.matrix)

  const group = svg
    .append('g')
    .selectAll('g')
    .data(chords.groups)
    .join('g')

  const arc = d3
    .arc()
    .innerRadius(innerRadius)
    .outerRadius(innerRadius + 20)

  const highlightGroup = opacity => {
    return d => {
      groupPath
        .filter(dd => dd.index != d.index)
        .transition()
        .style('opacity', opacity)
      ribbons
        .filter(dd => dd.source.index != d.index && dd.target.index != d.index)
        .transition()
        .style('opacity', opacity)
    }
  }

  const groupPath = group
    .append('path')
    .attr('fill', d => color[getGroup(d.index)])
    .attr('stroke', d => color[getGroup(d.index)])
    .attr('d', arc)
    .on('mouseover', highlightGroup(0.1))
    .on('mouseout', highlightGroup(1))

  group
    .append('text')
    .each(d => {
      d.angle = (d.startAngle + d.endAngle) / 2
    })
    .attr('dy', '.35em')
    .attr(
      'transform',
      d => `
        rotate(${(d.angle * 180) / Math.PI - 90})
        translate(${innerRadius + 26})
        ${d.angle > Math.PI ? 'rotate(180)' : ''}
      `
    )
    .attr('text-anchor', d => (d.angle > Math.PI ? 'end' : null))
    .attr('class', 'svg-link')
    .text(d => getTitle(d.index))
    .on('click', d => (location.href = getUrl(d.index)))

  group
    .append('title')
    .text(
      d =>
        `${getTitle(d.index)}: ${d.value} connection${d.value > 1 ? 's' : ''}`
    )

  const highlightRibbon = opacity => {
    return d => {
      groupPath
        .filter(
          dd => dd.index !== d.source.index && dd.index !== d.target.index
        )
        .transition()
        .style('opacity', opacity)
      ribbons
        .filter(dd => dd !== d)
        .transition()
        .style('opacity', opacity)
    }
  }

  const ribbons = svg
    .append('g')
    .attr('fill-opacity', 0.75)
    .selectAll('path')
    .data(chords)
    .join('path')
    .attr('stroke', d => d3.rgb(color[getGroup(d.target.index)]).darker(0.25))
    .attr('fill', d => color[getGroup(d.target.index)])
    .attr('d', ribbon)
    .on('mouseover', highlightRibbon(0.1))
    .on('mouseout', highlightRibbon(1))
})
