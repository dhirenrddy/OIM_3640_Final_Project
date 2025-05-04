import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

def load_events():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def get_events_for_date(date_str):
    for e in load_events():
        if e["date"] == date_str:
            return e 

def get_events_by_club(club_name):
    return [e for e in load_events() if e["club"].lower() == club_name.lower()]

def get_events_by_type(event_type):
    return [e for e in load_events() if e["type"].lower() == event_type.lower()]

def format_events(events):
    if not events:
        return "No events found 🎉"
    msg = "📅 Events:\n"
    for e in events:
        msg += f"• {e['title']} at {e['time']} in {e['location']} ({e['club']}, {e['type']})\n"
    return msg