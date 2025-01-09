# Basic FizzBuzz Implementation

def FizzBuzz(n):
    # Fizz for multiple of 3
    # Buzz for multiple of 5
    # FizzBuzz for multiple of both

    print(f"Running FizzBuzz for number {n}")

    for i in range(1,int(n)):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def CallFunc(func,arg):
    print(f"Calling function {func}")
    func(arg)
    
def main():
    num = input("Enter a number: ")
    CallFunc(FizzBuzz,num)

if __name__ == "__main__":
    print("Running main function:")
    main()

