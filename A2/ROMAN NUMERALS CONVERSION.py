
def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1

def printDecimal(roman):
    mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dec = last = 0
    for i in range(0, len(roman)):
        no = mapping.get(roman[i])
        dec = dec + (no - 2 * last) if no > last else dec + no
        last = no
    print(dec)

choice = input("Convert to Roman or Decimal?")

if choice.lower() == "roman":
    roman = int(input("Enter a number:"))
    print("Roman numeral is:", end = " ")
    printRoman(roman)

elif choice.lower() == "decimal":
    number = input("Enter a Roman number:")
    print("Decimal number is:", end = " ")
    printDecimal(number)

else:
    print("Error!")