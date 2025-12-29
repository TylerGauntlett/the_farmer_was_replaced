def handle():
	type = get_entity_type()
	
	measurement = measure()
	if type == Entities.Sunflower and measurement != None and measurement < 7:
		return

	if can_harvest():
		harvest()