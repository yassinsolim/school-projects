# spotify_program.py
# STUDENT NAME, ENDG 233 F23
# A terminal-based application to process and plot data based on given user input and provided data values.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.
#

import numpy as np
import matplotlib.pyplot as plt

# ******************************************************************************************************
# Data is imported from the included csv file. You may not modify the content, order, or location of the csv file.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
column_names = ['title', 'artist(s)', 'release', 'num_of_streams', 'bpm', 'key', 'mode', 'danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness']
data = np.genfromtxt('spotify_data.csv', delimiter = ',', skip_header = True, dtype = str)
# ******************************************************************************************************


# ******************************************************************************************************
# DEFINE BONUS CLASS HERE (optional)


# ******************************************************************************************************
# DEFINE FUNCTIONS HERE

def feature_stats(input_value):
    pass    # Delete and complete the function

def age_stats(input_value):
    pass    # Delete and complete the function


# ******************************************************************************************************
# DEFINE MAIN CODE
# Add your code within the main function. A docstring is not required for this function.

# You may find the following hints helpful:
# A list comprehension can be used to convert data values in a column and create a new array
# e.g. converted_data = np.array([row[column_value] for row in data], dtype='float')
# NumPy has many built-in functions/methods, including those for finding the index location of a value (e.g. argmax(), argmin(), etc.)
# Refer to the NumPy and Matplotlib documentation for more


def main():
    print("ENDG 233 Spotify Statistics\n")
    print("Song analysis options: ")
    for menu, option in enumerate(column_names):
         print(menu, option)
    print("Choose -1 to end the program.")

    # Continue main code below


    # Create and print danceability vs. bpm plot


    # Create bonus Song object (optional)
    # Create and print bonus plot (optional)



if __name__ == '__main__':
    main()

