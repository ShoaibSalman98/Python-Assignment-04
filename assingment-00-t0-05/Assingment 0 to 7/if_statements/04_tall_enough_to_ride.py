maximum_height =50

def main():
    height=float(input(" \033[1;3m Enter your height:-  \033[0m"))
    if height >= maximum_height:
     print("You are tall enough to Ride")
    else:
     print("You cant ride try next year")
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
    
    
    
## Second method.    
def main():
    while True:
        # User se height input lena
        height = input("\033[1;3m How tall are you?  \033[0m")

        # Agar user ne khali enter press kiya to program stop ho jaye
        if height == "":
            print("Exiting the program. Have a great day!")
            break

        # Input ko number me convert karna
        height = int(height)

        # Height check karna
        if height >= 50:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")

# Yeh line program ko run karne ke liye zaroori hai
if __name__ == '__main__':
    main()