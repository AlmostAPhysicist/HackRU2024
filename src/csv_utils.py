import pandas as pd
from bus_stop import BusStop

def load_bus_stops(data_path):
    bus_stops = []
    df = pd.read_csv(data_path)
    for _, row in df.iterrows():
        bus_stop = BusStop(
            object_id=row['OBJECTID'],
            county=row['COUNTY'],
            description=row['DESCRIPTION_BSL'],
            direction_op=row['DIRECTION_OP'],
            dlat_gis=row['DLAT_GIS'],
            dlong_gis=row['DLONG_GIS'],
            line=row['LINE'],
            municipality=row['MUNICIPALITY'],
            stop_num=row['STOP_NUM'],
            stop_type=row['STOP_TYPE'],
            street_dir=row['STREET_DIR'],
            heading=row['HEADING'],
            image=row['IMAGE'],
            point2id=[int(i) for i in str(row['POINT2ID']).split(';')]
        )
        bus_stops.append(bus_stop)
    return bus_stops
