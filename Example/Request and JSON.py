# Create a quizzing game. Make HTTP request to Open trivia API at each round of the game to get a new question and
# resent it to the user to answer. At the end of each round ask the user if he wants to play again Keep playing forever
# until the user types 'quit'. Show scoreboard of correct answer and incorrect answer after each round.
import html
import random
import requests
import json

url = 'https://opentdb.com/api.php?amount=10&category=23&difficulty=easy&type=multiple'
endGame = ''
score_correct = 0
score_incorrect = 0

while endGame != 'quit':

    r = requests.get(url)

    if r.status_code != 200:
        endGame = input('Sorry, there was a problem retrieving the question. '
                        'Please try again later or type "quit" to quit.')

    else:
        # Loading question and it's option MCQs
        valid_answer = False
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)
        print('\n' + html.unescape(question) + '\n')  # Question
        for answer in answers:  # Options
            print(str(answer_number) + ') ' + html.unescape(answer))
            answer_number += 1

        # Users input on answer
        while not valid_answer:
            user_answer = input('\nType the number of correct answer: ')
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print('Invalid Answer')
                else:
                    valid_answer = True
            except:
                print('Invalid answer! Use only numbers.')

        # Checking is the user answer is correct or not.
        user_answer = answers[int(user_answer) - 1]
        if user_answer == correct_answer:
            print('\nCongratulations! Your answer ' + html.escape(correct_answer) + ' is correct.')
            score_correct += 1
        else:
            print('\nSorry, ' + html.escape(user_answer) + ' is incorrect, the correct answer is ' +
                  html.escape(correct_answer))
            score_incorrect += 1

        # Scoreboard
        print('\n#############################')
        print('# Your Score is:\t\t\t#')
        print('# Correct answers: ' + str(score_correct) + '\t\t#')
        print('# InCorrect answers: ' + str(score_incorrect) + '\t\t#')
        print('#############################')
        endGame = input('\nPress enter to play again or type "quit" to quit: ').lower()

print('\nThanks for playing!!!')
