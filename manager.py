from storage import AlarmStorage
from models import Alarm


class AlarmManager:
    def __init__(self):
        self.storage = AlarmStorage()

    def add_alarm(
        self,
        trigger_time,
        label,
        repeat="none",
    ):
        alarms = self.storage.load()

        next_id = (
            max([alarm.id for alarm in alarms], default=0) + 1
        )

        alarm = Alarm(
            id=next_id,
            trigger_time=trigger_time,
            label=label,
            repeat=repeat,
        )

        alarms.append(alarm)

        self.storage.save(alarms)

        return alarm

    def list_alarms(self):
        return self.storage.load()

    def delete_alarm(self, alarm_id):
        alarms = self.storage.load()

        updated = [
            alarm
            for alarm in alarms
            if alarm.id != alarm_id
        ]

        self.storage.save(updated)

        return len(updated) != len(alarms)

    def update_alarm(self, alarm):
        alarms = self.storage.load()

        for index, existing in enumerate(alarms):
            if existing.id == alarm.id:
                alarms[index] = alarm
                break

        self.storage.save(alarms)