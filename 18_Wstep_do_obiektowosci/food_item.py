import csv

class FoodItem:
    def __init__(self, food_id, name, price):
        self.food_id = food_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"FoodItem(id={self.food_id}, name='{self.name}', price={self.price})"


def load_food_items_from_csv(file_path):
    food_items = []

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Pomijamy nagłówek, jeśli istnieje
        header = next(csv_reader, None)

        for row in csv_reader:
            # Zakładamy, że kolejność kolumn w pliku CSV to: id, name, price
            food_id, name, price = row
            food_item = FoodItem(food_id, name, float(price))
            food_items.append(food_item)

    return food_items


# Przykładowe użycie:
file_path = 'foods.csv'  # Zmień na właściwą ścieżkę do pliku CSV
food_items_list = load_food_items_from_csv(file_path)

# Wyświetlenie wczytanych obiektów FoodItem
for food_item in food_items_list:
    print(food_item)

