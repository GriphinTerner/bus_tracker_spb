# Bus 26 Live Tracker

Bus 26 Live Tracker is a Streamlit web application for tracking bus route 26 in Saint Petersburg.

The project receives public transport data, processes bus positions in Python, and displays them on an interactive map using Streamlit and Folium.

## Stack

- Python
- Streamlit
- Folium
- streamlit-folium
- requests
- urllib3
- GTFS Realtime

## Features

- Bus route 26 tracking
- Interactive map
- Streamlit web interface
- Folium map rendering
- GTFS Realtime vehicle position parsing
- Lightweight project structure
- Simple local launch

## Project structure

```text
tracker_26.py
requirements.txt
README.md
```

## Requirements

- Python 3.10+
- pip
- virtualenv
- Internet connection

## How to run

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

Run the Streamlit app:

```bash
streamlit run tracker_26.py
```

If the `streamlit` command is not available, run:

```bash
python -m streamlit run tracker_26.py
```

After launch, Streamlit will print a local URL in the terminal.

Usually it is:

```text
http://localhost:8501
```

Open this URL in your browser.

## Files description

### `tracker_26.py`

Main application file.

It loads transport data, processes bus coordinates, creates an interactive Folium map, and displays it inside the Streamlit interface.

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

### `streamlit: command not found`

Run Streamlit through Python:

```bash
python -m streamlit run tracker_26.py
```

Or reinstall dependencies:

```bash
pip install -r requirements.txt
```

### `ModuleNotFoundError`

Make sure the virtual environment is activated.

Then reinstall dependencies:

```bash
pip install -r requirements.txt
```

### The app opens, but buses are not displayed

Possible reasons:

- External transport API is unavailable
- Internet connection is unstable
- Route ID has changed
- No active buses are currently available in the feed

Restart the app:

```bash
streamlit run tracker_26.py
```

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

## License

This project is intended for educational and portfolio purposes.
