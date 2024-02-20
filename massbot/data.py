from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from datetime import datetime
from datetime import time


__all__ = ["time"]


MASSTIMES_FILE = "masstimes.csv"


@dataclass
class MassTime:
    name: str
    time: time

    def __str__(self) -> str:
        return f"{self.name} {self.time.strftime('%H:%M')}"


def save_masstimes(masstimes: list[MassTime]) -> None:
    with open(MASSTIMES_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for masstime in masstimes:
            writer.writerow((masstime.name, masstime.time.strftime("%H:%M")))


def append_masstime(masstime: MassTime) -> None:
    with open(MASSTIMES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow((masstime.name, masstime.time.strftime("%H:%M")))


def load_masstimes() -> list[MassTime]:
    if not os.path.exists(MASSTIMES_FILE):
        return []
    with open(MASSTIMES_FILE, newline="") as f:
        reader = csv.reader(f)
        return [
            MassTime(row[0], datetime.strptime(row[1], "%H:%M").time())
            for row in reader
        ]
