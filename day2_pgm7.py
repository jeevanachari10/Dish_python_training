#Create 2 lists containing fruits and vegetables and 2 tuples containing fruits and vegetables. Combine all fruits as single list and vegetables as single tuple.
#2 list containing fruits and vegetables
fruit_list = ["apple", "kiwi", "Cherry"]
vegetable_list = ["carrot", "potato", "onion"]
print(f"Fruit list: {fruit_list} \nVegetable list: {vegetable_list}")

#2 tuples containing fruits and vegetables
fruit_tuple = ("mango", "banana", "orange")
vegetable_tuple = ("potato", "tomato", "chili")
print(f"Fruit tuple: {fruit_tuple} \nVegetable tuple: {vegetable_tuple}")

#combining the list and tuple
combined_fruit_list = fruit_list + list(fruit_tuple)
combined_vegetable_list = vegetable_list + list(vegetable_tuple)

print(f"Combined fruit list: {combined_fruit_list} \nCombined vegetable list: {combined_vegetable_list}")
