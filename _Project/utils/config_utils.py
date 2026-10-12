# config_utils.py
import json
from pathlib import Path

CONFIG_FILE = Path.home() / ".music_player_app" / "config.json"

def load_config():
    """Load configuration from the config file."""
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    if not CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "x") as f:
                pass  # File created successfully
        except FileExistsError:
            pass  # File already exists (race condition)
        
        save_config({
            "last_playlist": None,
            "volume": 0.5,
            "auto_play": True,
            "show_tray_icon": True
        })

def save_config(config):
    """Save configuration to the config file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

if (__name__ == "__main__"):
    load_config()