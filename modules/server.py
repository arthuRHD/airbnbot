from time import sleep

from modules.config import TIME_INTERVAL
from modules.sms import send_sms


def listen_for_update(robot, dest, message):
    sleep(TIME_INTERVAL)
    send_sms(robot, dest, message)            