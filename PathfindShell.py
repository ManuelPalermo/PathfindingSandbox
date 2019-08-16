import random
from cmd import Cmd
from PathfindEngine import PathfindEngine

'''
To-do List:
	Make terrain spawn with some position logic
'''


class PathfindShell(Cmd):
	intro = 'Welcome to "Pathfinding Sandbox"! Type "help" for a list of available commands.\n->Start by initializing the map with init!'
	prompt = 'PathSandbox> '


	def do_init(self, arg):
		'Create a map with the desired size(x,y)  ex: "map x y'
		try:
			size = arg.split()
			global eng
			if len(size)==0:
				map_size = [50, 35]
				eng = PathfindEngine(map_size)
				eng.initialize()
			else:
				map_size = [int(size[0]), int(size[1])]
				eng = PathfindEngine(map_size)
				eng.initialize()
			print("A map of size ", map_size, " has successfully been created")
		except Exception as e:
			print("Invalid input! Try again.   (", e, ")")


	def do_start(self, arg):
		'Create a start cell on the chosen pos OR create x starts.    ex: start (x1,y1) (x2,y2)  OR  start x'
		try:
			info = arg.split()
			if len(info)==0:      # no info was given
				lpos = [random.choice(eng.valid_away_pos("exit"))]
			elif "(" not in info: # only number of exits to be created was given
				lpos = random.choices(eng.valid_away_pos("exit"), k = int(info[0]))
			else:                 # positions have been given
				lpos = []
				for p in info:
					pos_nums = p.strip("()").split(",")
					pos = [int(n) for n in pos_nums]
					lpos.append(pos)
			eng.create_terrain(lpos, "start")
			print("Starting nodes have been created on positions:\n", lpos)
		except IndexError:
			print("There are no more valid positions available!")
		except Exception as e:
			print("Invalid input! Try again.   (", e,  ")")


	def do_exit(self, arg):
		'Create an exit cell on the chosen pos OR create x exits.    ex: exit (x1,y1) (x2,y2)  OR  exit x'
		try:
			info = arg.split()
			if len(info)==0:      # no info was given
				lpos = [random.choice(eng.valid_away_pos("start"))]
			elif "(" not in info: # only number of exits to be created was given
				lpos = random.choices(eng.valid_away_pos("start"), k = int(info[0]))
			else:                 # positions have been given
				lpos = []
				for p in info:
					pos_nums = p.strip("()").split(",")
					pos = [int(n) for n in pos_nums]
					lpos.append(pos)
			eng.create_terrain(lpos, "exit")
			print("Exits nodes have been created on positions:\n", lpos)
		except IndexError:
			print("There are no more valid positions available!")
		except Exception as e:
			print("Invalid input! Try again.   (", e, ")")

	def do_ground(self, arg):
		'Create a ground cell on the chosen pos OR create x grounds.   ex: ground (x1,y1) (x2,y2)  OR  ground x'
		try:
			info = arg.split()
			if len(info)==0:      # no info was given
				lpos = [random.choice(eng.valid_pos(["exit", "ground", "start"]))]
			elif "(" not in info: # only number of exits to be created was given
				lpos = random.choices(eng.valid_pos(["exit", "ground", "start"]), k = int(info[0]))
			else:                 # positions have been given
				lpos = []
				for p in info:
					pos_nums = p.strip("()").split(",")
					pos = [int(n) for n in pos_nums]
					lpos.append(pos)
			eng.create_terrain(lpos, "ground")
			print("Ground nodes have been created on positions:\n", lpos)
		except IndexError:
			print("There are no more valid positions available!")
		except Exception as e:
			print("Invalid input! Try again.   (", e, ")")

	def do_tree(self, arg):
		'Create a tree cell on the chosen pos OR create x trees.   ex: tree (x1,y1) (x2,y2)  OR  tree x'
		try:
			info = arg.split()
			if len(info)==0:      # no info was given
				lpos = [random.choice(eng.valid_pos(["wall", "exit","start", "tree"]))]
			elif "(" not in info: # only number of exits to be created was given
				lpos = random.choices(eng.valid_pos(["wall", "exit", "start", "tree"]), k = int(info[0]))
			else:                 # positions have been given
				lpos = []
				for p in info:
					pos_nums = p.strip("()").split(",")
					pos = [int(n) for n in pos_nums]
					lpos.append(pos)
			eng.create_terrain(lpos, "tree")
			print("Tree nodes have been created on positions:\n", lpos)
		except IndexError:
			print("There are no more valid positions available!")
		except Exception as e:
			print("Invalid input! Try again.   (", e, ")")

	def do_hill(self, arg):
		'Create a hill cell on the chosen pos OR create x hills.   ex: hill (x1,y1) (x2,y2)  OR  hill x'
		try:
			info = arg.split()
			if len(info)==0:      # no info was given
				lpos = [random.choice(eng.valid_pos(["wall", "exit", "start", "hill"]))]
			elif "(" not in info: # only number of exits to be created was given
				lpos = random.choices(eng.valid_pos(["wall", "exit", "start", "hill"]), k = int(info[0]))
			else:                 # positions have been given
				lpos = []
				for p in info:
					pos_nums = p.strip("()").split(",")
					pos = [int(n) for n in pos_nums]
					lpos.append(pos)
			eng.create_terrain(lpos, "hill")
			print("Hill nodes have been created on positions:\n", lpos)
		except IndexError:
			print("There are no more valid positions available!")
		except Exception as e:
			print("Invalid input! Try again.   (", e, ")")


	def do_water(self, arg):
		'Create a water cell on the chosen pos OR create x water cells.   ex: water (x1,y1) (x2,y2)  OR  water x'
		try:
			info = arg.split()
			if len(info)==0:      # no info was given
				lpos = [random.choice(eng.valid_pos(["wall", "water", "exit", "start"]))]
			elif "(" not in info: # only number of exits to be created was given
				lpos = random.choices(eng.valid_pos(["wall", "water", "exit", "start"]), k = int(info[0]))
			else:                 # positions have been given
				lpos = []
				for p in info:
					pos_nums = p.strip("()").split(",")
					pos = [int(n) for n in pos_nums]
					lpos.append(pos)
			eng.create_terrain(lpos, "water")
			print("Water nodes have been created on positions:\n", lpos)
		except IndexError:
			print("There are no more valid positions available!")
		except Exception as e:
			print("Invalid input! Try again.   (", e, ")")

	def do_wall(self, arg):
		'Create a wall cell on the chosen pos OR create x walls.   ex: wall (x1,y1) (x2,y2)  OR  wall x'
		try:
			info = arg.split()
			if len(info)==0:      # no info was given
				lpos = [random.choice(eng.valid_pos(["wall", "exit", "start"]))]
			elif "(" not in info: # only number of exits to be created was given
				lpos = random.choices(eng.valid_pos(["wall", "exit", "start"]), k = int(info[0]))
			else:                 # positions have been given
				lpos = []
				for p in info:
					pos_nums = p.strip("()").split(",")
					pos = [int(n) for n in pos_nums]
					lpos.append(pos)
			eng.create_terrain(lpos, "wall")
			print("Wall nodes have been created on positions:\n", lpos)
		except IndexError:
			print("There are no more valid positions available!")
		except Exception as e:
			print("Invalid input! Try again.   (", e, ")")


	def do_explore(self, arg):
		'''Explores the map looking for exits using the chosen pathfinding algorithm      ex: explore bfs \n
		Available algorithms are: bfs, dfs, dijkstra, astar
		'''
		try:
			info = arg.split()
			if len(info)==0:      # no info was given
				algorithm = random.choice(["bfs", "dfs", "dijkstra", "astar"]) #"bfs", "dfs", "dijkstra","astar"])
			else:
				algorithm = info[0]
			print("Exploring using '%s' algorithm!" % algorithm)
			path = eng.explore(algorithm)
			print(path)
		except Exception as e:
			print("Invalid input! Try again.   (", e, ")")

	def do_reset(self, arg):
		'Resets the map to a state before exploring'
		try:
			eng.reset_map()
		except Exception as e:
			print("Invalid input! Try again.   (", e, ")")


	def do_map(self, arg):
		'Create a map with some random terrain'
		self.do_init("50 35")
		self.do_start("3")
		self.do_exit("5")
		self.do_tree("200")
		self.do_hill("200")
		self.do_wall("600")
		self.do_water("100")
		#self.do_explore("bfs")

	def do_map2(self, arg):
		'Create a map with only ground'
		self.do_init("50 35")
		self.do_start("2")
		self.do_exit("5")

	def do_test(self, arg):
		'Create a map with some random terrain and explore it using a pathfinding algorithm'
		self.do_map("")
		self.do_explore("")


if __name__ == '__main__':
	sh    = PathfindShell()
	eng   = None
	sh.cmdloop()
