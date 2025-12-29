import world_handler
import harvest_handler
import ground_handler
import item_handler

def grass():
	ground_handler.grassland()
	plant(Entities.Grass)
	item_handler.water()

def carrot():
	ground_handler.soil()
	plant(Entities.Carrot)
	item_handler.fertilize()
	item_handler.water()

def bush():
	ground_handler.grassland()
	plant(Entities.Bush)
	
def tree():
	ground_handler.grassland()
	plant(Entities.Tree)
	item_handler.water()
		
def pumpkin():
	ground_handler.soil()
	plant(Entities.Pumpkin)
	item_handler.water()
	
def sunflower():
	ground_handler.soil()
	plant(Entities.Sunflower)
	item_handler.water()
	
def cactus():
	ground_handler.soil()
	plant(Entities.Cactus)
	item_handler.water()

def hedge():
	ground_handler.grassland()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, 2)
	harvest()
	
def handle():
	handlers = {
		Entities.Grass: grass,
		Entities.Carrot: carrot,
		Entities.Bush: bush,
		Entities.Tree: tree,
		Entities.Pumpkin: pumpkin,
		Entities.Sunflower: sunflower,
		Entities.Cactus: cactus,
		Entities.Hedge: hedge,
	}
	
	expected_type = world_handler.expected_entity_type()
	
	plant_handler = handlers[expected_type]
	
	plant_handler()