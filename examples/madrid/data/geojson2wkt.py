#!/usr/bin/env python3
import json, sys
from shapely.geometry import shape

with open("ser.geojson") as f:
    data = json.load(f)

geoms = []
if data.get("type") == "FeatureCollection":
    geoms = [shape(f["geometry"]).wkt for f in data.get("features", []) if f.get("geometry")]
elif data.get("type") == "Feature":
    geoms = [shape(data["geometry"]).wkt] if data.get("geometry") else []
elif "coordinates" in data:
    geoms = [shape(data).wkt]

with open("ser.wkt", 'w') as f:
    f.write("\n".join(geoms))
print(f"Wrote {len(geoms)} geometry(ies)")