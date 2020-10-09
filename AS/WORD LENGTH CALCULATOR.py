def main():

    sentence = raw_input('Enter the sentence:  ')
    SumAccum = 0
    for ch in sentence.split():
        character = len(ch)
        SumAccum = SumAccum + character

    average = (SumAccum) / (len(sentence.split()))
    print(average)

main()