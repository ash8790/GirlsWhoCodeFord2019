import food
food_data = food.get_reports()
print(len(food_data))
#print(list_of_report[0]["Data"]["Beta Crytoxanthin"]
for food in food_data:
    print(food["Description"])
