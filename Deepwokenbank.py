weapons = {}

def add_weapon():
    name = input("Enter the name of the weapon: ")
    stars = int(input("Enter the number of stars (1-3): "))
    buff = input("Enter the buff associated with the stars: ")
    enchant = input("Does the weapon have an enchant? (yes/no): ")
    enchant_name = ""

    if enchant.lower() == "yes":
        enchant_name = input("Enter the name of the enchant: ")

    weapon_data = {"stars": stars, "buff": buff, "enchant": enchant_name}

    if name in weapons:
        weapons[name].append(weapon_data)
    else:
        weapons[name] = [weapon_data]

    print("Weapon data added successfully!")

def retrieve_weapon():
    name = input("Enter the name of the weapon to retrieve: ")
    if name in weapons:
        weapon_list = weapons[name]
        print(f"Weapon: {name}")
        for i, weapon_data in enumerate(weapon_list, start=1):
            print(f"Variant {i}:")
            print(f"Stars: {weapon_data['stars']}")
            print(f"Buff: {weapon_data['buff']}")
            enchant_name = weapon_data['enchant']
            if enchant_name:
                print(f"Enchant: {enchant_name}")
            print()
    else:
        print("Weapon not found!")

def main():
    while True:
        print("--- Weapon Management System ---")
        print("1. Add weapon")
        print("2. Retrieve weapon")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_weapon()
        elif choice == "2":
            retrieve_weapon()
        elif choice == "3":
            print("Thank you for using the Weapon Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()