import math


class Cell:
	'''
	self.pos      = position of the cell in the map
	self.type     = type of cell (start, exit, hill, water, tree, ground, wall)
	self.status   = status of the cell (stray, found, explored, path)
	'''
	def __init__(self, pos, typee):
		self.pos      = pos
		self.type     = typee
		self.status   = "stray"


	def trasnpose_dificulty(self):
		'Determines how dificult it is to move on the cell'
		if self.type == "ground":   return 1
		elif self.type == "tree":   return 3
		elif self.type == "hill":   return 5
		elif self.type == "water":  return 10
		elif self.type == "wall":   return math.inf
		elif self.type == "exit":   return 0
		elif self.type == "start":  return 0


	def info(self):
		'Prints cell info to console'
		print(self.pos)
		print(self.type)
		print(self.status)
		print(self.trasnpose_dificulty())


class Map:
	'''
    self.cells  = 2D array with all the cell objects
    self.starts = starting cell positions of each agent
    self.exits  = exit cells positions
    '''
	def __init__(self):
		self.cells   = []
		self.starts  = []
		self.exits   = []

	def initialize(self, size):
		'Initializes the map with all cells as ground'
		for y in range(size[1]):
			l = []
			for x in range(size[0]):
				l.append(Cell([x, y], "ground"))
			self.cells.append(l)

	def create_terrain_type(self, pos, typee):
		'Creates the terrain on the desired position'
		if typee=="start":
			self.starts.append(pos)
			self.cells[pos[1]][pos[0]].type = "start"
			self.cells[pos[1]][pos[0]].status = "path"
		elif typee=="exit":
			self.exits.append(pos)
		self.cells[pos[1]][pos[0]].type = typee