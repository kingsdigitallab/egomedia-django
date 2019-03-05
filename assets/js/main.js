$(document).ready(function() {

    $(document).foundation();

    // Table of Contents
    // TODO: Improve to use pure CSS selectors as jQuery recommends here:
    // https://api.jquery.com/header-selector/

    $( ":header" ).each( function() {
        alert("this is a heading");
    });

});
