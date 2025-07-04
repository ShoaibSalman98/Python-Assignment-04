import math  # Import the math library so we can use the sqrt function

def main():
    # Get the two side lengths from the user and cast them to be numbers
    ab: float = float(input(" \033[1;3m Enter the length of AB: \033[0m"))
    ac: float = float(input("\033[1;3m Enter the length of AC: \033[0m"))

    # Calculate the hypotenuse using the two sides and print it out
    bc: float = math.sqrt(ab**2 + ac**2)
    print(f"The length of BC (the hypotenuse) is: {bc}")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()