import geopandas as gpd
import osmnx as ox
from shapely.geometry import MultiPolygon
#also can be used for extracting any tag from osm 
# Load geojson with place you want to extract roads
gdf = gpd.read_file(r"tamil_nadu.geojson")

# Merge all geometries into one
geom = gdf.geometry.unary_union
if not isinstance(geom, MultiPolygon):
    geom = MultiPolygon([geom])

# Log the number of polygons being processed
print(f"Starting Overpass query for {len(geom.geoms)} polygons...")

# Custom filter for highways 
tags = {'highway': True}

# Use OSMnx's built-in logging
ox.settings.log_console = True
ox.settings.use_cache = True  

# Perform the query with print info
print("Downloading OSM highway data (this may take a while)...")
highways = ox.features_from_polygon(geom, tags=tags)
print("Download complete.")

# Save result
highways.to_file("roads_inside_TN.geojson", driver="GeoJSON")
print("Saved to roads_inside_TN.geojson")