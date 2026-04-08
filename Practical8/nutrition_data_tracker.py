class food_item:
    def __init__(self, name, calories, carbohydrates, protein, fat):
        self.name = name
        self.calories = calories
        self.carbohydrates = carbohydrates
        self.protein = protein
        self.fat = fat

    def __repr__(self):
        return f"{self.name}: {self.calories} calories, {self.carbohydrates}g carbs, {self.protein}g protein, {self.fat}g fat"

def total(list_of_food_items, warning_thresholds):
    result = {
        'calories': sum(item.calories for item in list_of_food_items),
        'carbohydrates': sum(item.carbohydrates for item in list_of_food_items),
        'protein': sum(item.protein for item in list_of_food_items),
        'fat': sum(item.fat for item in list_of_food_items)
    }
    
    warning = ""
    if warning_thresholds:
        if result['calories'] > warning_thresholds['calories']  :
            warning += "Calorie intake exceeds recommended daily limit.\n"
        if result['fat'] > warning_thresholds['fat']:
            warning += "Fat intake exceeds recommended daily limit.\n"
            
    return result, warning

if __name__ == "__main__":
    food_items = []
    warning_thresholds = {'calories': 2500, 'fat': 90}  # Example thresholds
    
    while True:
        name = input("Enter food item name (keep blank to finish): ")
        if not name:
            break
        calories = float(input("Enter calories: "))
        carbohydrates = float(input("Enter carbohydrates (g): "))
        protein = float(input("Enter protein (g): "))
        fat = float(input("Enter fat (g): "))
        food_items.append(food_item(name, calories, carbohydrates, protein, fat))

    totals, warnings = total(food_items, warning_thresholds)
    print("\nFood Items Intook:")
    for item in food_items:
        print(f" - {item}")
    print("\nTotal Nutritional Intake:")
    print(f"Calories: {totals['calories']} kcal")
    print(f"Carbohydrates: {totals['carbohydrates']} g")
    print(f"Protein: {totals['protein']} g")
    print(f"Fat: {totals['fat']} g")
    if warnings:
        print(f"\nWarnings:\n{warnings}")