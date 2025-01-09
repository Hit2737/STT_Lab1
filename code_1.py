"""
FizzBuzz Program
This script implements the FizzBuzz problem, where numbers from 1 to n are
printed with the following rules:
- Print "Fizz" for numbers divisible by 3.
- Print "Buzz" for numbers divisible by 5.
- Print "FizzBuzz" for numbers divisible by both 3 and 5.
- Print the number itself if none of the above conditions are met.

Functions:
    fizz_buzz(n): Implements the FizzBuzz logic.
    call_func(func, arg): Calls a given function with the provided argument.
    main(): The main entry point of the program.
"""

def fizz_buzz(n):
    """FizzBuzz Implementation

    Args:
        n (int): Number up to which FizzBuzz should be printed.
    """
    print(f"Running FizzBuzz for number {n}")

    for i in range(1, n + 1):
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
    try:
        num = int(input("Enter a number: "))
        call_func(fizz_buzz, num)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    print("Running main function:")
    main()
