import random

class Ability():
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
    def attack(self):
        return random.randint(0,self.attack_strength)

class Armor():
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        return random.randint(0,self.max_block)

class Weapon(Ability):
    def attack(self):
        if self.attack_strength == 0:
            print(f"You missed")
        else:
            return random.randint(self.attack_strength//2, self.attack_strength)

class Team():
    def __init__(self, team_name,):
        self.team_name = team_name
        

class Hero():
    def __init__(self,name,starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        pass
    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        sum = 0
        for ability in self.abilities:
            sum += ability.attack()
        return sum
    def add_armor(self,armor):
        self.armors.append(armor)
    def defend(self,damage_amt = 0):
        sum = 0
        if len(self.armors) == 0:
            print("no armor :(")
        else:
            for armor in self.armors:
                sum += armor.block()
        return sum - damage_amt
    def take_damage(self,damage):
        if self.defend() == damage:
            print("You Blocked the damage with your super powers")
        else:
            print(f"You take {damage} damage, but you blocked {self.defend()} damage: total damage taken {damage - self.defend()}")
            self.current_health -= damage - self.defend()
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True
    def fight(self, opponent):
        if self.is_alive() == True:
            for ability in opponent.abilities:
                self.current_health -= ability.attack_strength
            if self.is_alive() == False:
                print(f"{self.name} won")
            else:
                print("The battle rages on")
        else:
            print("you already dead bro")

    

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())

    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)

    # ability = Ability("Great Debugging", 50)
    # anotherAbility= Ability("Super Speed", 20)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(anotherAbility)
    # print(hero.abilities)

    # If you run this file from the terminal
    # this block of code is executed.

    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())

    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)

    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 10000)
    ability2 = Ability("Super Eyes", 1000000)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)