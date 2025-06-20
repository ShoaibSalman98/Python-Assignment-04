def main():
    print("Convert Fahrenheit into Celsius  :)")
    
    fahrenheit= float (input(" \033[1;3m Enter the Tempreture in Fahrenheit:-  \033[0m"))
    celsius = (fahrenheit -32) * 5.0/9.0
    print(f"The temprature in celsius is :- {celsius}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()