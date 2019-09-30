import copy
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

class Arena:
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two
    
    def create_ability(self):
        name_input = input("Please type in the name of the ability")
        attack_strength_input = input("Please input the attack strength of the ability")

        return Ability(name_input, int(attack_strength_input))
    
    def create_weapon(self):
        name_input = input("Please type in the name of the weapon you would like to add")
        attack_strength_input = input("Please type in the attack potential attack strength")

        return Weapon(name_input, int(attack_strength_input))

    def create_armor(self):
        name_input = input("Please type in the name of the weapon you would like to add")
        max_block_input = input("Please input Max Potential Block for your armor")

        return Armor(name_input, int(max_block_input))
    
    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        name_input = input("Please type in the name of the Hero you wish to create")
        self.create_ability()
        self.create_weapon()
        self.create_armor()

        return Hero(name_input)



class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def attack(self, other_team):
        if len(other_team.heroes) == 0 or len(self.heroes) == 0:
            if len(other_team.heroes) == 0:
                return "There isn't any heroes in the opposing team"
            elif self.heroes == 0:
                return "There isn't any heroes in the team"
        #Copies of both teams
        copy_team_list = copy.copy(self.heroes)
        copy_other_team_list = copy.copy(other_team.heroes)
        
        #while loop to find a winner or tag.
        bothAlive = True
        while bothAlive:
            # break case for while loop that checks if one or both the teams == 0
            if len(copy_other_team_list) <= 0 or len(copy_team_list) <= 0:
                bothAlive = False
            else:
                #two random Heros
                random_hero = random.choice(copy_team_list)
                other_random_hero = random.choice(copy_other_team_list)
                
                random_hero.fight(other_random_hero)
                print("Fighting")
                if random_hero.is_alive() == False:
                    print(f"{other_random_hero} defeated {random_hero}")
                    copy_team_list.remove(random_hero)
                elif other_random_hero.is_alive() == False:
                    print(f"{random_hero} defeated {other_random_hero}")
                    copy_other_team_list.remove(other_random_hero)

        if len(copy_other_team_list) == 0 and len(copy_team_list) == 0:
            print("This is a draw!")
        elif len(copy_other_team_list) == 0 and len(copy_team_list) != 0:
            print("Other Team, Wins!")
        elif len(copy_other_team_list) != 0 and len(copy_team_list) == 0:
            print("Team Wins!")

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health
        print("health restored")

    def stats(self):
        for hero in self.heroes:
            print(f"{hero.name}: {hero.kills // hero.deaths}")

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                print(f"You removed {name} hero")
                print(hero.name, name)
                self.heroes.remove(hero)
        print("The hero isn't in here")
        return 0

    def view_all_heroes(self):
        print("Your Heroes are\n")
        if len(self.heroes) == 0:
            print("There isn't any heros in this team. Add some heroes")
        else: 
            for hero in self.heroes:
                print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)
        print(f"You added {hero} to your team")

class Hero():
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.deaths = 0
        self.kills = 0

    def add_armor(self, armor):
        # It's passed an object of armor
        self.armors.append(armor)
    
    def add_weapon(self, weapon):
        # This adds a weapon to the self.abilities list
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        # TODO: This method should add the number of kills to self.kills
        self.kills += 1

    def add_death(self, num_deaths):
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths -= 1 

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
        # These are variables that will later be used to add up the attacks of both opponents 
        attack_self_sum = 0
        attack_opponent_sum = 0

        # This adds up all the attacks for both opponents
        for ability in opponent.abilities:
            attack_self_sum += ability.attack_strength
        for ability in self.abilities:
            attack_opponent_sum += ability.attack_strength

        # This minuses the health for both opponents 
        self.current_health -= attack_self_sum
        opponent.current_health -= attack_opponent_sum

        if (self.is_alive() == True) and (opponent.is_alive() == True):
            print("The battle rages on")
        elif (self.is_alive() == False) and (opponent.is_alive() == True):
            opponent.kills += 1
            print(f"kills: {self.kills}")
            self.deaths += 1
            print(f"{opponent.is_alive()} won")
        elif (self.is_alive() == True) and (opponent.is_alive() == False):
            self.kills += 1
            print(f"kills: {opponent.kills}")
            opponent.deaths += 1
            print(f"{self.name} won")
                
        

    

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

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 10000)
    # ability2 = Ability("Super Eyes", 1000000)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    team_one = Team("One")
    jodie = Hero("Jodie Foster")
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = Team("Two")
    athena = Hero("Athena")
    socks = Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)

    team_one.attack(team_two)