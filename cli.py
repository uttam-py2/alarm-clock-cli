import argparse

from manager import AlarmManager
from scheduler import AlarmScheduler


manager = AlarmManager()


def add_alarm(args):
    alarm = manager.add_alarm(
        trigger_time=args.time,
        label=args.label,
        repeat=args.repeat,
    )

    print(
        f"Alarm created with ID {alarm.id}"
    )


def list_alarms(args):
    alarms = manager.list_alarms()

    if not alarms:
        print("No alarms found")
        return

    print(
        f"{'ID':<5}"
        f"{'TIME':<20}"
        f"{'REPEAT':<10}"
        f"{'STATUS':<10}"
        f"LABEL"
    )

    for alarm in alarms:
        print(
            f"{alarm.id:<5}"
            f"{alarm.trigger_time:<20}"
            f"{alarm.repeat:<10}"
            f"{str(alarm.enabled):<10}"
            f"{alarm.label}"
        )


def delete_alarm(args):
    deleted = manager.delete_alarm(
        args.id
    )

    if deleted:
        print("Alarm deleted")
    else:
        print("Alarm not found")


def run_scheduler(args):
    scheduler = AlarmScheduler()
    scheduler.run()


def main():
    parser = argparse.ArgumentParser(
        prog="alarm"
    )

    subparsers = (
        parser.add_subparsers()
    )

    add_parser = (
        subparsers.add_parser("add")
    )

    add_parser.add_argument(
        "--time",
        required=True,
        help="YYYY-MM-DD HH:MM",
    )

    add_parser.add_argument(
        "--label",
        required=True,
    )

    add_parser.add_argument(
        "--repeat",
        default="none",
        choices=[
            "none",
            "daily",
            "hourly",
        ],
    )

    add_parser.set_defaults(
        func=add_alarm
    )

    list_parser = (
        subparsers.add_parser("list")
    )

    list_parser.set_defaults(
        func=list_alarms
    )

    delete_parser = (
        subparsers.add_parser(
            "delete"
        )
    )

    delete_parser.add_argument(
        "id",
        type=int,
    )

    delete_parser.set_defaults(
        func=delete_alarm
    )

    run_parser = (
        subparsers.add_parser("run")
    )

    run_parser.set_defaults(
        func=run_scheduler
    )

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()