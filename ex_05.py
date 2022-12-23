#### Secret Word Game ####

# The user have to type letters and the algorithm will check if the letter is in the word or not

# Defining the secret word
secret_word = 'algorithm'

# Creating the dictionaries
word_index = {}
result = {}

# Creating the number of chances
chances = 4

# Fulfilling the dictionairies
i = 0
for v in secret_word:
    word_index[i] = v
    result[i] = '_'
    i += 1

# Defining the header
title = 'Secret Word Game'
welcome = 'Welcome! You need to discover what is the secret word!'

# Printing the header
print('#' * len(welcome))
print(f"##{' ' * int(((len(welcome) - 3 - len(title))/2))}{title}{' ' * int(((len(welcome) - 3 - len(title))/2))}##")
print('#' * len(welcome))
print('\n')
print(welcome)
print('You can try 4 times.')
print('\n')
print('#' * len(welcome))
print('\n')


# This is the list of the words that the user will type
letters = []

# Creating a looping for the game
while True:

    # This variable will be used to check if the user got the word
    result_2 = ''

    # Fulfilling the variable that will be checked
    for k, v in result.items():
        result_2 += v

    # Checking if the result got the word
    if result_2 == secret_word:
        print('#' * len(welcome))
        print('\n')
        print('That is the secret word:  ', result_2)
        print('You got it!!!')
        print('\n')
        break

    # Printing the letters and blank spaces
    print('That is the secret word:  ', result_2)
    print('\n')
    print('#' * len(welcome))
    print('\n')

    # Asking to type a letter
    letter = input('What is the letter? ')

    # Cheking if the user have already typed the letter
    if letter in letters:
        print('You already have typed this letter')

    # Cheking if the letter is present in the secret word
    elif letter.lower() in secret_word:
        letters += letter
        for k, v in result.items():
            for k_2, v_2 in word_index.items():
                if letter == v_2 and k == k_2:
                    result[k] = letter

    else:
        print('We do not have this letter! ')
        chances -= 1
        print(f'You have {chances} now')

    # Cheking the chances
    if chances == 0:
        print('#' * len(welcome))
        print('\n')
        print('Gave Over!')
        print('\n')
        break

########################################### END  #############################################
