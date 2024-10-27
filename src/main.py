"""
This is the main entry point of the Bus Stop Project application.
It initializes the application, sets up the GUI, and starts the event loop.
"""
from bus_stop_controller import BusStopController
def main():
    data_path = 'data/Bus_Stops_of_NJ_Transit_by_Line.csv'
    controller = BusStopController(data_path)
    b = 0
    for i in controller.bus_stops:
        if i.object_id == 85:
            b = i
    # user location start
    user_location = (39.36053, -74.43227)  
    # Find closest bus stops
    
    # Display or use closest stops in your game logic
    for stop in controller.adjacent_bus_stops(b, controller.bus_stops):
        print(f"Closest Stop: {stop.description} at {stop.dlat_gis}, {stop.dlong_gis}")

if __name__ == "__main__":
    main()
