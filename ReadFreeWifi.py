import json

with open("/Users/kishorebattula/Desktop/Kishore/Wireless_Hotspots_from_DC_Government.geojson", mode='r') as hotspot:
    print(json.dumps(json.load(hotspot),indent=4))

