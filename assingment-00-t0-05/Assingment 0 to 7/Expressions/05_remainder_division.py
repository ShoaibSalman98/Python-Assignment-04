def main():
    dividend:int= int(input("\033[1;3m Please enter an integer to be divided:-\033[0m"))
    divisor:int= int(input("\033[1;3m Please enter an integer to divide by:- \033[0m"))
    
    quotient: int = dividend // divisor
    remainder: int = dividend % divisor
    
    print(f"The result of this division is {quotient} with a remainder of {remainder}") 

# This provided line is required at the end of
# Python file to call the m:-ain() function.
if __name__ == '__main__':
    main()  