$(document).ready(function() {
  var filters = {};

  const $results = $("#results").isotope({
    itemSelector: ".cell",
    layoutMode: "fitRows"
  });

  $("#results .cell").each(function(i, cell) {
    const tags = cell.querySelectorAll(".tag");

    $(tags).each(function(i, tag) {
      const filter =
        tag.className.replace(/\s/, "_") +
        "_" +
        tag.innerText.toLowerCase().replace(/\s/, "");

      $(cell).addClass(filter);
    });
  });

  $(".filter").change(function() {
    const value = $(this)
      .val()
      .toLowerCase();

    $results.isotope({ filter: value });
    d;
  });
});
