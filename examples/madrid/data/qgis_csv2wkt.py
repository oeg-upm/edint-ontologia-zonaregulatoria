import csv
from shapely import wkt, force_2d
from shapely.geometry import GeometryCollection

def filter_by_color(csv_file, target_color):
    """Filter CSV by Color and return a GeometryCollection of all matching lines."""
    geometries = []
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Color'] == target_color:
                geom = force_2d(wkt.loads(row['WKT']))
                geometries.append(geom)
    
    return GeometryCollection(geometries)

csv_file = "./ser_wkt_bands.csv"
colors = ["Azul", "Verde"]

for color in colors:

    result = filter_by_color(csv_file, color)
    print("WKT for zone defined as:", color)
    
    with open(f"{color}_bands.wkt", "w+") as wkt_file:
        wkt_file.write(result.wkt)