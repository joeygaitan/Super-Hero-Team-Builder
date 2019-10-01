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

    def defend(self,damage_amt = 0):
        sum = 0
        if len(self.armors) == 0:
            print("no armor :(")
        else:
            for armor in self.armors:
                sum += armor.block()
        return sum

    def take_damage(self,damage):
        if self.defend() > damage:
            print("You Blocked the damage with your super powers")
        else:
            print(f"You take {damage} damage, but you blocked {self.defend()} damage: total damage taken {damage - self.defend()}")
            self.current_health -= (damage - self.defend())

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):

        while (opponent.is_alive() == True) and (self.is_alive() == True):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

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
        else:
            print("You killed each other")
            self.deaths += 1
            opponent.deaths += 1
class Team():
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
        while len(copy_other_team_list) > 0 and len(copy_team_list) > 0:

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

class Arena(Team):
    def __init__(self):
        self.team_one = Team("team_one")
        self.team_two = Team("team_two")
    
    def create_ability(self):
        name_input = input("Please type in the name of the ability: ")
        attack_strength_input = input("Please input the attack strength of the ability: ")

        return Ability(name_input, int(attack_strength_input))
    
    def create_weapon(self):
        name_input = input("Please type in the name of the weapon you would like to add: ")
        attack_strength_input = input("Please type in the attack potential attack strength: ")

        return Weapon(name_input, int(attack_strength_input))

    def create_armor(self):
        name_input = input("Please type in the name of the Armor you would like to wear: ")
        max_block_input = input("Please input Max Potential Block for your armor: ")

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
        name_input = input("Please type in the name of the Hero you wish to create: ")
        new_hero = Hero(name_input)
        ability = self.create_ability()
        weapon = self.create_weapon()
        armor = self.create_armor()

        new_hero.add_ability(ability)
        new_hero.add_weapon(weapon)
        new_hero.add_armor(armor)

        return new_hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        #
        # Add the created hero to team one.
        range_input = int(input("Please Input how many heroes you want on Team one: "))
        if range_input <= 0:
            print("Please input a number greater than 0")
            self.build_team_one()
        
        for i in range(range_input):
            team1_hero = self.create_hero() 
            self.team_one.add_hero(team1_hero)
        print("team built")

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.
        range_input = int(input("Please Input how many heroes you want on Team two: "))
        if range_input <= 0:
            print("Please input a number greater than 0")
            self.build_team_one()
        
        for i in range(range_input):
            team1_hero = self.create_hero() 
            self.team_two.add_hero(team1_hero)
        print("team built")

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)

    def show_stats(self):
            '''Prints team statistics to terminal.'''
            # TODO: This method should print out battle statistics
            # including each team's average kill/death ratio.
            # Required Stats:
            #     Declare winning team
            #     Show both teams average kill/death ratio.
            #     Show surviving heroes.
            team_one_kill_sum = {"kills": 0, "count": 0}
            team_one_death_sum = {"deaths":0,"count": 0}

            team_two_kill_sum = {"kills": 0, "count": 0}
            team_two_death_sum = {"deaths":0,"count": 0}
            
            print(f"\nTeam One Stats\n")
            for hero in self.team_one.heroes:
                if hero.is_alive() == True:
                    print(f"{hero.name}Is Alive")
                    team_one_kill_sum["kills"] += hero.kills
                    team_one_death_sum["count"] += 1
                elif hero.is_alive == False:
                    team_one_death_sum["kills"] += hero.deaths
                    team_one_death_sum["count"] += 1
            if team_one_kill_sum["count"] == 0:
                team_one_kill_sum["count"] = 1
            if team_one_death_sum["count"] == 0:
                team_one_death_sum["count"] = 0

            average_one_kills = team_one_kill_sum["kills"] // team_one_kill_sum["count"]
            average_one_deaths = team_one_death_sum["deaths"] // team_one_death_sum["count"]
            if average_one_deaths == 0:
                average_one_deaths = 1
            print(f"Team Two kill death ratio: {average_one_kills / average_one_deaths}")

            print(f"\nTeam Two Stats\n")
            for hero in self.team_one.heroes:
                if hero.is_alive() == True:
                    print(f"{hero.name}Is Alive")
                    team_two_kill_sum["kills"] += hero.kills
                    team_two_death_sum["count"] += 1
                elif hero.is_alive == False:
                    team_two_death_sum["kills"] += hero.deaths
                    team_two_death_sum["count"] += 1

            if team_two_kill_sum["count"] == 0:
                team_two_kill_sum["count"] = 1

            if team_two_death_sum["count"] == 0:
                team_one_death_sum = 1

            average_two_kills = team_two_kill_sum["kills"] // team_two_kill_sum["count"]
            average_two_deaths = team_two_death_sum["deaths"] // team_two_death_sum["count"]
            if average_two_deaths == 0:
                average_two_deaths = 1
            print(f"Team Two kill death ratio: {average_two_kills / average_two_deaths}")
            
            if (team_one_death_sum["count"] == len(self.team_one.heroes)) and (team_two_death_sum["count"] == len(self.team_two.heroes)):
                print("It's A DRAW!!!!!!!!!!!")
            elif team_one_death_sum["count"] == len(self.team_one.heroes):
                print("The winner Is Team two")
            elif team_two_death_sum["count"] == len(self.team_two.heroes):
                print("Team one Wins")


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "y":
        #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
        #Check for Player Input
        elif play_again.lower() == "n":
            game_is_running = False
            