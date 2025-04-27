# Multiprocessing
import multiprocessing

def task():
    print("Process running")

process = multiprocessing.Process(target=task)
process.start()
