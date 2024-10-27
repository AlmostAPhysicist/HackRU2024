"""
Handles the logic for managing bus stops, including loading bus stop 
data from a CSV file, filtering stops based on user input, and 
navigating between stops. This class acts as the intermediary between 
the data model and the GUI.
"""
from csv_utils import load_bus_stops
import math

class BusStopController:
    def __init__(self, data_path):
        self.bus_stops = load_bus_stops(data_path)
        self.current_stop = None
        self.visited_stops = []

    def set_current_stop(self, stop_id):
        # Set the player's current bus stop
        self.current_stop = next((stop for stop in self.bus_stops if stop.object_id == stop_id), None)
        if self.current_stop:
            self.visited_stops.append(self.current_stop)

    def get_next_stops(self):
        # Get adjacent bus stops based on POINT2ID
        return self.adjacent_bus_stops(self.current_stop, self.bus_stops)

    def has_reached_landmark(self, landmark):
        # Check if the current stop matches the landmark
        return self.current_stop and landmark in self.current_stop.description
   # def __init__(self, data_path):
    #    bus_stops_raw = load_bus_stops(data_path)
     #   self.bus_stops = {}
     #   for i in bus_stops_raw:
      #      self.bus_stops[i.object_id] = i



    def adjacent_bus_stops(self, curr_bus_stop, bus_stops):
        # Implement logic to find the adjacent bus stops to the user's current bus stop
        adjacent_stops = []
        
        for stop in self.bus_stops:
            if stop.object_id in curr_bus_stop.point2id:
                adjacent_stops.append(stop)
        return adjacent_stops
    
    def calculate_angle(self, a, b, c, d):
        #Calculates the angle beween two points (a,b) and (c,d) wrt to the positive x-axis
        #returns a value between 0 to 2pi
        delta_x = c - a
        delta_y = d - b
        angle = math.atan2(delta_y, delta_x)  # atan2 returns the angle in radians
        if angle < 0:
            angle += 2 * math.pi  # adjust range to 0 to 2pi
        return angle
        
    ### BoilerPlate Code for the circular pop up...
    # controller = BusStopController("path")
    # b = controller.bus_stops[85] #home
    # for i in b.adjacent_bus_stops(b, controller.bus_stops):
    #   angle = controller.calculate_angle(b.dlat, b.dlon, i.dlat, b.dlon)
    #   i.plot_image(i.image, b.dlat + radius*cos(angle), b.dlong + radius*sin(angle))
    #      ## plot_image is a fictional function that takes in (image, x, y) in our map
    # def plot_image
    #   pass





