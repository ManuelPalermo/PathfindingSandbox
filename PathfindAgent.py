import math
import random


class Agent:
	'''
	self.color   = color of the agent(yellow)
	'''
	def __init__(self):
		self.explored = []

	def getNeighbors(self, mapp, pos):
		'Returns the valid neighbors of the current position'
		x   = pos[0]
		y   = pos[1]
		viz = []
		if x > 0                        and mapp.cells[y  ][x-1].type!="wall":  viz.append(mapp.cells[y  ][x-1])
		if x < len(mapp.cells[0])-1     and mapp.cells[y  ][x+1].type!="wall":  viz.append(mapp.cells[y  ][x+1])
		if y > 0                        and mapp.cells[y-1][x  ].type!="wall":  viz.append(mapp.cells[y-1][x  ])
		if y < len(mapp.cells)-1        and mapp.cells[y+1][x  ].type!="wall":  viz.append(mapp.cells[y+1][x  ])
		return viz

	def euclidian_distance(self, posA, posB):
		'Returns the euclidean distance between cellA and cellB'
		xA, yA = posA
		xB, yB = posB
		return math.sqrt((xA-xB)**2 + (yA-yB)**2)

	def explore(self, algorithm, mapp):
		'Explores the map using the chosen pathfinding algorithm and yields the result to the engine to be drawn'
		if algorithm == "bfs":
			for explored in self.bfs(mapp):
				yield explored

		elif algorithm=="dfs":
			for explored in self.dfs(mapp):
				yield explored

		elif algorithm=="dijkstra":
			for explored in self.dijkstra(mapp):
				yield explored

		elif algorithm=="astar":
			for explored in self.astar(mapp):
				yield explored


	def backtrack(self, parent, cell):
		'Backtracks from the exit to the start'
		while parent[cell][0]!=None:
			cell = parent[cell][0]
			cost = parent[cell][1]
			yield "path", cell, cost


	def bfs(self, mapp):
		'Explores the map using breadth-first-search algorithm'
		parent    = {mapp.cells[start_pos[1]][start_pos[0]]:(None, 0) for start_pos in mapp.starts}
		queue     = [mapp.cells[start_pos[1]][start_pos[0]] for start_pos in mapp.starts]
		while queue:
			cell = queue.pop()
			if cell.pos in mapp.exits:
				for result in self.backtrack(parent, cell):
					yield result
				return
			self.explored.append(cell.pos)
			viz = self.getNeighbors(mapp, cell.pos)
			yield "explored", cell
			for vcell in viz:
				if vcell.status=="stray":
					parent[vcell] = (cell, cell.trasnpose_dificulty())
					queue.insert(0,vcell)
					yield "found", vcell


	def dfs(self, mapp):
		'Explores the map using dept-first-search algorithm'
		parent = {mapp.cells[start_pos[1]][start_pos[0]]: (None, 0) for start_pos in mapp.starts}
		queue = [mapp.cells[start_pos[1]][start_pos[0]] for start_pos in mapp.starts]
		while queue:
			cell = queue.pop()
			if cell.pos in mapp.exits:
				for result in self.backtrack(parent, cell):
					yield result
				return
			self.explored.append(cell.pos)
			viz = self.getNeighbors(mapp, cell.pos)
			random.shuffle(viz)
			yield "explored", cell
			for vcell in viz:
				if vcell.status == "stray":
					parent[vcell] = (cell, cell.trasnpose_dificulty())
					queue.append(vcell)
					yield "found", vcell

	def dijkstra(self, mapp):
		'Explores the map using dijkstras algorithm'
		# all nodes are initialized to no parent and inf distance, the start nodes are initialized to (None, 0)
		queue = [cell for row in mapp.cells for cell in row]
		parent = {cell: (None, 0) if cell.pos in mapp.starts else (None, math.inf) for cell in queue}
		distance = {cell: 0 if cell.pos in mapp.starts else math.inf for cell in queue}
		while queue:
			# sorts the queue by distance from start to node
			queue.sort(key=lambda x: distance[x], reverse=True)
			cell = queue.pop()
			if cell.pos in mapp.exits:
				for result in self.backtrack(parent, cell):
					yield result
				return
			self.explored.append(cell.pos)
			yield "explored", cell
			viz = self.getNeighbors(mapp, cell.pos)
			for vcell in viz:
				dis = distance[cell] + vcell.trasnpose_dificulty()
				if dis < distance[vcell]:
					parent[vcell] = (cell, cell.trasnpose_dificulty())
					distance[vcell] = dis
					yield "found", vcell


	def priority_queue(self, mapp, queue, distance):
		'Sorts queue based on a heuristic'
		priority_queue = []
		for cell in queue:
			distances2exits = []
			for exit in mapp.exits:
				dis = self.euclidian_distance(cell.pos, exit)
				distances2exits.append(dis)
			priority = -2*min(distances2exits) - distance[cell]
			priority_queue.append((cell, priority))
		priority_queue.sort(key=lambda x: x[1])
		return [q[0] for q in priority_queue]


	def astar(self, mapp):
		'Explores the map using A* algorithm'
		queue = [cell for row in mapp.cells for cell in row]
		parent = {cell: (None, 0) if cell.pos in mapp.starts else (None, math.inf) for cell in queue}
		distance = {cell: 0 if cell.pos in mapp.starts else math.inf for cell in queue}
		while queue:
			queue = self.priority_queue(mapp, queue, distance)
			cell = queue.pop()
			if cell.pos in mapp.exits:
				for result in self.backtrack(parent, cell):
					yield result
				return
			self.explored.append(cell.pos)
			yield "explored", cell
			viz = self.getNeighbors(mapp, cell.pos)
			for vcell in viz:
				dis = distance[cell] + vcell.trasnpose_dificulty()
				if dis < distance[vcell]:
					parent[vcell] = (cell, cell.trasnpose_dificulty())
					distance[vcell] = dis
					yield "found", vcell