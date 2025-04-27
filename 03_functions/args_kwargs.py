# *args and **kwargs
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(1, 2, 3, a=4, b=5)
