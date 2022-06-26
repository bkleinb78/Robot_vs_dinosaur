from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs.append(Dinosaur('T-rex', 50))
        self.dinosaurs.append(Dinosaur('Stego', 40))
        self.dinosaurs.append(Dinosaur('Raptor', 30)) 