# Magic Methods
class Example:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Value is {self.value}"

ex = Example(10)
print(ex)
