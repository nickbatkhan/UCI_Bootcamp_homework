var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson";

 // Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
    // Once we get a response, send the data.features object to the create_Features function
    create_Features(data.features);
    console.log(data.features)
  });
  
function create_Features(earthquakeData) {

    // Define a function we want to run once for each feature in the features array
    // Give each feature a popup describing the place and time of the earthquake
    function onEachFeature(feature, layer) {
        layer.bindPopup("<h3>" + feature.properties.place +
        "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
    }

    //provides color each magnitude
    function color(mag) {
        switch(true) {
            case mag > 5:
                //aqua
                return "#00FFFF";
            case mag > 4:
                //chocolate
                return "#D2691E";
            case mag > 3:
                //dark blue
                return "#00008B";
            case mag > 2:
                //deep pink
                return "#FF1493";
            case mag > 1:
                //fushia
                return "#FF00FF";
            default:
                //gold
                return "#FFD700";
        }
    }
    
    //makes different size for each magnitude
    function circle(mag) {
        return mag * 5
    };

    function style(feature) {
    return {
        radius: circle(feature.properties.mag),
        fillColor: color(feature.properties.mag),
        color: "black",
        weight: 1,
        fillOpacity: 1
        }
    };

    // Create a GeoJSON layer containing the features array on the earthquakeData object
    // Run the onEachFeature function once for each piece of data in the array
    var earthquakes = L.geoJSON(earthquakeData, {
        onEachFeature: onEachFeature,
        style: style,
        pointToLayer: function (feature, latlng) {
              return L.circleMarker(latlng);
          },
    });

    // Sending our earthquakes layer to the createMap function
    createMap(earthquakes);
}
  
  function createMap(earthquakes) {
  
    // Define streetmap and darkmap layers
    var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.streets",
      accessToken: 'pk.eyJ1IjoibnVyYm9sYmF0a2hhbiIsImEiOiJjazQ1eDBwc3IwZTkzM2Zxdjg3MXl3dGd5In0.g0yHQfpanySmObn0CJp2hg'
    });
  
    var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.dark",
      accessToken: 'pk.eyJ1IjoibnVyYm9sYmF0a2hhbiIsImEiOiJjazQ1eDBwc3IwZTkzM2Zxdjg3MXl3dGd5In0.g0yHQfpanySmObn0CJp2hg'
    });
  
    // Define a baseMaps object to hold our base layers
    var baseMaps = {
      "Street Map": streetmap,
      "Dark Map": darkmap
    };
  
    // Create overlay object to hold our overlay layer
    var overlayMaps = {
      Earthquakes: earthquakes
    };
  
    // Create our map, giving it the streetmap and earthquakes layers to display on load
    var myMap = L.map("map", {
      center: [
        37.09, -95.71
      ],
      zoom: 3,
      layers: [streetmap, earthquakes]
    });
  
    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: true
    }).addTo(myMap);
  }