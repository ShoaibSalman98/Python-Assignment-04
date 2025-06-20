def main():
    print("Take input of two Numbers and Add them and Print the Result ")
    
    num1 :str = input ("Enter The First Number  ") 
    num1 = int(num1)
    
    num2:str = input("Enter The Second Number  ")
    num2 = int(num2)
    
    tottal:int = num1 + num2
    
    print(f"The Sum of Two Numbers is  : {tottal}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()