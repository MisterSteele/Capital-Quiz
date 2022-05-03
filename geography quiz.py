print('Welcome to my American capital quiz!')

playing = input('Would you like to participate? ')

if playing.lower() != 'yes':
    quit()
if playing.lower() == 'yes':
    print('Okay, lets get started!.')
    print('You can use Google for some help if needed.')
score = 0

answer = input('What is the capital of Florida? ')
if answer.lower() == 'tallahassee':
    print('Correct!')
    score = score + 1
else:
    print('Incorrect')

answer = input('What is the capital of California? ')
if answer.lower() == 'sacramento':
    print('Correct!')
    score = score + 1
else:
    print('Incorrect')

answer = input('What is the capital of Colorado? ')
if answer.lower() == 'denver':
    print('Correct!')
    score = score + 1
else:
    print('Incorrect')

print('You got ' + str(score) + ' question(s) right!')
question = 3
if question == 3:
    print('You did a phenomenal job')
