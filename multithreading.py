import logging
import threading
import time


def thread(name):
    logging.info(f"thread starting {name}")
    time.sleep(2)
    logging.info(f"thread exiting")


def main():
    format = "%(asctime)s: %(message)s "
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main: before creating thread")
    x = threading.Thread(target=thread, args=(1,), daemon=True)
    logging.info("Before starting thread")
    x.start()
    logging.info("wait for the thread to finish")
    # x.join()
    logging.info("All done")


if __name__ == "__main__":
    main()
    import json

    json.dump(fp="")
