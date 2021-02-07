import threading
import time


def animated_loading(process):
    t0 = time.process_time()
    while process.is_alive():
        chars = [".", "..", "...", "....", "....."]
        for char in chars:
            if not process.is_alive():
                break
            print('\r' + 'Processing' + char, end="")
            time.sleep(0.01)
    print("\nTime elapsed:", (time.process_time() - t0))


def init(function):
    loading_process = threading.Thread(target=function)
    loading_process.start()
    animated_loading(loading_process)
    loading_process.join()
