# Q&A GAME

questions = [
    {
        'Question': 'How much is 2 + 2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4'

    },
    {
        'Question': 'How much is 5 * 5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25'
    },
    {
        'Question': 'How much is 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5'
    }
]

points = 0

for question in questions:
    print(question['Question'])

    i = 1
    for o in question['Options']:
        print(f'{i}) {o}')
        i += 1
    tries = input('Choose an option:')

    if tries == question['Answer']:
        points += 1
        print(f'Congrats!!! You got it.\nNow you are with {points} points')

    elif points == 3:
        print('You got all the answers!!!!!!')

    else:
        print(
            f"You did not get it...\nThe right values were {question['Answer']}")

if points < 3:
    print('You was good, but you did not get all...')
