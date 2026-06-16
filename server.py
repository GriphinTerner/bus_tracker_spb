import asyncio
import websockets
import requests
from google.transit import gtfs_realtime_pb2
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://transport.orgp.spb.ru/Portal/transport/internalapi/gtfs/realtime/vehicle"
HEADERS = {"User-Agent": "Mozilla/5.0"}

async def send_positions(websocket):
    while True:
        feed = gtfs_realtime_pb2.FeedMessage()
        response = requests.get(URL, headers=HEADERS, verify=False)
        feed.ParseFromString(response.content)

        data = []
        for entity in feed.entity:
            if not entity.vehicle or not entity.vehicle.trip:
                continue
            v = entity.vehicle
            if v.trip.route_id == "26":  # ← точный маршрут
                data.append({
                    "id": entity.id,
                    "lat": v.position.latitude,
                    "lon": v.position.longitude,
                    "timestamp": v.timestamp
                })

        await websocket.send(str(data))
        await asyncio.sleep(3)  # частота обновления

async def main():
    async with websockets.serve(send_positions, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())