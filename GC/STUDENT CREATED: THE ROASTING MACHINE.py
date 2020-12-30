import random

name = raw_input('Whats your name? ')
list = [str(name)+',I just wanted to say that you are free to disagree with me, I cant force you to be right.', str(name)+', to your advantage, light travels faster than sound. This is why people like you seem bright before you speak.','If I wanted to kill myself, I would climb up to your ego and jump down to your IQ.','I miss the old you, back when I didnt know you.','You are definitive proof that human evolution can go backwards']

print(random.choice(list))