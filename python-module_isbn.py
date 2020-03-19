#ISBNから書名、著者、出版時期を取得するモジュール
InputISBN = input()
if len(InputISBN) == 13:
    ISBN_13 = InputISBN
    print(ISBN_13)
elif len(InputISBN) == 10:
    print("WIP")
# WIP 978 を追加して10->13変換するやつ    
    #DigitISBN = len(InputISBN) - 1
    #for i in range(DigitISBN // 2):
    #sum_even = sum(int(InputISBN[2 * i + 1 ]) for i in range(DigitISBN // 2) ) * 3
    #sum_odd = sum(int(InputISBN[2 * i]) for i in range(DigitISBN // 2) )
    #CheckDigit = 10 - (sum_even + sum_odd) % 10 
    #print(CheckDigit)
    #ISBN_13 = "978" + InputISBN + str(CheckDigit)
    #print(ISBN_13)
#WIPここまで    
else:
    print("ERROR: Check your input.")