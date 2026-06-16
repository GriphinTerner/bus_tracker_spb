import requests
from datetime import datetime
from google.transit import gtfs_realtime_pb2
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://transport.orgp.spb.ru/Portal/transport/internalapi/gtfs/realtime/vehicle"
HEADERS = {"User-Agent": "Mozilla/5.0"}

feed = gtfs_realtime_pb2.FeedMessage()

response = requests.get(URL, headers=HEADERS, verify=False)
response.raise_for_status()
feed.ParseFromString(response.content)

print("Текущее время:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "\n")

found = False
for entity in feed.entity:
    if not entity.vehicle or not entity.vehicle.trip:
        continue

    v = entity.vehicle
    route_id = v.trip.route_id

    if "26" in route_id:
        found = True
        print("НАЙДЕН АВТОБУС 26")
        print("Route ID:", route_id)
        print("Vehicle ID:", v.vehicle.id)
        print("Latitude:", v.position.latitude)
        print("Longitude:", v.position.longitude)
        if v.timestamp:
            print("Последнее обновление:", datetime.fromtimestamp(v.timestamp))
        print("-"*40)

if not found:
    print("Автобус 26 не найден в потоке. Возможно, не на линии.")