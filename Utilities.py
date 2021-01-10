import threading
import time


def animated_loading(process):
    while process.is_alive():
        chars = [".", "..", "...", "....", "....."]
        for char in chars:
            print('\r' + 'Processing' + char, end="")
            time.sleep(0.3)


def init(function):
    loading_process = threading.Thread(target=function)
    loading_process.start()
    animated_loading(loading_process)
    loading_process.join()
