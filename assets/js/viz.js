$(document).ready(() => {
  // 1. prepare the data
  let data = {
    indexByName: new Map(),
    nameByIndex: new Map(),
    matrix: []
  }

  let n = 0

  // creates a unique index for each object
  vizData.forEach(d => {
    if (!data.indexByName.has((d = d.title))) {
      data.nameByIndex.set(n, d)
      data.indexByName.set(d, n++)
    }
  })

  // creates a square matrix counting related objects
  vizData.forEach(d => {
    const source = data.indexByName.get(d.title)
    let row = data.matrix[source]

    if (!row) row = data.matrix[source] = Array.from({ length: n }).fill(0)

    d.related.forEach(d => row[data.indexByName.get(d.title)]++)
  })

  console.log(data)

  // 2. d3: functions/settings
  const height = (width = 954)
  const outerRadius = Math.min(width, height) * 0.5
  const innerRadius = outerRadius - 124

  const arc = d3
    .arc()
    .innerRadius(innerRadius)
    .outerRadius(innerRadius + 20)

  const chord = d3
    .chord()
    .padAngle(0.04)
    .sortSubgroups(d3.descending)
    .sortChords(d3.descending)

  const color = d3.scaleOrdinal(d3.schemeCategory10)

  const ribbon = d3.ribbon().radius(innerRadius)

  // 3. d3: render the svg
  const svg = d3
    .select('#viz')
    .append('svg')
    .attr('viewBox', [-width / 2, -height / 2, width, height])
    .attr('font-size', 10)
    .attr('font-family', 'sans-serif')
    .style('width', '100%')
    .style('height', 'auto')

  const chords = chord(data.matrix)

  const group = svg
    .append('g')
    .selectAll('g')
    .data(chords.groups)
    .join('g')

  group
    .append('path')
    .attr('fill', d => color(d.index))
    .attr('stroke', d => color(d.index))
    .attr('d', arc)

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
    .text(d => data.nameByIndex.get(d.index))

  svg
    .append('g')
    .attr('fill-opacity', 0.67)
    .selectAll('path')
    .data(chords)
    .join('path')
    .attr('stroke', d => d3.rgb(color(d.source.index)).darker())
    .attr('fill', d => color(d.source.index))
    .attr('d', ribbon)
})
