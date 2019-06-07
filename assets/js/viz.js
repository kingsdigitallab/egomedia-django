$(document).ready(() => {
  // 1. prepare the data
  data = {
    nodes: [],
    links: []
  }

  const addNode = (nodes, node) => {
    if (!nodes.find(item => item.id === node)) {
      nodes.push({
        id: node,
        name: node
          .split('_')
          .slice(1)
          .join(' '),
        group: node.split('_').shift(),
        sourceLinks: [],
        targetLinks: []
      })
    }

    return nodes
  }

  $('#results .cell').each(function() {
    const classes = $(this)
      .attr('class')
      .split(' ')

    // ignores the first element
    classes.shift()

    const node = classes.shift()

    data.nodes = addNode(data.nodes, node)

    classes.forEach(item => {
      data.nodes = addNode(data.nodes, item)

      data.links.push({
        source: node,
        target: item,
        value: 1
      })
    })
  })

  data.nodes.sort((a, b) => {
    if (a.name < b.name) {
      return -1
    }
    if (a.name > b.name) {
      return 1
    }

    return 0
  })

  const nodeById = new Map(data.nodes.map(d => [d.id, d]))

  data.links = data.links.map(({ source, target, value }) => ({
    source: nodeById.get(source),
    target: nodeById.get(target),
    value
  }))

  for (const link of data.links) {
    const { source, target, value } = link
    source.sourceLinks.push(link)
    target.targetLinks.push(link)
  }

  const colours = {
    project: '#8cc5e3',
    researcher: '#93db83',
    theme: '#fcb049'
  }

  // 2. d3: functions/settings
  const colour = group => {
    if (group in colours) {
      return colours[group]
    }

    return '#e2e2e2'
  }

  const margin = { top: 30, right: 30, bottom: 30, left: 30 }
  const step = 14
  const width = (data.nodes.length - 1) * step + margin.left + margin.right
  const height = 600 + margin.top + margin.bottom

  const x = d3.scalePoint(data.nodes.map(d => d.id), [
    margin.left,
    width - margin.right
  ])

  const arc = d => {
    const x1 = x(d.source.id)
    const x2 = x(d.target.id)
    const r = Math.abs(x2 - x1) / 2
    return `M${x1},${height - step}A${r},${r} 0,0,${
      x1 < x2 ? 1 : 0
    } ${x2},${height - step}`
  }

  // 3. d3: render the svg
  const svg = d3
    .select('#viz')
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .append('g')
    .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')

  const label = svg
    .append('g')
    .attr('font-family', 'sans-serif')
    .attr('font-size', 10)
    .attr('text-anchor', 'end')
    .selectAll('g')
    .data(data.nodes)
    .join('g')
    .attr('id', d => d.id)
    .attr('transform', d => `translate(${x(d.id)},${height - 15})rotate(-45)`)
    .call(g =>
      g
        .append('text')
        .attr('x', -5)
        .attr('dy', '0.35em')
        .attr('fill', d => d3.lab(colour(d.group)).darker(2))
        .text(d => d.name)
    )
    .call(g =>
      g
        .append('circle')
        .attr('r', 3)
        .attr('fill', d => colour(d.group))
    )

  const path = svg
    .insert('g', '*')
    .attr('fill', 'none')
    .attr('stroke-opacity', 0.6)
    .attr('stroke-width', 1.5)
    .selectAll('path')
    .data(data.links)
    .join('path')
    .attr('stroke', d => colour(d.source.group))
    .attr('d', arc)

  const overlay = svg
    .append('g')
    .attr('fill', 'none')
    .attr('pointer-events', 'all')
    .selectAll('rect')
    .data(data.nodes)
    .join('rect')
    .attr('width', step)
    .attr('height', height - margin.top)
    .attr('x', d => x(d.id) - step / 2)
    .attr('y', 2 * margin.bottom)
    .on('mouseover', d => {
      svg.classed('hover', true)
      label.classed('primary', n => n === d)
      label.classed(
        'secondary',
        n =>
          n.sourceLinks.some(l => l.target === d) ||
          n.targetLinks.some(l => l.source === d)
      )
      path
        .classed('primary', l => l.source === d || l.target === d)
        .filter('.primary')
        .raise()
    })
    .on('mouseout', d => {
      svg.classed('hover', false)
      label.classed('primary', false)
      label.classed('secondary', false)
      path.classed('primary', false).order()
    })
})
