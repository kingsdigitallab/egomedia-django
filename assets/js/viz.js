$(document).ready(function() {
  data = {
    nodes: Array(),
    links: Array()
  }

  $('#results .cell').each(function() {
    const classes = $(this)
      .attr('class')
      .split(' ')

    // ignore the first element
    classes.shift()

    const node = classes.shift()

    if (!data.nodes.includes(node)) {
      data.nodes.push({
        id: node,
        name: node,
        group: node.split('_').shift()
      })
    }

    classes.forEach(function(item) {
      if (!data.nodes.includes(item)) {
        data.nodes.push({
          id: item,
          name: item,
          group: item.split('_').shift()
        })
      }

      data.links.push({
        source: node,
        target: item,
        value: 1
      })
    })
  })

  data.nodes.sort(function(a, b) {
    if (a.id > b.id) {
      return -1
    }
    if (a.id < b.id) {
      return 1
    }

    return 0
  })

  // d3
  var margin = { top: 0, right: 30, bottom: 50, left: 60 },
    width = 1440 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom

  // append the svg object to the body of the page
  var svg = d3
    .select('#viz')
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .append('g')
    .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')

  // list of node names
  var allNodes = data.nodes.map(function(d) {
    return d.name
  })

  // list of groups
  var allGroups = data.nodes.map(function(d) {
    return d.group
  })
  allGroups = [...new Set(allGroups)]

  // a color scale for groups:
  var color = d3
    .scaleOrdinal()
    .domain(allGroups)
    .range(d3.schemeSet3)

  // a linear scale for node size
  var size = d3
    .scaleLinear()
    .domain([1, 10])
    .range([2, 10])

  // a linear scale to position the nodes on the X axis
  var x = d3
    .scalePoint()
    .range([0, width])
    .domain(allNodes)

  // In my input data, links are provided between nodes -id-, NOT between node names.
  // So I have to do a link between this id and the name
  idToNode = {}
  data.nodes.forEach(function(n) {
    idToNode[n.id] = n
  })

  // Add the links
  var links = svg
    .selectAll('mylinks')
    .data(data.links)
    .enter()
    .append('path')
    .attr('d', function(d) {
      start = x(idToNode[d.source].name) // X position of start node on the X axis
      end = x(idToNode[d.target].name) // X position of end node
      return [
        'M',
        start,
        height - 30, // the arc starts at the coordinate x=start, y=height-30 (where the starting node is)
        'A', // This means we're gonna build an elliptical arc
        (start - end) / 2,
        ',', // Next 2 lines are the coordinates of the inflexion point. Height of this point is proportional with start - end distance
        (start - end) / 2,
        0,
        0,
        ',',
        start < end ? 1 : 0,
        end,
        ',',
        height - 30
      ] // We always want the arc on top. So if end is before start, putting 0 here turn the arc upside down.
        .join(' ')
    })
    .style('fill', 'none')
    .attr('stroke', 'grey')
    .style('stroke-width', 1)

  // Add the circle for the nodes
  var nodes = svg
    .selectAll('mynodes')
    .data(data.nodes)
    .enter()
    .append('circle')
    .attr('cx', function(d) {
      return x(d.name)
    })
    .attr('cy', height - 30)
    .attr('r', function(d) {
      return size(5)
    })
    .style('fill', function(d) {
      return color(d.group)
    })
    .attr('stroke', 'white')

  // And give them a label
  var labels = svg
    .selectAll('mylabels')
    .data(data.nodes)
    .enter()
    .append('text')
    .attr('font-size', 10)
    .attr('transform', function(d) {
      return 'translate(' + x(d.id) + ',' + (height - 15) + ')rotate(-90)'
    })
    .attr('x', 0)
    .attr('y', 0)
    .text(function(d) {
      return d.name
    })
    .style('text-anchor', 'end')

  // Add the highlighting functionnality
  nodes
    .on('mouseover', function(d) {
      // Highlight the nodes: every node is green except of him
      nodes.style('opacity', 0.2)
      d3.select(this).style('opacity', 1)
      // Highlight the connections
      links
        .style('stroke', function(link_d) {
          return link_d.source === d.id || link_d.target === d.id
            ? color(d.group)
            : '#b8b8b8'
        })
        .style('stroke-opacity', function(link_d) {
          return link_d.source === d.id || link_d.target === d.id ? 1 : 0.2
        })
        .style('stroke-width', function(link_d) {
          return link_d.source === d.id || link_d.target === d.id ? 4 : 1
        })
      labels.attr('font-size', function(label_d) {
        return label_d.name === d.name ? 16 : 5
      })
    })
    .on('mouseout', function(d) {
      nodes.style('opacity', 1)
      links
        .style('stroke', 'grey')
        .style('stroke-opacity', 0.8)
        .style('stroke-width', '1')
      labels.attr('font-size', 10)
    })
})
