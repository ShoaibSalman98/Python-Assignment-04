def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    
    
    
    
def print_divisors(num):
    # Loop from 1 to num (inclusive) to find divisors
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')  # Print each divisor on the same line
    print()  # Print a newline after all divisors

def main():
    # Get user input
    num = int(input("Enter a number: "))
    print(f"Here are the divisors of {num}")
    print_divisors(num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()