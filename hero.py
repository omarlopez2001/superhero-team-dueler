from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
    
    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        total_block = 0
        for armor in self.armors:
            if self.armors == 0:
                print('No armor is equipped')
            else:
                total_block += armor.block()
        return damage_amt - total_block

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        return self.current_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        if len(self.abilities) <= 0 or len(opponent.abilities) <= 0:
            print('Draw')
        else:
            while self.current_health > 0 and opponent.current_health > 0:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())

                if self.is_alive() == False:
                    print(f'{opponent.name} won!')
                    opponent.add_kill += 1
                    self.add_death += 1
                else:
                    print(f'{self.name} won!')
                    self.add_kill += 1
                    opponent.add_death += 1

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())