spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

peper_emoji = "🌶"

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print("{} ({}) | Heat Level: {}".format(food["name"], food["cuisine"], peper_emoji * food["heat_level"]))
    
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:    
            print("{} ({}) | Heat Level: {}".format(food["name"], food["cuisine"], peper_emoji * food["heat_level"]))
    

def get_average_heat_level(spicy_foods):
    total = 0
    count = 0

    for food in spicy_foods:
        total += food["heat_level"]
        count += 1
    average = total / count
    return average

print("{:.0f}".format(get_average_heat_level(spicy_foods)))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
