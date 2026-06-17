# SPb Bus Tracker

SPb Bus Tracker is a prototype web application for tracking public transport in Saint Petersburg in real time.

The project receives live transport data, extracts vehicle coordinates and displays buses on a map.

## Stack

- Python
- WebSocket
- GTFS Realtime / live transport data
- HTML
- JavaScript
- Map visualization

## Features

- Receive live public transport data
- Filter vehicles by route
- Extract bus coordinates and timestamps
- Display buses on a map
- Auto-update vehicle positions
- Send live coordinates through a WebSocket server
- Work with transport API data

## Project structure

```text
server.py
tracker_26.py
tracker_26_live.html
index.html
requirements.txt
README.md
```

## Requirements

- Python 3.10+
- pip
- virtualenv

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

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python server.py
```

If you want to run the tracker script directly:

```bash
python tracker_26.py
```

After launch, open the local address printed in the terminal.

If the project runs a local web server, open:

```text
http://localhost:8000
```

or:

```text
http://127.0.0.1:8000
```

## Screenshots

Screenshots can be added to the `screenshots/` folder.

```text
screenshots/
  map.png
  tracker.png
```

Example:

```markdown
![Live map](screenshots/map.png)
```

## Status

The project is a working prototype for real-time public transport tracking and map visualization.
