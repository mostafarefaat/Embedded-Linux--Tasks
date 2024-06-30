from plyer import notification
import psutil
from time import sleep

while True:
    battery = psutil.sensors_battery()

    percent = int(battery.percent)

    notification.notify(
        title="Battery Percentage",
        message=str(percent)+"% Battery remaining",
        timeout=10
    )
    sleep(60)

  