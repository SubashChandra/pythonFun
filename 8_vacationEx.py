
def hotel_cost(nights):
	return nights*140

def plane_ride_cost(city):
	if city=="Charlotte":
		return 183
	elif city=="Tampa":
		return 220
	elif city=="Pittsburgh":
		return 222
	elif city=="Los Angeles":
		return 475

def rental_car_cost(days):
	cost=days*40
	if days >=7:
		cost=cost-50
	elif days>=3:
		cost=cost-20
	return cost

def trip_cost(city,days):
	return hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)

print trip_cost("Los Angeles",2)
