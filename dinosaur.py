class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.attacks = ('Bite', 'Stomp', 'Charge')
        self.enegery = 500
        self.current_attack = None

    def attack(self, robot):
        attack_names = []
        for attack in self.attacks:
            attack_names.append(attack)
        print()
        user_input = input(f'Choose which attack the {self.name} will use! {attack_names}: ').capitalize()
        print()
        if user_input in attack_names:
            self.current_attack = user_input
        elif user_input not in attack_names:
            print(f'It looks like {self.name} does not have a {user_input}')
            self.current_attack = self.attacks[0]    
            print()
            print(f'Instead he will use a {self.current_attack}!')
            print()
        print(f'{self.name} attacks {robot.name} with a {self.current_attack} for {self.attack_power} and consumed 10 Energy!')
        robot.health -= self.attack_power 
        self.enegery -= 10   
        print()
        print(f'{robot.name} only has {robot.health} health left!')
        print()
        print(f'{self.name} has {self.enegery} Energy left. Use it wisely!')