$(document).ready(function() {

    $(document).foundation();

    // Table of Contents
    // TODO: Improve to use pure CSS selectors as jQuery recommends here:
    // https://api.jquery.com/header-selector/

    // $( ":header" ).each( function() {
    //     alert("this is a heading");
    // });

    // Expande / Collapse
    $('.toggler').on('click', function () {
        $(this).next('.content').slideToggle(400).toggleClass('hide show');
        $(this).toggleClass('close open');

        return false;
    });

    // Cookie disclaimer
    if (!Cookies.get('ego-cookie')) {
        $("#cookie-disclaimer").removeClass('hide');
    }
    // Set cookie and hide the box
    $('#cookie-disclaimer .close').on("click", function() {
        Cookies.set('ego-cookie', 'ego-cookie-set', { expires: 30 });
        $("#cookie-disclaimer").addClass('hide');
    });
});
