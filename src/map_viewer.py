"""
Contains logic for creating and displaying an interactive map using 
the Folium library. This module takes a list of bus stops and overlays 
them on the map, allowing users to visualize their locations and 
navigate through them.
"""

import folium
from bus_stop_controller import BusStopController
controller = BusStopController("data/Bus_Stops_of_NJ_Transit_by_Line.csv")
origin=None
for i in controller.bus_stops:
    if i.object_id == 85:
        origin = i


# Initialize a Folium map centered on Atlantic City
m = folium.Map(location=[origin.dlat_gis, origin.dlong_gis], zoom_start=17)  # Atlantic City's coordinates

# Add CartoDB Positron No Labels layer
folium.TileLayer(
    tiles="https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png",
    attr="&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors &copy; <a href='https://carto.com/attributions'>CARTO</a>",
    subdomains="abcd",
    max_zoom=20,
    name="CartoDB Positron No Labels"
).add_to(m)



for stop in controller.bus_stops:
    folium.CircleMarker(
        location=[stop.dlat_gis, stop.dlong_gis],   # Use the latitude and longitude of the stop
        radius=5,                          # Size of the circle
        color='blue',                      # Outline color of the circle
        fill=False                         # No fill to make it an empty circle
    ).add_to(m)

    
# Add a label with the stop's object_id above the circle marker
    folium.Marker(
        location=[stop.dlat_gis, stop.dlong_gis],
        icon=folium.DivIcon(
            html=f'<div style="font-size: 10px; color: black; text-align: center; transform: translate(-50%, -20px);">{stop.object_id}</div>'
        )
    ).add_to(m)


# Add Layer Control to toggle between map layers
folium.LayerControl().add_to(m)

# Save the map to an HTML file and display
m.save("map_with_cartodb_positron_atlantic_city.html")

import webbrowser
import os

# Specify the path to your HTML file
file_path = os.path.abspath("map_with_cartodb_positron_atlantic_city.html")

# Open the HTML file in the default browser
webbrowser.open(f"file://{file_path}")