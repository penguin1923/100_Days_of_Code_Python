'''Functions'''
#defining... def
def my_function():
    print("This is a function")
    print("Goodbye")

#This calls the function
my_function()

#These are from Reborgs World - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
def hurdle_3():
    def turn_right():
        turn_left()
        turn_left()
        turn_left()

    def hurdle():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
    while at_goal() == False:
        if wall_in_front():
            hurdle()
        else:
            move()


def hurdle_4():
    def turn_right():
    turn_left()
    turn_left()
    turn_left()

    def hurdle():    
        turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()
        
    while not at_goal():
        if wall_in_front():
            hurdle()
        else:
            move()        