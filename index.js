const { body } = document;

let map;

function convertZoomToRange(zoom) {
    const range = 35200000 / (Math.pow(2, zoom));
    console.log("alt. ", range, " ft");
    // if(range<300) range = 300;
    return range;
}

async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
    /*
    Tonto National Park
    33.8719° N, 111.2756° W
    */
    map = new Map(document.getElementById("map"), {
        center: { lat: 33.833378, lng: -111.417358 },
        mapTypeId: google.maps.MapTypeId.SATELLITE,
        zoom: 12,
    });
    await google.maps.event.addListener(map, 'zoom_changed', function () {
        const zoomLevel = map.getZoom();
        convertZoomToRange(zoomLevel);
        htmlToImage.toPng(document.getElementById('map'),{width:500,height:500,pixelRatio:1})//,canvasWidth:1000, canvasHeight:500})
        .then(function (dataUrl) {
            console.log(dataUrl);
        });
    });
}

initMap();