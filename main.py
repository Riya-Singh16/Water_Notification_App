import time
from plyer import notification

notification.notify(
        title = "**Please Drink Water Now!!",
        message = "The National Academics of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
        app_name = "Drink water",
        app_icon = "water icon.ico",
        timeout=2,
    )
time.sleep(2)