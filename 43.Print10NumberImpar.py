count = 0


def to_infinity():
    index = 0
    while True:
        yield index
        index += 1
for x in to_infinity():
    if x % 2 != 0:
        print(x)
        count += 1
        if count == 10:
            break
