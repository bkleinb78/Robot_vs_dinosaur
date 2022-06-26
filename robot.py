from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapons = [Weapon('Sword', 30), Weapon('Gun', 40), Weapon('Canon', 50)]
        self.power_level = 500
        self.current_weapon = None

    def attack(self, dinosaur):
        weapon_names = []
        for weapon in self.weapons:
            weapon_names.append(weapon.name)
        user_input = input(f'Choose your weapon to attack! {weapon_names}: ').capitalize()
        for weapon in self.weapons:
            if user_input == weapon.name:
                self.current_weapon = weapon
            else:
                continue    
        if user_input not in weapon_names:
            self.current_weapon = self.weapons[0] 
            print(f'It looks like {self.name} does not have a {user_input} in his Arsenal.')
            print()
            print(f'Instead he will use a {self.weapons[0].name}')   
        print()
        print(f'{self.name} attacks {dinosaur.name} with a {self.current_weapon.name} for {self.current_weapon.attack_power}, and consumed 10 Power!')
        dinosaur.health -= self.current_weapon.attack_power
        self.power_level -= 10
        print()
        print(f'{dinosaur.name} only has {dinosaur.health} health left!')
        print()
        print(f'{self.name} has {self.power_level} Power left, use it wisely!')