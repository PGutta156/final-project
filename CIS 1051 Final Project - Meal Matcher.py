import csv

def load_data():
    dishes = []
    with open('recipes.csv', newline='', encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        print("CSV Column Names:", reader.fieldnames)
        for row in reader:
            dishes.append(row)
    return dishes


# Recommends dishes based on the user's preferences
def recommend_dish(dishes, protein, spice_level, cuisine_type, cook_time, vegan, allergies, gluten_free):
    for dish in dishes:
        if (protein.lower() in dish['Primary Protein'].lower() and
            spice_level.lower() in dish['Spice Level'].lower() and
            cuisine_type.lower() in dish['Cuisine Type'].lower() and
            int(dish['Cook Time (mins)']) <= cook_time and
            (vegan == 'yes' and dish['Vegan?'] == 'Yes' or vegan == 'no') and
            (gluten_free == 'yes' and dish['Gluten-Free?'] == 'Yes' or gluten_free == 'no') and
            (allergies == 'no' or allergies.lower() not in dish['Allergens'].lower())):
            return dish['\ufeffDish Name']
    return "No dish matches your criteria. Try adjusting your preferences."

# Add a new dish to the CSV file
def add_dish():
    dish_name = input("Enter the name of the dish: ")
    primary_protein = input("Enter the primary protein: ")
    spice_level = input("Enter the spice level: ")
    cuisine_type = input("Enter the cuisine type: ")
    ingredients = input("Enter the ingredients: ")
    difficulty = input("Enter the difficulty (easy/medium/hard): ")
    vegetarian = input("Is it vegetarian? (yes/no): ")
    vegan = input("Is it vegan? (yes/no): ")
    gluten_free = input("Is it gluten-free? (yes/no): ")
    allergens = input("Enter any allergens (comma-separated, or 'none'): ")

    new_dish = [dish_name, primary_protein, spice_level, cuisine_type, ingredients, difficulty, vegetarian, vegan, gluten_free, allergens]

    with open('recipes.csv', mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_dish)

# Main function to run the Meal Matcher program
def main():
    dishes = load_data()
    
    while True:
        # Ask for user preferences
        print("Welcome to Meal Matcher!")
        print("Please provide your preferences:")
        protein = input("What primary protein do you want? ")
        spice_level = input("What spice level do you prefer? (Mild, Medium, or Hot) ")
        cuisine_type = input("What cuisine type do you want? ")
        cook_time = int(input("What is the maximum cook time (in minutes)? "))
        vegan = input("Do you want a vegan dish? (yes/no): ")
        allergies = input("Do you have any allergies? If so, list them (or enter 'no' to skip): ")
        gluten_free = input("Do you want a gluten-free dish? (yes/no): ")

        #dish based on user preferences
        recommended_dish = recommend_dish(dishes, protein, spice_level, cuisine_type, cook_time, vegan, allergies, gluten_free)
        print(f"We recommend you try: {recommended_dish}")
        
        #option to add a new dish, get another recommendation, or exit
        choice = input("Would you like to (1) add a new dish, (2) get a different recommendation, or (3) exit the Meal Matcher? (Enter 1, 2, or 3): ")

        if choice == '1':
            add_dish()
            print("New dish added successfully!")
        elif choice == '2':
            continue
        elif choice == '3':
            print("Exiting the Meal Matcher. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
