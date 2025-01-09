# Basic FizzBuzz Implementation

def fizz_buzz(n):
    """FizzBuzz Implementation

    Args:
        n (int): Number up to which FizzBuzz should be printed.
    """

    print(f"Running FizzBuzz for number {n}")

    for i in range(1, int(n) + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def call_func(func, arg):
    """Calls a function with the given argument.

    Args:
        func (function): The function to call.
        arg (int): The argument to pass to the function.
    """
    print(f"Calling function {func.__name__}")
    func(arg)

def main():
    """Main function to run the FizzBuzz program."""
    num = int(input("Enter a number: "))
    call_func(fizz_buzz, num)

if __name__ == "__main__":
    print("Running main function:")
    main()
