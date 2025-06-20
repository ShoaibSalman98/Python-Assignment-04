# def main():
#     num1=int(input("Enter a first number :-  "))
#     num2=int(input("Enter a second number :-  "))
#     average= (num1+num2) / 2
#     print(average)


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
    
def average(a: float, b: float):
    """
    Returns the number which is half way between a and b
    """
    sum = a + b
    return sum / 2

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)
    

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    
    
    
    
def find_average(num1, num2):
    return (num1 + num2) / 2

def main():
    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculating and displaying the average
    average = find_average(num1, num2)
    print(f"The average of {num1} and {num2} is: {average}")

if __name__ == '__main__':
    main()