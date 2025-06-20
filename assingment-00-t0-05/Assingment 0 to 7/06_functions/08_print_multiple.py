
def print_multiple(message:str, repeat:int):
    for i in range(repeat):
        print(message)



def main():
    message=input("Pleaase type a Message: ")
    repeat=int(input("Enter a number of times to repeat your message:"))
    print_multiple(message , repeat)
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()