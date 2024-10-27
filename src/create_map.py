import folium

def create_map(bus_stops):
    # Initialize a Folium map centered on the user's current location
    m = folium.Map(location=[39.3643, -74.4229], zoom_start=17)

    # Add CartoDB Positron No Labels layer
    folium.TileLayer(
        tiles="https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png",
        attr="&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors &copy; <a href='https://carto.com/attributions'>CARTO</a>",
        subdomains="abcd",
        max_zoom=20,
        name="CartoDB Positron No Labels"
    ).add_to(m)

    # Add markers for each bus stop
    for stop in bus_stops:
        folium.Marker(
            location=[stop.dlat_gis, stop.dlong_gis],
            popup=stop.description,
            icon=folium.Icon(color='blue')
        ).add_to(m)

    folium.LayerControl().add_to(m)
    
    return m

def save_map(map_instance, filename="map_with_bus_stops.html"):
    map_instance.save(filename)
