"""
text=input('何を記録しますか>>?')
file=open('diary.txt','a')
file.write(text+'\n')
file.close()
"""
text=input('何を記録する>>')
with open('diary.txt','a') as file:
    file.write(text+'/n')
