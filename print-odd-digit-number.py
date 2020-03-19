#入力された文字列の偶数番目の文字を表示する
InputStr = input()
InputNumber = len(InputStr) 
for i in range(InputNumber // 2):
    print(InputStr[2 * i + 1 ])