

def print_the_value_of_i(i: int) -> None:
    print(i)


fs = []

for i in range(5):
    fs.append(lambda: print_the_value_of_i(i))

for f in fs:
    f()
