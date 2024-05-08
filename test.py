"""This module holds th function to test the functionalty of this project
"""
def clock_test import DigitalClock
from utime import sleep
def clock_test() -> None:
    clock = DigitalClock()
    while True:
        sleep(1)
        pass