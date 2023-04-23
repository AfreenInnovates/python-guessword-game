import random

def coding_language_function(): # this loop is entered when the user enters 1 to guess a coding language 
    codelanguage_guesses = 8
    coding_languages = ['java', 'python', 'javascript', 'ruby', 'r', 'julia', 'php', 'pascal', 'c++', 'cobol', 'c#', 'c']
    print("Our random coding word starts with the letter 'j', 'p', 'c' or 'r'. ")
    random_coding_word = random.choice(coding_languages)
    while True:
        print("You have", codelanguage_guesses, "guesses to get the right coding language name!")
        user_code_choice = input("Enter the coding language you guess or enter 'q' to quit the game: ").rstrip().lower()
        if user_code_choice == 'q':
            print("Goodbye!")
            quit()
        elif user_code_choice == random_coding_word:
            print("You got it right!")
            codelanguage_guesses -= 1
            break
        elif user_code_choice not in coding_languages:
            print("This coding language does not belong to the set of languages we have in our mind.")
        elif user_code_choice != random_coding_word:
            codelanguage_guesses -= 1
            if codelanguage_guesses == 0:
                print("You have no more guesses left.")
                break
            elif codelanguage_guesses > 0 and codelanguage_guesses <= 8:
                print("Guess again :)")
    if codelanguage_guesses > 0:
        print("It took you", 8-codelanguage_guesses, "guesses to get the coding language name right.") # this line is printed only if the user played the game (i.e. the guesses are more than 0) if 0 guesses then it does not print it. 
        print("Thank you so much for playing the game!")


def company_names_functions():  # this loop is entered when the user enters 2 to guess a company name  
    company_guesses = 15
    company_names = ['google', 'goldman sachs', 'gucci', 'gap', 'facebook', 'fedex', 'ferrari', 'adidas', 'amazon', 'apple', 'netflix', 'nike', 'nvidia', 'paypal', 'porche', 'prada']
    print("Our random company name starts with the letter 'g', 'f', 'a', 'p' or 'n'.")
    random_company_name = random.choice(company_names)
    while True:
        print("You have", company_guesses, "guesses to get the right company name!")
        user_company_choice = input("Enter the company name you guess or enter 'q' to quit the game: ").rstrip().lower()

        if user_company_choice == 'q':
            print("Goodbye!")
            quit()
        elif user_company_choice == random_company_name:
            print("You got it right!")
            company_guesses -= 1
            break
        elif user_company_choice not in company_names:
            print("This company name does not belong to the set of companies we have in our mind.")
        elif user_company_choice != random_company_name:
            company_guesses -= 1
            if company_guesses == 0:
                print("You have no more guesses left.")
                break
            elif company_guesses > 0 and company_guesses <= 15:
                print("Guess again :)")
    if company_guesses > 0:
        print("It took you", 15 - company_guesses, "guesses to get the company name right.") # this line is printed only if the user played the game (i.e. the guesses are more than 0) if 0 guesses then it does not print it. 
        print("Thank you so much for playing the game!")


def animal_names_function():  # this loop is entered when the user enters 3 to guess an animal 
    animal_guesses = 20
    animals = ['cheetah', 'crocodile', 'crab', 'camel', 'bear', 'buffalo', 'bull', 'dog', 'deer', 'coyote', 'hippopotamus', 'horse', 'hyena', 'lion', 'loepard', 'llma', 'frog', 'fox', 'flamingo']
    print("Our random animal name starts with the letter 'c', 'b', 'd', 'h', 'l', 'h' or 'f'.")
    random_animal_name = random.choice(animals)
    while True:
        print("You have", animal_guesses, "guesses to get the right animal name!")
        user_animal_choice = input("Enter the animal name you guess or enter 'q' to quit the game: ").rstrip().lower()

        if user_animal_choice == 'q':
            print("Goodbye!")
            quit()
        elif user_animal_choice == random_animal_name:
            print("You got it right!")
            animal_guesses -= 1
            break
        elif user_animal_choice not in animals:
            print("This animal name does not belong to the set of animal names we have in our mind.")
        elif user_animal_choice != random_animal_name:
            animal_guesses -= 1
            if animal_guesses == 0:
                print("You have no more guesses left.")
                break
            elif animal_guesses > 0 and animal_guesses <= 20:
                print("Guess again :)")
    if animal_guesses > 0:
        print("It took you", 20 - animal_guesses, "guesses to get the animal name right.") # this line is printed only if the user played the game (i.e. the guesses are more than 0) if 0 guesses then it does not print it. 
        print("Thank you so much for playing the game!") 



def play():
    while True:
        player_choose = input("What type of words would you like to guess?? Enter 1 to guess coding languages, 2 for company names, 3 for animal names, or 'q' to quit the game: ").rstrip().lower()

        if player_choose == 'q':
            print("Goodbye!")
            quit()
        elif player_choose == '1':
            coding_language_function()
        elif player_choose == '2':
            company_names_functions()
        elif player_choose == '3':
            animal_names_function()
        else:
            print("Invalid input. Please enter 1, 2, 3 or 'q'.")

        run_again = input("Enter 'run' to play again or enter any other key to quit the game: ").rstrip().lower()
        if run_again != "run":
            print("Goodbye!")
            quit()
play()
