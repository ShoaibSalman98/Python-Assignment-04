def get_user_info():
    firstName:str= input("Enter Your First Name:-  ").strip().title()
    lastName:str=input("Enter Your last Name:-  ").strip().title()
    emailId:str=input("Enter your Email Address:-  ").strip()
    
    return firstName,lastName,emailId

def main():
    info=get_user_info()
    print(f"Received follwoing data from the user {info}")
    
    
if __name__ == '__main__':
    main()