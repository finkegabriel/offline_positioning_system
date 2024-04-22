let map;

async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
    /*
    Tonto National Park
    33.8719° N, 111.2756° W
    */
    map = new Map(document.getElementById("map"), {
        center: { lat: 33.833378, lng: -111.417358 },
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.SATELLITE,
    });
}

initMap();