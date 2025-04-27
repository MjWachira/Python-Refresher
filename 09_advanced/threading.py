# Threading
import threading

def task():
    print("Thread running")

thread = threading.Thread(target=task)
thread.start()
