import time


def main():
    log_limit = 0
    counter = 0
    while True:
        time.sleep(0.5)
        counter += 1
        if counter % 10 == 0:
            print(f"Counter = {counter}")
            log_limit += 1
        if log_limit >= 100:
            print("App works too long ...")
            exit(0)


if __name__ == "__main__":
    main()
