def substract_seven(num):
    return num-7

def main():
    enterNumber:int= int(input("Enter your Number:-  "))
    
    final=substract_seven(enterNumber)
    print(f"{enterNumber} minus 7 is {final}")
    
    
if __name__ == '__main__':
    main()