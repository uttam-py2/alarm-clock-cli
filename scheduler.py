import time

from datetime import datetime, timedelta

from manager import AlarmManager


class AlarmScheduler:
    def __init__(self):
        self.manager = AlarmManager()

    def _calculate_next_time(
        self,
        alarm_time,
        repeat,
    ):
        if repeat == "daily":
            return alarm_time + timedelta(days=1)

        if repeat == "hourly":
            return alarm_time + timedelta(hours=1)

        return None

    def run(self):
        print("Alarm scheduler started...")

        while True:
            alarms = self.manager.list_alarms()

            now = datetime.now()

            for alarm in alarms:
                if not alarm.enabled:
                    continue

                alarm_dt = datetime.strptime(
                    alarm.trigger_time,
                    "%Y-%m-%d %H:%M"
                )

                if now >= alarm_dt:
                    print("\n")
                    print("=" * 40)
                    print("⏰ ALARM")
                    print(f"Label: {alarm.label}")
                    print(
                        f"Time: {alarm.trigger_time}"
                    )
                    print("=" * 40)
                    print("\a")

                    if alarm.repeat == "none":
                        alarm.enabled = False
                    else:
                        next_alarm = (
                            self._calculate_next_time(
                                alarm_dt,
                                alarm.repeat,
                            )
                        )

                        alarm.trigger_time = (
                            next_alarm.strftime(
                                "%Y-%m-%d %H:%M"
                            )
                        )

                    self.manager.update_alarm(alarm)

            time.sleep(1)