jQuery(document).ready(function($) {
    if ($('#tumescence').length) {
        $('#tumescence').bjqs({
            height       : 480,
            width        : 1000,
            animduration : 200,
            animspeed    : 6000,
            responsive   : true,
            showcontrols : true,
            usecaptions  : false,
            nexttext     : '&rsaquo;',
            prevtext     : '&lsaquo;',
        });
    }
    else if ($('.p-location').length) {
        var coordinates = [$('.p-latitude').attr('value'),$('.p-longitude').attr('value')];
        var placeName = $('.p-location').html();
        placeName = placeName.charAt(0).toUpperCase() + placeName.slice(1);
        var map = L.map('map').setView(coordinates, 16);
        L.tileLayer('http://www.york.ac.uk/about/maps/campus/data/tiles/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors | <a href="http://www.york.ac.uk/about/maps/campus/">University of York</a>',
            maxZoom: 18,
            minZoom:13
        }).addTo(map);
        L.marker(coordinates).addTo(map).bindPopup(placeName).openPopup();
    }
});
