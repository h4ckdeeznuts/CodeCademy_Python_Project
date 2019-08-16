premium_cost = 125.00
def ground_shipping(weight):
  if weight <= 2:
    return 1.50*weight+20
  elif weight > 2 and weight <= 6:
    return 3.00*weight+20
  elif weight > 6 and weight <= 10:
    return 4.00*weight+20
  else:
    return 4.75*weight+20

print(ground_shipping(8.4))

def drone_shipping(weight):
  if weight <= 2:
    return 4.50*weight
  elif weight > 2 and weight <= 6:
    return 9.00*weight
  elif weight > 6 and weight <= 10:
    return 12.00*weight
  else:
    return 14.25*weight


def cheap_ship(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_cost:
   print("For "+str(weight)+" lbs, The cost for ground shipping is "+str(ground_shipping(weight))+" and is the cheapest! ")
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_cost:
   print("For "+str(weight)+" lbs, The cost for drone shipping is "+str(drone_shipping(weight))+" and is the cheapest! ")
  else:
    print("Premium shipping of $125 is the cheapest option.")
# For testing-
print(cheap_ship(30.8)) 
print(cheap_ship(4.8))
