
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    second:int= DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    print(f"There are {second } seconds in a year!")
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()