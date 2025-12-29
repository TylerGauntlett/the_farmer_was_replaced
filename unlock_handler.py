

def auto_unlock():
	for unlockable in Unlocks:
		costs = get_cost(unlockable)
		
		if len(costs) == 0:
			continue
				
		can_unlock = True
		
		required_items = []

		for item in Items:
			if item in costs:
				required_items.append(item)

		for item in required_items:
			cost = costs[item]

			if num_items(item) < cost:
				can_unlock = False
				break
			
		if can_unlock:
			unlock(unlockable)