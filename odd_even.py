#入力された整数以下の奇数を返す
InputNumber = int(input())
if InputNumber % 2 == 0: #偶数の場合
    m = InputNumber // 2
else:
    m = InputNumber // 2 + 1
for i in range(m):
    print(2*i + 1)