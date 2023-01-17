print('hello')
today_weight = float(input("what is your weight today? \n please enter in kg: "))
yesterday_weight = float(input("What was your weight yesterday?\n please enter in kg: "))

per_day = round(today_weight -yesterday_weight,2)

print(f"Your daily weight lost speed is {per_day}Kg")

should_calculate = input("Would you like to calculate how many days it would take you to lose this weight based on current speed? y/n: ")


if should_calculate == 'y':
    goal_weight = float(input("what is your goal weight?"))
    kg_to_lose = round(today_weight - goal_weight,2)
    print(f"This is your goal weight {goal_weight}Kg")
    print(f"You need to lose {kg_to_lose}Kg to reach your {goal_weight}Kg")

else:
    print("ok then bye")






