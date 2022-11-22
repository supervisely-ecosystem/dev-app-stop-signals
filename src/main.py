import time
import signal
import sys


def signal_sigint_handler(sig, frame):
    print("You pressed Ctrl+C!")
    # sys.exit(0)


# no way to handle this
# def signal_sigkill_handler(sig, frame):
#     print("You pressed SIGKILL!")
#     # sys.exit(0)


def signal_sigterm_handler(sig, frame):
    print("You pressed SIGTERM!")
    # sys.exit(0)


def signal_sigusr1_handler(sig, frame):
    print("You pressed SIGUSR1!")


def signal_sigusr2_handler(sig, frame):
    print("You pressed SIGUSR2!")


signal.signal(signal.SIGINT, signal_sigint_handler)
# signal.signal(signal.SIGKILL, signal_sigkill_handler)
signal.signal(signal.SIGTERM, signal_sigterm_handler)
signal.signal(signal.SIGUSR1, signal_sigusr1_handler)
signal.signal(signal.SIGUSR2, signal_sigusr2_handler)


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
