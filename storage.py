import json
import os

from models import Alarm


class AlarmStorage:
    def __init__(self, file_path="alarms.json"):
        self.file_path = file_path

    def load(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as file:
            data = json.load(file)

        return [Alarm(**item) for item in data]

    def save(self, alarms):
        with open(self.file_path, "w") as file:
            json.dump(
                [alarm.to_dict() for alarm in alarms],
                file,
                indent=4,
            )