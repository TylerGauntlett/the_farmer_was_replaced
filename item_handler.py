def fertilize():
	if num_unlocked(Unlocks.Fertilizer) > 0:
		use_item(Items.Fertilizer)
		
def water():
	if get_water() < .1 and num_unlocked(Unlocks.Watering) > 0:
		use_item(Items.Water)