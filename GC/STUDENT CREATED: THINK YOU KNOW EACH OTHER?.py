# list of questions
p1q = []
p2q = []

# points
p1pts = 0
p2pts = 0

# value for list selection (p2)
p1x = 0
p2x = 0

questionsasked = 0

p1 = raw_input('(Player One) Enter your name: ')
p2 = raw_input('(Player Two) Enter your name: ')
numofq = int(input('How many questions would you like? '))

for i in range(numofq):
    print('Player One')
    p1q.append(raw_input('Enter a question: '))
    p1q.append(raw_input('Enter the answer: '))
for i in range(15):
    print('')

for i in range(numofq):
    print('Player Two')
    p2q.append(raw_input('Enter a question: '))
    p2q.append(raw_input('Enter the answer: '))
for i in range(15):
    print('')

print('All questions have been entered!')

print('Questions for', str(p1) + '!')
for i in range(numofq):
    print(p2q[p2x])
    answer = raw_input('Enter your answer: ')
    if answer == str(p2q[p2x + 1]):
        p1pts += 1
    p2x += 2

print('Questions for', str(p2) + '!')
for i in range(numofq):
    print(p1q[p1x])
    answer = raw_input('Enter your answer: ')
    if answer == str(p1q[p1x + 1]):
        p2pts += 1
    p1x += 2

for i in range(15):
    print('')

print('Game over!')
print(str(p1), 'has', str(p1pts), 'point(s)!')
print(str(p2), 'has', str(p2pts), 'point(s)!')

if max(p1pts, p2pts) < p1pts:
    print(str(p1), 'wins!')
if max(p1pts, p2pts) < p2pts:
    print(str(p2), 'wins!')
if p1pts == p2pts:
    print('Draw!')