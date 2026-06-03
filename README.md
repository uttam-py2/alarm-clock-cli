# Alarm Clock CLI

A simple command-line Alarm Clock application built with Python.

The application allows users to create, list, delete, and execute alarms from the command line. Alarm data is persisted locally using a JSON file, and the system supports one-time as well as recurring alarms.

---

## Features

- Create alarms
- List alarms
- Delete alarms
- Persistent storage using JSON
- Enable/disable alarms
- Alarm scheduler that continuously monitors alarms
- Daily and hourly repeating alarms
- Terminal notification and bell sound icon when an alarm triggers

---

## Project Structure

```text
alarm-clock-cli/
│
├── cli.py
├── models.py
├── storage.py
├── manager.py
├── scheduler.py
│
├── alarms.json
│
├── tests/
│   └── test_manager.py
│
├── requirements.txt
└── README.md
```

### Responsibilities

| File | Responsibility |
|--------|---------------|
| models.py | Alarm domain model |
| storage.py | JSON persistence layer |
| manager.py | Business logic for alarms |
| scheduler.py | Alarm execution and scheduling |
| cli.py | Command-line interface |

---

## Design Decisions

### Why a CLI?

The assignment explicitly requested a command-line application without a web interface. A CLI keeps the solution focused on the core alarm functionality.

### Why JSON instead of a Database?

The requirements explicitly excluded databases.

Using a JSON file:

- Keeps the solution lightweight
- Avoids unnecessary complexity
- Provides persistence across application restarts

### Why a Separate Storage Layer?

Separating storage from business logic makes the application easier to test and maintain.

Instead of having file operations scattered throughout the codebase:

```text
CLI
  ↓
Manager
  ↓
Storage
  ↓
JSON File
```

### Why Dataclasses?

Python dataclasses provide:

- Type hints
- Automatic constructors
- Readable object representation
- Simple serialization support

This makes the Alarm model easy to work with while keeping the code concise.

---

## Alarm Data Model

```python
@dataclass
class Alarm:
    id: int
    trigger_time: str
    label: str
    repeat: str = "none"
    enabled: bool = True
```

Example stored alarm:

```json
{
  "id": 1,
  "trigger_time": "2026-06-03 18:00",
  "label": "Team Meeting",
  "repeat": "daily",
  "enabled": true
}
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd alarm-clock-cli
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Create Alarm

```bash
python cli.py add \
  --time "2026-06-03 18:00" \
  --label "Team Meeting"
```

### Create Repeating Alarm

```bash
python cli.py add \
  --time "2026-06-03 18:00" \
  --label "Daily Standup" \
  --repeat daily
```

Supported repeat values:

- none
- daily
- hourly

---

### List Alarms

```bash
python cli.py list
```

Example output:

```text
ID   TIME                 REPEAT     STATUS     LABEL
1    2026-06-03 18:00     daily      True       Daily Standup
```

---

### Delete Alarm

```bash
python cli.py delete 1
```

---

### Start Alarm Scheduler

```bash
python cli.py run
```

When an alarm triggers:

```text
========================================
⏰ ALARM
Label: Daily Standup
Time: 2026-06-03 18:00
========================================
```

---

## Running Tests

Run all tests:

```bash
pytest
```

---

## Assumptions

- Alarm times are supplied in `YYYY-MM-DD HH:MM` format.
- The scheduler checks alarms every second.
- Timezone support is out of scope.
- Alarm persistence is local to the machine.
- Multiple alarms can exist for the same time.

---

## AI-Assisted Development

AI tools were used during:

- Requirement refinement
- Architecture brainstorming
- Edge case identification
- Test planning
- Code review

All generated suggestions were manually reviewed, validated, and adapted before implementation.

The focus was on using AI as an engineering assistant rather than blindly accepting generated code.

---

## Future Improvements

Potential enhancements if this were developed further:

- Timezone support
- Relative time input (`in 10m`, `in 2h`)
- Snooze functionality
- Rich terminal UI
- Desktop notifications
- Cron-style recurring schedules
- Improved test coverage
- Structured logging

---

## Trade-offs

This implementation prioritizes:

- Simplicity
- Readability
- Maintainability
- Separation of concerns
