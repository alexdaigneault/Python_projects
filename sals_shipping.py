def ground_shipping(weight):
  cost = 0
  flat_charge = 20.00
  if weight <= 2:
    cost += weight * 1.50 + flat_charge
    return cost
  elif weight > 2 and weight <= 6:
    cost += weight * 3.00 + flat_charge
    return cost
  elif weight > 6 and weight <= 10:
    cost += weight * 4.00 + flat_charge
    return cost
  else:
    cost += weight * 4.75 + flat_charge
    return cost

print(ground_shipping(8.4))

premium_ground_shipping = 125.00

def drone_shipping(weight):
  cost = 0
  if weight <= 2:
    cost += weight * 4.50 
    return cost
  elif weight > 2 and weight <= 6:
    cost += weight * 9.00
    return cost
  elif weight > 6 and weight <= 10:
    cost += weight * 12.00 
    return cost
  else:
    cost += weight * 14.25 
    return cost
  
print(drone_shipping(1.5)) 

def cheapest_shipping(weight):
  g = ground_shipping(weight)
  d = drone_shipping(weight) 
  p = premium_ground_shipping 
  if g < d and g < p:
    print("The cheapest method for a package that weight %f pound is: Ground Shipping and it will cost $%f." % (weight, round(g, 2)))
  elif d < g and d < p:
    print("The cheapest method for a package that weight %d pound is: Drone Shipping and it will cost $%d." % (weight, d))
  else:
    print("The cheapest method for a package that weight %f pound is: Premium Ground Shipping and it will cost $%d." % (weight, p))

cheapest_shipping(4.8)
cheapest_shipping(41.5)