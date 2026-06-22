import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class TranslationSettings:
    translation_memory: bool
    terminology: bool
    workflow: str

class LocaleFlow:
    def __init__(self):
        self.settings = None

    def configure_translation_settings(self, translation_memory: bool, terminology: bool, workflow: str) -> TranslationSettings:
        self.settings = TranslationSettings(translation_memory, terminology, workflow)
        return self.settings

    def save_settings(self) -> Dict:
        if self.settings is None:
            raise ValueError("Settings not configured")
        return self.settings.__dict__

    def validate_settings(self, settings: Dict) -> bool:
        required_keys = ["translation_memory", "terminology", "workflow"]
        for key in required_keys:
            if key not in settings:
                return False
        return True
