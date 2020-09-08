
s = raw_input('Please enter the displacement: ')
u = raw_input('Please enter the Inital velocity: ')
v = raw_input('Please enter the Final Velocity: ')
a = raw_input('Please enter the acceleration: ')
t = raw_input('Please enter the time taken: ')

from collections import deque

stack = deque()

stack.append(s)
stack.append(u)
stack.append(v)
stack.append(a)
stack.append(t)



if v == "":
    answer = float(u) + float(a) * float(t)
    print("final velocity is", answer)


if s == "" and a == "":
    answer = float(0.5 * (float(u) + float(v)) * float(t))
    print("displacement is", answer)

if s == "" and v == "":
    answer = float((float(u) * float(t)) + (0.5 * float(a) * (float(t))**2))
    print("displacement is", answer)

if s == "" and u == "":
    answer = float((float(v) * float(t)) - (0.5 * float(a) * (float(t))**2))
    print("displacement is", answer)

if t == "" and v == "":
    answer = (float(u)**2 + (2 * float(a) * float(s)))
    print("velocity squared is", answer)

