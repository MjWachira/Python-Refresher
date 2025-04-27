# Generators
def gen_numbers():
    for i in range(3):
        yield i

for num in gen_numbers():
    print(num)
