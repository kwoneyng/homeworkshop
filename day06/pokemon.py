class Pokemon:

    def __init__(self, name='피카츄'):
        self.name = name
        self.lv = 5
        self.hp = self.lv * 20
        self.exp = 0

    def win(self, x):
        print('이겼다')
        self.exp += x.lv * 15
        if self.exp > 100 :
            print('레벨업!')
            self.lv += 1
            self.exp = 0


    def bark(self):
        return print('pikachu')

    
    def body_attack(self, x):
        if x.hp <= 0 :
            print('이미 죽었어...')
        else :
            x.hp -= self.lv * 5
            if x.hp < 0:
                self.win(x)
        return print(x.hp)
    

    def thousond_volt(self, x):
        if x.hp <= 0 :
            print('이미 죽었어...')
        else :
            x.hp -= self.lv * 7
            if x.hp < 0:
                self.win(x)


    def __repr__(self):
        return self.name

pika = Pokemon()
pika2 = Pokemon()

pika.bark()
pika.body_attack(pika2)
pika.body_attack(pika2)
pika.body_attack(pika2)
pika.body_attack(pika2)
pika.body_attack(pika2)
pika.body_attack(pika2)
