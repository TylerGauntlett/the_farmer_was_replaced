def soil():
	if get_ground_type() != Grounds.Soil:
		till()
		
def grassland():
	if get_ground_type() != Grounds.Grassland:
		till()