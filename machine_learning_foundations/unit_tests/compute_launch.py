def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    interval = launch_day - current_day
    if (interval < 0 ):
        return 0
    else:
        return interval
