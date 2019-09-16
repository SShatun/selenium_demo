from time import sleep


def wait_for(bool_expression, delay=1, attempts=3):
    for attempt in range(attempts):
        if not bool_expression:
            sleep(delay)
        else:
            return True
    return False
