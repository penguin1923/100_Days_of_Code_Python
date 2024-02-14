################### Scope ####################

enemies = 1

def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")
# enemies inside function: 2
increase_enemies()
print(f"enemies outside function: {enemies}")
# enemies outside function: 1

#Global Constants 

#All Caps
PI =3.14
