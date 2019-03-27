$(document).ready(function() {
  const $results = $("#results").isotope({
    itemSelector: ".cell",
    layoutMode: "fitRows"
  });

  $("#results .cell").each(function(i, cell) {
    const tags = cell.querySelectorAll(".tag");

    $(tags).each(function(i, tag) {
      $(cell).addClass($(tag).data("filter"));
    });
  });

  var filters = {};

  $(".filter").change(function() {
    const category = $(this).data("category");
    const value = $(this).val();

    filters[category] = value;

    const filterValue = Object.values(filters).join("");

    $results.isotope({ filter: filterValue });

    const items = $results.isotope("getFilteredItemElements");
    const availableFilters = [
      ...new Set(items.flatMap(x => x.className.split(" ")))
    ];

    $(".filter option").each(function(i, option) {
      const value = option.value.replace(/\./, "");

      if (value) {
        if (availableFilters.includes(value)) {
          $(option).removeAttr("disabled");
        } else {
          $(option).attr("disabled", true);
        }
      }
    });
  });
});
