def main():
    
    side1:float = float(input(" \033[1;3m Enter the length of Side 1 :- \033[0m"))
    side2:float = float(input(" \033[1;3m Enter the length of Side 2 :- \033[0m"))
    side3:float = float(input(" \033[1;3m Enter the length of Side 3 :- \033[0m"))
    perimeter:float= (side1 + side2 + side3)
    
    print(f"The Perimeter of Triangle is {perimeter} ")
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()