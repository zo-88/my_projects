#weight tracker
import math


# calculate weight needed to lose to reach goal weight function
def weight_goal(current, goal):
    
    lose_kg = round(current - goal,2)
    print(f"You need to lose {lose_kg} Kg")
    yes = input("Would you like to estimate your weight lost? ").lower()
    if yes[0] == 'y':
        user_amount = float(input("How much would you like to lose daily? Please enter in Kg: "))
        print(f"You want to lose {user_amount}Kg per day")
        
        days = math.ceil(lose_kg/user_amount)
        
        #i = 0
        #days = 0
        #while i < lose_kg:
            #days += 1
            #i += user_amount
        print(f"It will take around {days} days to lose {lose_kg}")
    else:
        print("ok, remember no snacking! Good luck!")
        keep_tracking = False
        



    
    
keep_tracking = True

while keep_tracking:
    print("please enter weight in KG")
    current_weight = float(input("What is your weight? "))
    goal_weight = float(input("What is in your goal weight?"))
    weight_goal(current = current_weight, goal = goal_weight)
    continue_tracking = input('Do you want to calculate again?').lower()
    if continue_tracking == 'n':
        print("Okay Good Luck!")
        keep_tracking = False
    
    
    



                         
                         
