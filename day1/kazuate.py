import random

ans=random.randint(1,100)
max_count=5
print('1~100の数字を一つを選んだよ')
print('その数字を',max_count,'回以内にあててね')

for i in range(1,max_count+1):
    print(i,'回目、いくつかな?')
    num=int(input())
    if num==ans:
        print('あたり')
        break
    elif i==max_count:
        pass
    elif num>ans:
        print('もっと下だよ')
    else:
        print('もっと上だよ')
else:
    print('残念～正解は'ans,'でした')
