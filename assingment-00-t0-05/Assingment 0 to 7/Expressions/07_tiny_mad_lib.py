SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    adjective:str= input("\033[1;3m Please type an adjective and press enter \033[0m")
    noun:str= input ("\033[1;3m Please type an noun and press enter \033[0m")
    verb:str= input ("\033[1;3m Please type a verb and press enter \033[0m")
    
    print(SENTENCE_START + adjective + " " +noun +" "+ verb)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()