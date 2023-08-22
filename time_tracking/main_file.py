import time


def main_func():
    try:
        while True:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            print("Current time:", current_time)
            time.sleep(5)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main_func()
