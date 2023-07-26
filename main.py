import pygame
import sys
from random import choice

res = width, height = 1000, 600
tile = 50
cols, rows = width // tile, height // tile

pygame.init()
sc = pygame.display.set_mode(res)
clock = pygame.time.Clock()

class cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}
        self.visited = False

    def draw_current_cell(self):
        x,y=self.x*tile,self.y*tile
        pygame.draw.rect(sc,pygame.Color('red'),(x+2,y+2,tile-2,tile-2))
    def draw(self):
        x, y = self.x * tile, self.y * tile
        if self.visited:
            pygame.draw.rect(sc, pygame.Color('black'), (x, y, tile, tile))

        if self.walls['N']:
            pygame.draw.rect(sc, pygame.Color('orange'), (x, y, tile, 2))
        if self.walls['E']:
            pygame.draw.rect(sc, pygame.Color('orange'), (x + tile, y, 2, tile))
        if self.walls['S']:
            pygame.draw.rect(sc, pygame.Color('orange'), (x, y + tile, tile, 2))
        if self.walls['W']:
            pygame.draw.rect(sc, pygame.Color('orange'), (x, y, 2, tile))

    def check_cell(self,x,y):
        find_index= lambda x,y:x+y*cols
        if x<0 or x> cols-1 or y<0 or y>rows-1:
            return False
        return  grid_cells[find_index(x,y)]
    def check_neighbors(self):
        neighbors=[]
        top=self.check_cell(self.x,self.y-1)
        right=self.check_cell(self.x+1,self.y)
        bottom=self.check_cell(self.x,self.y+1)
        left=self.check_cell(self.x-1,self.y)

        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False

def remove_walls(current,next):
    dx=current.x-next.x
    if dx == 1:
        current.walls['W']=False
        next.walls['E']=False
    elif dx == -1:
        current.walls['E']=False
        next.walls['W']=False
        
    dy=current.y-next.y
    if dy == 1:
        current.walls['N']=False
        next.walls['S']=False
    elif dy == -1:
        current.walls['S']=False
        next.walls['N']=False



grid_cells = [cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []

while True:
    sc.fill(pygame.Color('aquamarine1'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    [cell.draw() for cell in grid_cells]
    current_cell.visited=True
    current_cell.draw_current_cell()

    next_cell=current_cell.check_neighbors()
    if next_cell:
        next_cell.visited=True
        stack.append(current_cell)
        remove_walls(current_cell,next_cell)
        current_cell=next_cell
    elif stack:
        current_cell=stack.pop()






    pygame.display.flip()
    clock.tick(30)