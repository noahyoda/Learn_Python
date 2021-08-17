name = input("What's your name: ")
print("hi " + name)

data = input("Num to square: ")


def sqr(num):
    print(num * num)


sqr(int(data))


def sqr2(num):
    return num * num


print(sqr2(int(data)))
