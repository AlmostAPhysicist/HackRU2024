"""
Contains logic for creating and displaying an interactive map using 
the Folium library. This module takes a list of bus stops and overlays 
them on the map, allowing users to visualize their locations and 
navigate through them.
"""

import folium
from bus_stop_controller import BusStopController
controller = BusStopController("data/Bus_Stops_of_NJ_Transit_by_Line.csv")
# controller = BusStopController("data/RAW_Bus_Stops_of_NJ_Transit_by_Line.csv")
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

custom_icon_url = "images/285659_marker_map_icon.png"


for stop in controller.bus_stops:
# for stop in controller.bus_stops[1:1000]:
 # Assign labels based on specific object IDs
    if stop.object_id == 85:
        label = "Home"
    elif stop.object_id == 69:
        label = "James"
    elif stop.object_id == 169:
        label = "Pam"
    elif stop.object_id == 173:
        label = "Harry"
    else:
        label = None
    if label:
        folium.Marker(
            location=[stop.dlat_gis, stop.dlong_gis],
            icon=folium.DivIcon(
                html=f"""
                <div style="
                    font-size: 14px; 
                    color: black; 
                    font-weight: bold; 
                    background-color: white;
                    padding: 5px;
                    border-radius: 5px;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
                    text-align: center;
                    ">
                    {label}
                </div>"""
            )
        ).add_to(m)


    icon = folium.CustomIcon(
        custom_icon_url,
        icon_size=(30, 30)  # Size of the custom icon
    )

        # Add a marker with the custom icon and popup information
    folium.Marker(
        location=[stop.dlat_gis, stop.dlong_gis],
        icon=icon,
        popup=f"<strong>Stop ID:</strong> {stop.object_id}<br><strong>County:</strong> {stop.county}"
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