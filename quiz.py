# quiz.py
import random

def user_quiz(states_and_capitals):
    correct_answers = 0
    incorrect_answers = 0
    states = list(states_and_capitals.keys())
    random.shuffle(states)

    for state in states:
        correct_capital = states_and_capitals[state]
        user_answer = input(f'What is the capital of {state}? ').strip()
        if user_answer.lower() == correct_capital.lower():
            print('Correct!')
            correct_answers += 1
        else:
            print(f'Sorry, the correct capital is {correct_capital}.')
            incorrect_answers += 1

        another_question = input('Do you want to answer another question about state capitals? (yes/y / no/n) ')
        if another_question not in ['Yes', 'yes', 'Y', 'y']:
            break

    print('Quiz Summary: ')
    print(f'Correct Answers: {correct_answers}')
    print(f'Incorrect Answers: {incorrect_answers}')