classmate_favorite_foods = {'Lasagna', 'Sushi', 'Pizza', 'Pasta', 'Salad'}

user_favorite_foods = set()  

user_favorite_foods.add(input("Enter your first favorite food: "))
user_favorite_foods.add(input("Enter your second favorite food: "))
user_favorite_foods.add(input("Enter your third favorite food (press Enter to skip): ") or None)

user_favorite_foods.discard(None)

common_foods = classmate_favorite_foods.intersection(user_favorite_foods)

if common_foods:
    print(f"Our common favorite food(s): {', '.join(common_foods)}")
else:
    print("We have no common favorite foods.")