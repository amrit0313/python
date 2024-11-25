def add(*args):
    # print(args)
    # print(args[0])
    addition = 0
    for n in args:
        addition +=n
        # print(n)
    return addition


print(add(2, 3, 4, 5, 9))



def calculate(n, **kwargs):
    print(kwargs)
    # for key, values in kwargs.items():
    #     print(key, values)
    # print(kwargs["multiply"])
    n*=kwargs["multiply"]
    n/=kwargs["divide"]

    print(n)


calculate(4, multiply = 4,  divide = 3)
