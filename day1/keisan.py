a=10
b=3

answer=a+b
print(a,'+',b,'=',answer)

answer=a-b
print(a,'-',b,'=',answer)

answer=a*b
print(a,'*',b,'=',answer)

answer=a/b
print(a,'/',b,'=',answer)

answer=a/b
print(a,'//',b,'=',answer)

answer=a/b
print(a,'%',b,'=',answer)

str='Hello'*5
print(str)

x=10
x=x+100
print(x)

x=10
if x>0:
    print('正の数です')
else:
    print('正の数ではありません')
"""
if(x>){
    print systemin("正の数です")
"""
score=64
if score>80:
    print('優')
elif score>60:
    print('良')
elif score>40:
    print('可')
else:
    print('不可')

n=0;
while n<10:
    print(n)
    n=n+1
print('終了')


for i in range(5):
    print(i)

for i in range(1,11):
    print(i,end='')
print()

for i in range(1,4):
    for j in range(1,11):
        print(i*j,end='')
        print()

num=random.randint(5,10)
print(num)

x=10
print(type(x))

name='松田'
age=23
heigh=175.6
print('私の名前は{}で、年齢は{}歳で、身長は{}cmです'.format(name,age,height))

print(f'私の名前は{name}で、年齢は{age}歳で、身長は{height}cmです)
