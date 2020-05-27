""" FizzBuzz interview problem """

def fizzbuzz(checks, n=100):
    """Output the correct word for each number in [0,n].

    Arguments:
        checks (Dictionary[Number,String]): All the numbers to check against
        n (Number): Amount of numbers to interate through (default: 100)
            must be positive
    """

    # N must be positive
    if (n <= 0):
        print("n must be a positive whole number")
        return

    for i in range(0, n):
        out = ""
        for c in checks.keys():
            if (i % c == 0):
                out += checks[c]
        if (out == ""):
            print(i)
        else:
            print(out)

if (__name__ == '__main__'):
    check_dict = {
        3 : "Fizz",
        5 : "Buzz",
        9 : "Bizz"
    }
    fizzbuzz(check_dict)

