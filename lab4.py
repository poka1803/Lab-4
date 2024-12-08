import random

items = {
    'r': (3, 25),  
    'p': (2, 15),  
    'a': (2, 15),  
    'm': (2, 20),  
    'i': (1, 5),   
    'k': (1, 15),  
    'x': (3, 20),  
    't': (1, 25),  
    'f': (1, 15),  
    'd': (1, 10),  
    's': (2, 20),  
    'c': (2, 20)   }


backpack_size = (2, 4) 
total_cells = backpack_size[0] * backpack_size[1]  
initial_survival_points = 20  
mandatory_item = 'd'  


def random_combination():
    all_items = list(items.keys())
    
    selected_items = [mandatory_item]
    total_size = items[mandatory_item][0]  

    remaining_items = all_items.copy()
    remaining_items.remove(mandatory_item)  

    
    while total_size < total_cells:
        item = random.choice(remaining_items)
        item_size = items[item][0]
        if total_size + item_size <= total_cells:
            selected_items.append(item)
            total_size += item_size
        
        remaining_items.remove(item)

    return selected_items

def calculate_inventory(items_to_take):
    total_size = 0
    total_points = initial_survival_points

    for item in items_to_take:
        size, points = items[item]
        total_size += size
        total_points += points

    all_items_set = set(items.keys())
    for item in all_items_set - set(items_to_take):
        size, points = items[item]
        total_points -= points

    return total_size, total_points

def generate_valid_combination():
    while True:
        items_to_take = random_combination()
        total_size, total_survival_points = calculate_inventory(items_to_take)

        if total_survival_points > 0:  
            return items_to_take, total_size, total_survival_points
        else:
            print(f"Сгенерированная комбинация {items_to_take} имеет отрицательные очки выживания.Попробуем еще раз.")

items_to_take, total_size, total_survival_points = generate_valid_combination()

inventory = [[None for _ in range(backpack_size[1])] for _ in range(backpack_size[0])]

idx = 0
for i in range(backpack_size[0]):
    for j in range(backpack_size[1]):
        if idx < len(items_to_take):
            inventory[i][j] = items_to_take[idx]
            idx += 1

for row in inventory:
    print('[' + '],['.join(item if item is not None else ' ' for item in row) + ']')

print("Итоговые очки выживания:", total_survival_points)