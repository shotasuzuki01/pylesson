number=int(input('数値を入力>>'))
if number%2==0:
    print('ぐうすうです')
else:
    print('きすうです')

div='偶数' if number%2==0 else'奇数'
print(div)

result='優' if number>=80 else'良' if number>=60 else'可' if number>=40 else'不可'
