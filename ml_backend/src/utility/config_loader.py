import yaml
from pathlib import Path
from typing import Any, Dict


class ConfigLoader:
    """Loads YAML config files from the config/ directory."""

    def __init__(self):
        self.config_dir = Path(__file__).resolve().parent.parent.parent / "config"

    def load(self, name: str) -> Dict[str, Any]:
        """Load a YAML config file by name (without .yaml extension)."""
        path = self.config_dir / f"{name}.yaml"
        if not path.exists():
            raise FileNotFoundError(f"Config not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}


config = ConfigLoader()
