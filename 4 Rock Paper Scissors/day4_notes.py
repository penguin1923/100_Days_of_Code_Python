# import random

# random_integer = random.randint(1,10)
# print(random_integer)

# # doesn't take anything in the parentheses would have to multiply the result to get larger than .99999
# random_float =random.random()*5
# print(random_float)

states_of_america = ["Delaware","Pennsylvania"]
#should be DE
print(states_of_america[0])

#should be PA counting from the end of the list
print(states_of_america[-1])
#also PA counting from the front
print(states_of_america[1])

states_of_america.append("New Jersey")
# now it should be NJ not PA because it counts from the end
print(states_of_america[-1])
#also NJ
print(states_of_america[2])
