def count_even():
    lst = []  # Initialize an empty list
    
    # Taking input until the user presses Enter
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        if user_input == "":  # Stop if Enter is pressed
            break
        
        try:
            num = int(user_input)  # Convert input to integer
            lst.append(num)  # Add to list
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Count even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    
    # Print the result
    print(f"Number of even numbers: {even_count}")

def main():
    count_even()

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:  # If the current number in the list is even (divisible by 2)
            count += 1  # Add one to our count!

    # Here's another way to do this same thing, with a different kind of for-loop:
    # for i in range(len(lst)):
    #     num = lst[i]
    #     if num % 2 == 0:
    #         count += 1

    print(count)  # Print out how many even numbers we counted above

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Make an empty list to store integers
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
    while user_input != "":  # While the user doesn't enter nothing...
        lst.append(int(user_input))  # Cast the user input into an integer and add it to our list
        user_input = input("Enter an integer or press enter to stop: ")  # Get the next user input

    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()