"""Fibonacci Number Generator."""

def main():
    """Takes in user input, returns Fibonacci Numbers."""
    
    numTerms = input("Enter number of Fibonnaci Terms: ")
    isNum = numTerms.isnumeric()

    if(isNum):
        numTerms = int(numTerms)
        if(numTerms <= 0):
            print("Invalid input. Input must be an integer greater than zero.")
        else:
            a,b = 1,1
            for i in range(0, numTerms):
                print(a)
                a,b = b,a+b
    else:
        print("Invalid input. Input must be an integer greater than zero.")

main()
