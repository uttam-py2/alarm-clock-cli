from manager import AlarmManager


def test_add_alarm():
    manager = AlarmManager()

    alarm = manager.add_alarm(
        "2030-01-01 10:00",
        "Test Alarm",
    )

    assert alarm.label == "Test Alarm"


def test_list_alarms():
    manager = AlarmManager()

    alarms = manager.list_alarms()

    assert isinstance(
        alarms,
        list,
    )