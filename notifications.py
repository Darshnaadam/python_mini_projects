from plyer import notification
import time

if __name__ == '__main__':
        while True:
            notification.notify(
                title = "Reminder", # Title of the notification
                message = "Time to take a break!", # Message to be displayed on the notification
                app_icon = "D:/python_mini_projects/bell.ico",
                timeout=5
            )
            time.sleep(15)