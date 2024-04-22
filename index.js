const { body } = document;

let map;

const canvas = document.createElement("canvas");
const ctx = canvas.getContext("2d");
canvas.width = canvas.height = 100;

const newImg = document.getElementById("map");
newImg.addEventListener("load", onNewImageLoad);
newImg.src =
  "data:image/svg+xml," +
  encodeURIComponent(
    '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><foreignObject width="100%" height="100%"><div xmlns="http://www.w3.org/1999/xhtml"> Hey there...</div></foreignObject></svg>'
  );

const targetImg = document.createElement("map");
body.appendChild(targetImg);

function onNewImageLoad(e) {
  ctx.drawImage(e.target, 0, 0);
  targetImg.src = canvas.toDataURL();
}


function convertasbinaryimage() {
    html2canvas(document.getElementById("map"), {
        onrendered: function (canvas) {
            var img = canvas.toDataURL()
            window.open(img);
            // var img = canvas.toDataURL("image/png");
            // img = img.replace('data:image/png;base64,', '');
            // var finalImageSrc = 'data:image/png;base64,' + img;
            // window.open(img)
            // console.log(finalImageSrc);
        }
    });
}

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
        convertasbinaryimage();
    });
}

initMap();