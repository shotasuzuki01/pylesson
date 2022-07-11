scores=[80,20,75,60]
count=0
for data in scores:
    if data>=60:
        print('合格')
    else:
        print('不合格')
div='合格' if data>=60 else '不合格'
print(div)

ages=[28,50,8,20,78,25,22,25,22,10,27,33]
num=5
samples=list()
for age in ages:
    if 20<=age<30:
        samples.append(age)
        if len(samples)==num:
            break
print(samples)

ages=[28,50,'ひみつ',8,20,78,25,22,25,22,10,27,'無回答',33]
samples=list()
for data in ages:
    #if not isinstance(data,int):
    if not type(data)is int:
        continue
    if data<20 or data>=30:
        continue
        samples.append(data)
print(samples)

