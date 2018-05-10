import pygame


class PathfindWindow:
	def __init__(self, map_size, cell_size):
		################ Window size #######################
		self.map_size  = map_size   # size of the window (in cells)
		self.csize     = cell_size                                                  # size of each cell (in pixels)
		self.win_size  = (self.map_size[0]*cell_size, self.map_size[1]*cell_size)   # size of the window (in pixels)
		################ Pygame Window #####################
		pygame.init()
		self.window    = pygame.display.set_mode(self.win_size)           # game window using pygame
		pygame.display.set_caption('Pathfinding Sandbox')                 # name of the window


	def update(self):
		'Calls pygame´spiders display.flip(), updating the screen with drawn objects(pygame uses double buffer)'
		pygame.display.flip()

	def display_all(self, mapp):
		'Displays all the cells in the screen (used to initialize the game screen)'
		self.window.fill(((10, 10, 10)))
		line_color = (100, 100, 100)
		for y in range(self.map_size[1]):
			pygame.draw.line(self.window, line_color, [0, y*self.csize],[self.win_size[0], y*self.csize])
			for x in range(self.map_size[0]):
				pygame.draw.line(self.window, line_color, [x*self.csize, 0], [x*self.csize, self.win_size[1]])
				self.display_cell(mapp.cells[y][x])


	def cell_color(self, cell):
		'Determines what color should the cell be'
		if cell.type == "exit":         return (255, 255, 255)
		elif cell.type == "start":      return (255, 0, 0)
		elif cell.type == "wall":       return (32, 32, 32)
		elif cell.status == "found":    return (255, 255, 0)
		elif cell.status == "stray":
			if cell.type == "ground":   return (135, 97, 59)
			elif cell.type == "tree":   return (0, 102, 0)
			elif cell.type == "hill":   return (51, 25, 0)
			elif cell.type == "water":  return (0, 128, 255)
		elif cell.status == "explored":
			if cell.type == "ground":   return (135, 110, 59)
			elif cell.type == "tree":   return (37, 102, 0)
			elif cell.type == "hill":   return (51, 33, 0)
			elif cell.type == "water":  return (0, 200, 255)
		elif cell.status == "path":     return (255, 50, 50)


	def display_cell(self, cell):
		'Displays the cell on the screen'
		color = self.cell_color(cell)
		draw_posx, draw_posy = cell.pos[0] * self.csize, cell.pos[1] * self.csize
		pygame.draw.rect(self.window, color,(draw_posx + 1, draw_posy + 1, self.csize - 1, self.csize - 1))