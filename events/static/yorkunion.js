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
        var placeName = $('.p-location').text();
        var map = L.map('map', {
            maxBounds: [[53.916, -1.175], [54.008, -0.994]],
            center: coordinates,
            zoom: 16,
            layers: [L.tileLayer('http://www.york.ac.uk/about/maps/campus/data/tiles/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors | <a href="http://www.york.ac.uk/about/maps/campus/">University of York</a>',
                maxZoom: 18,
                minZoom: 13,
            })]
        });
        L.marker(coordinates).addTo(map).bindPopup(placeName).openPopup();
    }

});
