def handle():
	type = get_entity_type()
	
	if type == Entities.Sunflower and measure() != None and measure() < 7:
		return

	if can_harvest():
		harvest()