class Hero:
    name='松田'
    hp=100
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def sleep(self,hours):
        print('{}は{}時間寝た',format(self.name,hours))
        self.hp +=hours

print("start")
h=Hero()
h.sleep(3)
print('{}のHPは現在{}です'.format(h.name,h.hp))

scores1=[80,40,50]
scores2=[80,40,50]

print('scores1のidentity:{}'.format(id(scores1)));
print('scores2のidentity:{}'.format(id(scores2)));

name=list()
print('前:{}'.format(id(name)))
name.append('松田')
print('後:{}'.format(id(names)))
name=
print('前:{}'.format(id(name)))
name=name+'さん'
print('後:{}'.format(id(name)))
