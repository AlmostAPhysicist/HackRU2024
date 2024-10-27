"""
Sets up the graphical user interface (GUI) for the Bus Stop Project.
Uses Tkinter to create windows, buttons, and display elements for 
user interaction. This module also connects user actions to the 
appropriate controller functions.
"""
import folium
import tkinter as tk
from tkinterweb import HtmlFrame
from bus_stop_controller import BusStopController
import os

def create_map():
    # Initialize the bus stop controller and find the origin stop
    controller = BusStopController("data/Bus_Stops_of_NJ_Transit_by_Line.csv")
    origin = None
    for stop in controller.bus_stops:
        if stop.object_id == 85:
            origin = stop
            break

    # Initialize a Folium map centered on Atlantic City
    m = folium.Map(location=[origin.dlat_gis, origin.dlong_gis], zoom_start=17)

    # Add CartoDB Positron No Labels layer
    folium.TileLayer(
        tiles="https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png",
        attr="&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors &copy; <a href='https://carto.com/attributions'>CARTO</a>",
        subdomains="abcd",
        max_zoom=20,
        name="CartoDB Positron No Labels"
    ).add_to(m)

    # Add bus stop markers with labels
    for stop in controller.bus_stops:
        # Add empty circle marker
        folium.CircleMarker(
            location=[stop.dlat_gis, stop.dlong_gis],
            radius=5,
            color='blue',
            fill=False
        ).add_to(m)

        # Add object_id label above the circle marker
        folium.Marker(
            location=[stop.dlat_gis, stop.dlong_gis],
            icon=folium.DivIcon(
                html=f'<div style="font-size: 10px; color: black; text-align: center; transform: translate(-50%, -20px);">{stop.object_id}</div>'
            )
        ).add_to(m)

    # Add Layer Control to toggle between map layers
    folium.LayerControl().add_to(m)

    # Save the map to an HTML file in the current working directory
    map_path = os.path.join(os.getcwd(), "map_with_cartodb_positron_atlantic_city.html")
    m.save(map_path)
    return map_path

# Create the main GUI application window
root = tk.Tk()
root.title("Interactive Map Viewer")
root.geometry("800x600")

# Create a frame to display the HTML map inside the Tkinter window
frame = HtmlFrame(root, messages_enabled=False)

# Generate the map and display it in the HtmlFrame
map_path = create_map()
frame.load_file(f"file:///{map_path.replace('\\', '/')}")  # Adjust for Windows path

frame.pack(fill="both", expand=True)

# Run the application
root.mainloop()
