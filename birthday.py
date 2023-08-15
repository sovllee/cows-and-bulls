import json

def save_to_json(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    try:
        with open("data.json", "r") as file:
            nb = json.load(file)
    except FileNotFoundError:
        nb = {}
    
    print("I know birthdays of:")
    for name in nb:
        print(name)
    
    x = input("Whose birthday are you willing to know?: ")
    
    if x in nb:
        print(f"The birthday of {x} is {nb[x]}")
    else:
        print(f"Sorry, I don't know the birthday of {x}")
    
    add_new = input("Do you want to add a new person and birthday? (yes/no): ")
    
    if add_new.lower() == "yes":
        new_name = input("Enter the new person's name: ")
        new_birthday = input("Enter the new person's birthday: ")
        nb[new_name] = new_birthday
        save_to_json(nb)
        print(f"{new_name}'s birthday has been added to the dictionary.")


