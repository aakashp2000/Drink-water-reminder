from plyer import notification
if __name__ == "__main__":
    notification.notify(
        title="Please Drink Water",
        message="Daily fluid intake should be about 15.5 cups or 3.7 liters",
        app_icon=None,
        timeout=5
    )
    time.sleep(60 * 60)
