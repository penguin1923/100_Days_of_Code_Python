#dictionary syntax the key and definition are separated by a colon. Different keys are separated by a comma.
#Leave a comma at the end of the code so that you can quickly add another entry.
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",}


#the way to call a value is by grabbing the key
print(programming_dictionary["Bug"])

#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

#create an empty dictionary
empty_dictionary = {}

#wipe a dictionary
# programming_dictionary = {}

#edit and item in a dictionary
# it is the exact same way as adding an item. It will look to see if you have the key and then modify or add to dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through keys in dictionary
for key in programming_dictionary:
    print(key)
#print value of found key in dictionary on new line
    print(programming_dictionary[key])

#nesting dictionary
# {Key:[List],
#  Key2:{Dictionary}}
capitals={"France":"Paris","Germany":"Berlin"}
#nested list
travel_log ={"France":["Paris","Lille","Dijon"],"Germany":["Berlin","Hamburg","Stuttgart"]}    
# dictionary in dictionary
travel_log ={"France":{"Paris":3,"Lille":4,"Dijon":2},"Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"]}} 

#nesting a dictionary in a list
list_name= [{"key":"value"},{"key":"value"}]