import harvest_handler
import plant_handler

G = Entities.Grass
C = Entities.Carrot
S = Entities.Sunflower
B = Entities.Bush
T = Entities.Tree
P = Entities.Pumpkin
X = Entities.Cactus
H = Entities.Hedge

world_map = [
	[G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],
	[G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],
	[G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],
	[C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
	[C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
	[C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
	[S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S],
	[S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S],
	[S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S],
	[T, B, T, B, T, B, T, B, T, B, T, B, S, S, S, S, S, S, S, S, S, S],
	[B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T],
	[T, B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T, B],
	[B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T, B, T],
	[X, X, X, X, X, X, X, H, H, H, H, H, H, H, P, P, P, P, P, P, P, P],
	[X, X, X, X, X, X, X, H, H, H, H, H, H, H, P, P, P, P, P, P, P, P],
	[X, X, X, X, X, X, X, H, H, H, H, H, H, H, P, P, P, P, P, P, P, P],
	[X, X, X, X, X, X, X, H, H, H, H, H, H, H, P, P, P, P, P, P, P, P],
	[X, X, X, X, X, X, X, H, H, H, H, H, H, H, P, P, P, P, P, P, P, P],
	[H, H, H, H, H, H, H, H, H, H, H, H, H, H, P, P, P, P, P, P, P, P],
	[H, H, H, H, H, H, H, H, H, H, H, H, H, H, P, P, P, P, P, P, P, P],
	[H, H, H, H, H, H, H, H, H, H, H, H, H, H, P, P, P, P, P, P, P, P],
	[H, H, H, H, H, H, H, H, H, H, H, H, H, H, P, P, P, P, P, P, P, P],
]

def expected_entity_type():
	x = get_pos_x()
	y = get_pos_y()
	
	if 0 <= y < len(world_map) and 0 <= x < len(world_map[0]):
		return world_map[::-1][y][x]
		
	return H

def handle():
	size = get_world_size()

	for i in range(size):
		for y in range(size):
			harvest_handler.handle()
				
			plant_handler.handle()
					
			move(North)
				
		move(East)

def move_drone(target):
	x = get_pos_x()
	y = get_pos_y()

	while (x != target):
		if not can_move(East):
			harvest()
		else:
			move(East)
			x = get_pos_x()
			
	while (y != 0):
		if not can_move(North):
			harvest()
		else:
			move(North)
			y = get_pos_y()

def setup_drone_spawns():
	count = max_drones()
	increments = get_world_size() // count

	for i in range(count):
		target = increments * (i + 1)
		
		def drone_task():
			move_drone(target)
			while True:
				handle()
		
		spawn_drone(drone_task)

def setup():
	# move primary drone
	move_drone(0)

	# move and start spawns
	setup_drone_spawns()