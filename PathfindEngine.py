import math
from copy import deepcopy
from PathfindWindow import PathfindWindow, pygame
from PathfindMap import Map
from PathfindAgent import Agent


class PathfindEngine:
	'''
	self.size      = size of the map in cells [x, y]
	self.cell_size = size of each cell in the map (square cells)
	self.map       = map where cells and things are stored
	self.agents    = agents which move on the map
	self.graphWin  = graphical window where objects are displayed
	'''
	def __init__(self, size):
		self.size      = size
		self.cell_size = int(min(568/self.size[1], 1266/self.size[0]))
		self.map       = Map()
		self.agent     = Agent()
		self.window    = PathfindWindow(self.size, self.cell_size)
		self.time      = pygame.time.Clock()


	def initialize(self):
		'Initializes the map and agents and creates the graphical window'
		self.map.initialize(self.size)
		self.window.display_all(self.map)
		self.window.update()


	def create_terrain(self, pos, terrain):
		'Creates the desired terrain on the chosen positions'
		for p in pos:
			self.map.create_terrain_type(p, terrain)
			self.window.display_cell(self.map.cells[p[1]][p[0]])
		self.window.update()


	def valid_away_pos(self, away_type):
		'Returns list of positions away from the away_type'
		far_pos = []
		if  away_type=="start": dis_sensitivity = math.log(len(self.map.starts)+1.8, 1.8)
		elif away_type=="exit": dis_sensitivity = math.log(len(self.map.exits)+1.8, 1.8)
		radius = max(len(self.map.cells[0]), len(self.map.cells)) / dis_sensitivity
		for y, row in enumerate(self.map.cells):
			for cell in row:
				if cell.type not in ["wall", "water", "exit", "start"]:
					distances = [math.inf]
					if away_type=="start":
						for start_pos in self.map.starts:
							distances.append(math.sqrt((start_pos[0] - cell.pos[0]) ** 2 + (start_pos[1] - cell.pos[1]) ** 2))
					elif away_type == "exit":
						for exit_pos in self.map.exits:
							distances.append(math.sqrt((exit_pos[0] - cell.pos[0]) ** 2 + (exit_pos[1] - cell.pos[1]) ** 2))
					if min(distances) > radius:
						far_pos.append(deepcopy(cell.pos))
		return far_pos


	def valid_pos(self, invalid_cell_type):
		'Returns a list with all the valid positions on the map(without walls)'
		valid = []
		for y, row in enumerate(self.map.cells):
			for cell in row:
				if cell.type not in invalid_cell_type:
					valid.append(deepcopy(cell.pos))
		return valid


	def explore(self, algorithm):
		'Makes the choosen agent explore the map in search for an exit using the selected algorithm'
		path = []
		cost = 0
		cells_explored = 0
		for explored_cell in self.agent.explore(algorithm, self.map):
			type2draw = explored_cell[0]
			cell2draw = explored_cell[1]
			#print("explored on eng:", explored_cell.pos)
			if type2draw=="explored":
				cell2draw.status = "explored"
				cells_explored+=1
			elif type2draw=="found":
				cell2draw.status = "found"
			elif type2draw == "path":
				cell2draw.status = "path"
				path.append(cell2draw)
				cost +=  explored_cell[2]
			self.window.display_cell(cell2draw)
			self.window.update()
			self.time.tick(240)
		if path: return "A path to exit has been found(cost = %s | explored_cells = %s) :\n %s" % (cost, cells_explored, [cell.pos for cell in reversed(path)])
		else: return "No path to exit has been found!"

	def reset_map(self):
		'Resets all cells to stray, reseting the map to a not explored state'
		for y, row in enumerate(self.map.cells):
			for cell in row:
				cell.status = "stray"
				self.window.display_cell(cell)
		self.window.update()











