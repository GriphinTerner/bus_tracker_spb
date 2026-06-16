import requests
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import streamlit as st
from datetime import datetime
from google.transit import gtfs_realtime_pb2
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://transport.orgp.spb.ru/Portal/transport/internalapi/gtfs/realtime/vehicle"
HEADERS = {"User-Agent": "Mozilla/5.0"}

st.set_page_config(page_title="Bus 26 Tracker", layout="wide")
st.title("Автобус 26 — Live Tracking 🚍")

# Инициализация состояния
if "updating" not in st.session_state:
    st.session_state["updating"] = True
if "last_buses" not in st.session_state:
    st.session_state["last_buses"] = []

# Кнопки
col1, col2 = st.columns(2)
if col1.button("🔄 Начать обновление"):
    st.session_state["updating"] = True
if col2.button("⏸️ Остановить обновление"):
    st.session_state["updating"] = False

st.write("Обновление активировано ✅" if st.session_state["updating"] else "Обновление остановлено ⛔")

# Загружаем данные только при обновлении
buses = []

if st.session_state["updating"]:
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(URL, headers=HEADERS, verify=False)
    feed.ParseFromString(response.content)

    for entity in feed.entity:
        if not entity.vehicle or not entity.vehicle.trip:
            continue
        v = entity.vehicle
        if  v.trip.route_id == "1674" :  # фильтр теперь точный
            buses.append(v)

    # 💾 Сохраняем последний успешный результат
    if buses:
        st.session_state["last_buses"] = buses

# ❗Если обновление выключено → используем старые данные
if not st.session_state["updating"]:
    buses = st.session_state["last_buses"]

# ---- Рисуем карту ----
m = folium.Map(location=[59.93, 30.31], zoom_start=12)
cluster = MarkerCluster().add_to(m)

for v in buses:
    lat = v.position.latitude
    lon = v.position.longitude
    ts = datetime.fromtimestamp(v.timestamp).strftime('%H:%M:%S') if v.timestamp else "N/A"
    popup = f"Route: {v.trip.route_id}<br>Time: {ts}"
    folium.Marker([lat, lon], popup=popup).add_to(cluster)

st_folium(m, width=900, height=550)

st.markdown(f"**Всего найдено:** {len(buses)}")
st.markdown(f"_Последнее обновление данных: {datetime.now().strftime('%H:%M:%S')}_")

# Автообновление каждые 5 секунд
if st.session_state["updating"]:
    time.sleep(5)
    st.rerun()