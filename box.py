# made by V¡ktor
# 2022-09-06
# thanks for using box.py <3

import os
import datetime
import random
from string import ascii_letters, digits

import pytz


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def gray(*args, type=1) -> str:
    """gray text"""
    return f"\033[{type};30m" + " ".join(str(obj) for obj in args) + "\033[0m"


def red(*args, type=1) -> str:
    """red text"""
    return f"\033[{type};31m" + " ".join(str(obj) for obj in args) + "\033[0m"


def green(*args, type=1) -> str:
    """green text"""
    return f"\033[{type};32m" + " ".join(str(obj) for obj in args) + "\033[0m"


def yellow(*args, type=1) -> str:
    """yellow text"""
    return f"\033[{type};33m" + " ".join(str(obj) for obj in args) + "\033[0m"


def blue(*args, type=1) -> str:
    """blue text"""
    return f"\033[{type};34m" + " ".join(str(obj) for obj in args) + "\033[0m"


def magneta(*args, type=1) -> str:
    """magneta text"""
    return f"\033[{type};35m" + " ".join(str(obj) for obj in args) + "\033[0m"


def cyan(*args, type=1) -> str:
    """cyan text"""
    return f"\033[{type};36m" + " ".join(str(obj) for obj in args) + "\033[0m"


def tzFilter(hour: int = 23, gmt: int = None) -> int:
    # Examples:
    # >>> tzFilter(hour=18)
    # -5
    # >>> tzFilter(gmt=5)
    # -300
    zones = ('Etc/GMT' + (f'+{i}' if i > 0 else str(i)) for i in range(-12, 12))
    for _ in (['Etc/GMT' + (f'+{gmt}' if gmt > 0 else str(gmt))] if isinstance(gmt, int) else zones):
        zone = datetime.datetime.now(pytz.timezone(_))
        if not gmt and int(zone.strftime('%H')) != hour:
            continue
        return int(zone.strftime('%Z').replace('GMT', '00')) * 60


def randomCode(length=15, chars=None) -> str:
    # Example:
    # >>> randomCode(length=8, chars="aeiou12345")
    # '552ei4o4'
    return "".join(random.choice(
        list(chars) if chars else list(
            string.ascii_letters + string.digits + "!@#$%&")
        ) for _ in range(length)
    )
