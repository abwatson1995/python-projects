number_of_quizzes = 5

quiz_score_1 = int(input('Enter score of quiz 1: '))
quiz_score_2 = int(input('Enter score of quiz 2: '))
quiz_score_3 = int(input('Enter score of quiz 3: '))
quiz_score_4 = int(input('Enter score of quiz 4: '))
quiz_score_5 = int(input('Enter score of quiz 5: '))

print(f"\nYour quiz average is {(quiz_score_1+quiz_score_2+quiz_score_3+quiz_score_4+quiz_score_5)/number_of_quizzes}")
