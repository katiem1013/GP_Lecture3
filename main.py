# activity 6


# activity 5
import random
tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant",
        6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice",
        12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star",
        18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

fortune = {"past": "", "present": "", "future": ""}

for key in fortune.keys():
    remaining_cards = list(tarot.keys())
    choice = remaining_cards[random.randint(0, len(remaining_cards)-1)]
    fortune[key] = tarot.pop(choice)

for k, val in fortune.items():
        print("Your ", k, " is the ", val, " card.")

# activity 4
available_items = {"health potion": 10, "cake": 5, "green elixir": 20, "lombas bread": 25, "bogweed": 15, "rabbit stew": 30}
health_points = 20

health_points += available_items.pop("cake", 0)  # pop takes it from the dictionary and returns it
print(health_points)

# activity 3
animals_on_campus = {}
print(animals_on_campus)

animals_on_campus["Foxes"] = 8
animals_on_campus["Birds"] = 12
animals_on_campus["Aligators"] = 0
print(animals_on_campus)

animals_on_campus["Foxes"] = 4
print(animals_on_campus)

# activity 2

translation = {'mountain': 'blenon', 'bread': 'havon', 'friend': 'raqiros', 'horse': ' anne'}
print(translation['bread'])

# activity 1

numbers_as_string = input("Enter some numbers: ")
numbers = numbers_as_string.split()
output = []  # create new lists, changing old lists will just confuse the list

for number in numbers:
    if int(number) % 2 != 0:
        output.append(number)

print(output)

