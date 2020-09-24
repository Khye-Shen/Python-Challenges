

Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

word = raw_input("Enter a word:")

wordlist = list(word)

wordvalue = 1

trianglenumber = 0

count = 0

for i in range(len(Alphabet)):

    for j in (wordlist):

      if j == i:

          wordvalue = wordvalue + Alphabet.index(i)

while wordvalue > trianglenumber:

    count =+ 1
    trianglenumber = (0.5*count) * (count+1)


if wordvalue == trianglenumber:
    print("this string is triangular")

else:
    print("string is not triangular")