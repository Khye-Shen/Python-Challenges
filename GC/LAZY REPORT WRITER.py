import random

students = int(input('How many students do you have? '))

comments = ["Listens and follows directions well", "Expresses ideas clearly", "Does neat, thorough work", "Seeks information independently", "Completes activities in a timely manner", "Occupies his/her time constructively", "Communicates well with students and teacher", "Works well in group settings and makes many contributions to the group", "Follows directions well and is self-sufficient within the classroom", "s extremely motivated and always puts his/her best effort into classroom assignments", "Has demonstrated very good progress this year", "Has matured nicely this year, both academically and socially", "Is learning how to be a better listener and takes direction well", "Is becoming more self-reliant during independent work periods", "Is learning to be cooperative when working in groups", "Work habits have shown improvement"]

for i in range(students):
    name = input('Enter name of student: ')
    print(name + random.choice(comments))

