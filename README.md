# Bus 26 Live Tracker

Bus 26 Live Tracker is a real-time web application for tracking bus route 26 in Saint Petersburg.

The project receives live public transport data from a GTFS Realtime feed, processes vehicle positions on a Python backend, and displays buses on an interactive Leaflet map in the browser.

## Stack

- Python
- WebSockets
- requests
- urllib3
- GTFS Realtime
- Leaflet.js
- OpenStreetMap
- HTML
- JavaScript
- Streamlit
- Folium

## Features

- Real-time bus tracking
- Interactive map with Leaflet.js
- OpenStreetMap tile layer
- Python WebSocket backend
- GTFS Realtime vehicle position parsing
- Live vehicle marker updates
- Browser-based frontend
- Optional Streamlit/Folium version
- Utility script for checking route IDs
- Lightweight project structure

## Project structure

```text
server.py
tracker_26.py
test.py
index.html
tracker_26_live.html
requirements.txt
README.md
```

## Requirements

- Python 3.10+
- pip
- virtualenv
- Modern web browser
- Internet connection

## How the project works

The recommended launch mode is:

```text
GTFS Realtime API
        ↓
Python backend server.py
        ↓
WebSocket ws://localhost:8765
        ↓
Browser frontend index.html
        ↓
Leaflet map with live bus markers
```

The backend receives live vehicle data, filters buses by route, and sends coordinates to the browser through WebSocket.

The frontend receives bus coordinates and updates markers on the map in real time.

## Installation

Clone the repository:

```bash
git clone https://github.com/GriphinTerner/bus_tracker_spb.git
cd bus_tracker_spb
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment on macOS / Linux:

```bash
source venv/bin/activate
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Upgrade pip:

```bash
pip install --upgrade pip
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to run

The project should be launched in two terminals.

### Terminal 1: start the backend

Run:

```bash
python server.py
```

The backend should start a WebSocket server at:

```text
ws://localhost:8765
```

Keep this terminal open.

### Terminal 2: start the frontend server

Open a second terminal in the project folder.

Run:

```bash
python -m http.server 8000
```

### Open the project in browser

Open:

```text
http://localhost:8000/index.html
```

The browser should show a map of Saint Petersburg with live bus markers.

## Full run commands for macOS / Linux

```bash
git clone https://github.com/GriphinTerner/bus_tracker_spb.git
cd bus_tracker_spb

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python server.py
```

Then open a second terminal:

```bash
cd bus_tracker_spb
source venv/bin/activate

python -m http.server 8000
```

Open in browser:

```text
http://localhost:8000/index.html
```

## Full run commands for Windows

```bash
git clone https://github.com/GriphinTerner/bus_tracker_spb.git
cd bus_tracker_spb

python -m venv venv
venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r requirements.txt

python server.py
```

Then open a second terminal:

```bash
cd bus_tracker_spb
venv\Scripts\activate

python -m http.server 8000
```

Open in browser:

```text
http://localhost:8000/index.html
```

## Alternative Streamlit launch

The project also contains a Streamlit/Folium version.

Run:

```bash
streamlit run tracker_26.py
```

If the `streamlit` command is not available, run:

```bash
python -m streamlit run tracker_26.py
```

Streamlit will print a local URL, usually:

```text
http://localhost:8501
```

Open that URL in your browser.

## Files description

### `server.py`

Main Python backend.

It connects to the GTFS Realtime vehicle feed, parses vehicle positions, filters buses by route, and sends coordinates to the browser through WebSocket.

The frontend expects this server to be available at:

```text
ws://localhost:8765
```

### `index.html`

Main frontend file.

It creates a Leaflet map, connects to the local WebSocket backend, receives bus coordinates, and updates bus markers on the map.

This is the recommended frontend file for normal project launch.

### `tracker_26.py`

Alternative Streamlit/Folium version of the tracker.

It can be launched with:

```bash
streamlit run tracker_26.py
```

### `tracker_26_live.html`

Experimental direct-browser version.

This file tries to load GTFS Realtime data directly from the browser.

It may not work correctly because public APIs can block direct browser requests due to CORS restrictions.

The recommended version is:

```text
server.py + index.html
```

### `test.py`

Utility script for checking GTFS Realtime data and route IDs.

Run it if buses are not displayed:

```bash
python test.py
```

Use this file to check whether the transport API uses an internal route ID instead of the public route number.

### `requirements.txt`

Project dependencies:

```text
requests
urllib3
websockets
gtfs-realtime-bindings
folium
streamlit
streamlit-folium
```

Install them with:

```bash
pip install -r requirements.txt
```

## Troubleshooting

### The map opens, but no buses appear

Make sure the backend is running:

```bash
python server.py
```

Make sure the frontend is opened through the local server:

```text
http://localhost:8000/index.html
```

Do not open `index.html` by double-clicking it.

Use:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/index.html
```

### WebSocket connection failed

Check that `server.py` is running.

The frontend connects to:

```text
ws://localhost:8765
```

If port `8765` is already used by another process, stop that process or change the port in both files:

- `server.py`
- `index.html`

### No vehicles are displayed

The public route number can be different from the internal GTFS route ID.

Run:

```bash
python test.py
```

Check the printed route IDs.

If the real route ID is different, update the route filter in `server.py` or `tracker_26.py`.

Example:

```python
ROUTE_ID = "1674"
```

### `ModuleNotFoundError`

Make sure the virtual environment is activated.

Then reinstall dependencies:

```bash
pip install -r requirements.txt
```

### `streamlit: command not found`

Run Streamlit through Python:

```bash
python -m streamlit run tracker_26.py
```

Or reinstall dependencies:

```bash
pip install -r requirements.txt
```

### Browser shows a blank page

Open the browser developer console and check errors.

Possible reasons:

- `server.py` is not running
- `index.html` was opened directly instead of through `python -m http.server`
- Port `8765` is already used
- WebSocket connection failed
- External transport API is unavailable
- GTFS route ID has changed

## Recommended `.gitignore`

```gitignore
venv/
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
.env
.env.local
.idea/
.vscode/
.DS_Store
*.log
```

## Development workflow

Start the backend:

```bash
source venv/bin/activate
python server.py
```

Start the frontend server in another terminal:

```bash
python -m http.server 8000
```

Open:

```text
http://localhost:8000/index.html
```

After changing backend code, restart `server.py`.

After changing frontend code, refresh the browser page.

## Possible improvements

- Add route selector
- Add support for multiple routes
- Add vehicle direction filter
- Add vehicle popup information
- Add last update timestamp
- Add frontend error messages
- Add automatic marker removal for inactive buses
- Add Docker support
- Add `.env` configuration
- Add VPS deployment guide
- Add Nginx reverse proxy configuration
- Add HTTPS/WSS support
- Add logging
- Add tests
- Add mobile-friendly interface

## Recommended GitHub repository description

Real-time Saint Petersburg bus route 26 tracker using Python WebSocket backend, GTFS Realtime data, Leaflet.js and OpenStreetMap.

## Recommended GitHub topics

```text
python
websocket
gtfs
gtfs-realtime
leaflet
openstreetmap
public-transport
bus-tracker
saint-petersburg
streamlit
folium
```

## License

This project is intended for educational and portfolio purposes.
