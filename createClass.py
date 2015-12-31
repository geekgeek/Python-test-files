# Classes
#shows how to use classes and objects in Python 2.7
#https://www.youtube.com/watch?v=POQIIKb1BZA

class Enemy:
    life = 3
    #self = using something in the class
    def attack(self):
        print("outch")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("i am dead")
        else:
            print(str(self.life) + "life left")

#create object
enemy1 = Enemy()

enemy1.attack()
enemy1.checkLife()
