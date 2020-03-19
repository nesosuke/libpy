#ISBNから書名、著者、出版時期を取得するモジュール
InputISBN = input()
if len(InputISBN) == 13:
    ISBN_13 = InputISBN
    print(ISBN_13)
elif len(InputISBN) == 10:
    CheckDigit = 10 - sum(int(i) for i in InputISBN) % 10 
    ISBN_13 = "978" + InputISBN + str(CheckDigit)
    print(ISBN_13)
else:
    print("Error: Check your input.")
