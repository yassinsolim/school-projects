# awards.py
# ENDG 233 F21
# Yassin Soliman
# A terminal-based program for analyzing movie awards data.
# You must include the code listed below. You may add your own additional functions, variables, etc. 
# You may not import any modules.
# You may only use built-in functions that directly support strings, lists, dictionaries, sets, and tuples.
# Remember to include docstrings for your functions and comments throughout your code.
#


# ******************************************************************************************************
# Data is imported from the included awards_data.py file. Both files must remain in the same directory.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
from awards_data import SAG, oscars, NBR, ISA, GLAAD, NAACP
award_list_names = ['sag', 'oscars', 'nbr', 'isa', 'glaad', 'naacp']
award_list_options = [SAG, oscars, NBR, ISA, GLAAD, NAACP]
# ******************************************************************************************************



# ******************************************************************************************************
# DEFINE FUNCTIONS HERE
def lower_list(list_name):
    for i in range(len(list_name)):
        list_name[i] = list_name[i].lower()
    return list_name


def count_awards(movie_title):
    number_of_awards = 0
    for i in range(len(award_list_options)):
        award = award_list_options[i]
        award = lower_list(award)
        if movie_title in award:
            for x in range(len(award)):
                if movie_title == award[x]:
                    number_of_awards += 1
    return number_of_awards

def print_award_winners(awards):
    if awards not in award_list_names:
        print("Awards list not found.")
    for i in range(len(award_list_options)):
        if awards == award_list_names[i]:
            print("\n".join(award_list_options[i]))



# ******************************************************************************************************
print("ENDG 233 Awards Data Program")

# DEFINE MAIN CODE BELOW
# Choice variable that takes integer input from user
choice = int(input("\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: "))

# While True loop for the choice so that program runs continuously until the user chooses to end
while choice != 0:
# If statment for choice #1 which will take a string input of the movie title
    if choice == 1:
        movie_title = input("Please enter the movie title you would like to search: ")
        movie_title = movie_title.lower() # Makes all of the characters lowercase
        movie_title = movie_title.strip() # Removes any trailing/leading whitespace in string
        print("--Number of Awards Won--") # Prints the number of awards won by the movie
        print(count_awards(movie_title)) # Prints the number of awards won by the movie

# If statment for choice #1 which will take a string input of the movie title
    elif choice == 2:
        awards = input("\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n")
        awards = awards.lower() # Makes all of the characters lowercase
        awards = awards.strip() # Removes any trailing/leading whitespace in string
        print("--Requested Award Winners--") # Prints the movies that have won that award
        print_award_winners(awards) # Prints the movies that have won that award

    else:
        print("You must select either 1, 2, or 0.")
    choice = int(input("\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: "))

print("Thank you for using the awards data program.")


# You may find the following strings helpful for the interface design:
# "\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: "
# "Please enter the movie title you would like to search: "
# "\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n"
# "Awards list not found."
# "You must select either 1, 2, or 0."
# "Thank you for using the awards data program."
# "--Number of Awards Won--"
# "--Requested Award Winners--"
