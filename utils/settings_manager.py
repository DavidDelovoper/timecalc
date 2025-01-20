import json
from utils.path_utils import resource_path


class SettingsManager():
    @staticmethod
    def get_default_settings() -> dict:
        with open(resource_path('default_settings.json'), 'r') as file:
            data = json.load(file)
        return data
    @staticmethod
    def get_settings() -> dict:
        with open(resource_path('settings.json'), 'r') as file:
            data = json.load(file)
        if data == {}:
            data = SettingsManager.get_default_settings()
        return data
    @staticmethod
    def set_settings(settings: dict) -> None:
        with open(resource_path('settings.json'), 'w') as file:
            json.dump(settings, file)