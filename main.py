import random
import pygame
import itertools

class Molecule:
    def __init__(self):
        self.mol = pygame.image.load('mol'+str(random.randint(1,7))+".png")
        self.speed = 5
        self.mol_mask = pygame.mask.from_surface(self.mol)

        self.x = random.randint(1, 18)*50
        self.y = random.randint(1, 18)*50
        self.Kx = random.choice([3 / 5, -3 / 5, 1, -1])
        self.Ky = random.choice([3 / 5, -3 / 5, 1, -1])

    def change(self):
        if self.x <= 0:
            self.Kx = self.Kx * (-1)
        if self.y <= 0:
            self.Ky = self.Ky * (-1)
        if self.x >= 1000 - 50:
            self.Kx = self.Kx * (-1)
        if self.y >= 1000 - 50:
            self.Ky = self.Ky * (-1)
        self.move()
    def move(self):
        self.x += self.speed * self.Kx
        self.y += self.speed * self.Ky
    def show(self, win):
        win.blit(self.mol, (self.x, self.y))

    def get(self):
        return (self.mol_mask, self.x, self.y)

    def connect(self, cor):
        if self.mol_mask.overlap(cor[0], (cor[1] - self.x, cor[2] - self.y)):
            self.expand()
            self.move()
            return True
        else:
            return False
    def expand(self):
        self.x *= -1
        self.y *= -1


main_win = pygame.display.set_mode((1000, 1000))
main_win.fill((255, 255, 255))
flag = True

COUNT = 5
mas_mol = [Molecule() for i in range(COUNT)]
while flag:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
    pygame.display.update()
    main_win.fill((255, 255, 255))

    for mol in mas_mol:
        mol.show(main_win)
        mol.change()
    for par in itertools.combinations(mas_mol, 2):
        if par[0].connect(par[1].get()):
            par[1].expand()
            par[1].move()



