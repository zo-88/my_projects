#weight tracker
import math



print("please enter weight in KG")
current_weight = float(input("What is your weight? "))
goal_weight = float(input("What is in your goal weight?"))



# calculate weight needed to lose to reach goal weight function
def weight_goal(current, goal):
    
    lose_kg = round(current - goal,2)
    print(f"You need to lose {lose_kg} Kg")
    yes = input("Would you like to estimate your weight lost? ").lower()
    if yes[0] == 'y':
        user_amount = float(input("How much would you like to lose daily? Please enter in Kg: "))
        print(f"You want to lose {user_amount}Kg per day")
        
        days = math.ceil(lose_kg/user_amount)
      
        print(f"It will take around {days} days to lose {lose_kg}")
    else:
        print("ok, remember no snacking! Good luck!")
    print("Note must have yesterday's weight to compare to do the following:")
    should_continue = input("Would you like to measure you daily weight lost Y/N? ").lower()
    if should_continue == 'y':
        yesterday_weight = float(input("Enter yesterday's weight: "))
        daily_lost = round(yesterday_weight -current_weight,2)
        print(f"Your daily lost is {daily_lost}")
        actual_time = math.ceil(lose_kg/daily_lost)
        print(f"Based on your daily lost it should take {actual_time} days to lose {lose_kg}")
        
    else:
        print("ok bye")

      
    
    
#Function weight_goal called

    
weight_goal(current = current_weight, goal = goal_weight)



                         
                         

