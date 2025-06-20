ADULT_AGE : int = 18 # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False
    
########## No need to edit code beyond this point :) ##########

def main():
    age : str = int(input("How old is this person?: "))
    print(is_adult(age))
    

if __name__ == "__main__":
    main()
    
    
# 2nd Methode    
ADULT_AGE = 18  

def is_adult(age):
    """Returns True if the age is 18 or older, otherwise returns False."""
    return age >= ADULT_AGE  

def main():
    # Ask the user for their age
    age = int(input("How old is this person?: "))
    
    # Call is_adult() function and print the result
    print(is_adult(age))

# Required line to run the program
if __name__ == '__main__':
    main()    