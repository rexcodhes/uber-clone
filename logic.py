import random
import json
import os
locations = {
    "Kolkata": 10,
    "Delhi": 20,
    "Bangalore": 30,
    "Mumbai": 40,
    "Darjeeling": 50,
    "Pune": 60
}

vehicles = {
    "Bike": 0.75,
    "Auto": 1.0,
    "Cab": 1.25
}

is_cancled = False
data_found = False
data_save = False
ride_history_list = []
user_profile = {}
user_data = {}
login = False
file_path = "user_data.json"



def generate_token():
    token = random.randint(10000, 99999)
    return token


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def fill_data(name, age, phone_num, adult, ride_history=None):
    global data_save
    if ride_history is None:
        ride_history = []

    data = {}

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

    data[name] = {
        "name": name,
        "age": age,
        "phone_num": phone_num,
        "adult": adult,
        "ride_history": ride_history
    }

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        data_save = True
        return data_save


def get_data(name):
    global data_found
    if not os.path.exists(file_path):
        print("No data found.")
        return None

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("Empty or corrupt JSON. Initializing empty data.")
            data = {}

    if name in data:
        data_found = True
        return data[name]
    else:
        data_found = False
        return False


def open_map():
    clear_screen()
    print("\nAvailable Locations:")
    for i, city in enumerate(locations.keys(), start=1):
        print(f"{i}: {city}")
    input("Press Enter to continue...")


def book_ride():
    clear_screen()
    print("\nBook a Ride")
    current_location = input("Enter your current location: ").strip().title()
    destination = input("Enter your destination: ").strip().title()

    if current_location not in locations or destination not in locations:
        print("Invalid location(s). Please choose from the available map.")
        return

    distance = abs(locations[destination] - locations[current_location])
    print(
        f"Distance between {current_location} and {destination}: {distance} km")

    print("Available vehicles: Bike, Auto, Cab")
    vehicle = input("Choose your vehicle: ").strip().title()

    if vehicle not in vehicles:
        print("Invalid vehicle. Please choose from available options.")
        return

    base_fare = distance * 10
    final_fare = base_fare * vehicles[vehicle]
    print(f"Your {vehicle} ride from {current_location} to {destination} of {distance} kms will cost {final_fare:.2f} rupees")

    confirmation = input("Please confirm your ride (yes/no): ").strip().lower()
    token = generate_token()
    if confirmation == "yes":
        print(
            f"Your ride to {destination} has been booked and your token number is {token}.")
        ride_history_list.append({
            "from": current_location,
            "to": destination,
            "vehicle": vehicle,
            "fare": final_fare,
            "token": token,
            "is_cancled": is_cancled
        })
        save_ride_to_file(user_data["name"], ride_history_list[-1])
    else:
        print("Ride booking cancelled")
    input("Press Enter to continue...")


def save_ride_to_file(name, new_ride):
    if not os.path.exists(file_path):
        return
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        data = {}

    if name in data:
        if "ride_history" not in data[name]:
            data[name]["ride_history"] = []
        data[name]["ride_history"].append(new_ride)

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)


def ride_desc():
    clear_screen()
    if not ride_history_list:
        input("Please book a ride first. No rides booked yet.")
    else:
        for i, ride in enumerate(ride_history_list, start=1):
            print(
                f"\n Hello {user_data['name']} your ride from {ride['from']} to {ride['to']} via {ride['vehicle']} has been booked and your token number is {ride['token']}.")
            input("Press Enter to continue...")


def cancel_ride():
    clear_screen()
    print("\nCancel Ride")

    token = input("Enter your ride token to cancel: ").strip()
    try:
        token = int(token)
    except ValueError:
        input("Invalid token format. Press Enter to try again.")
        return

    # Load full data
    if not os.path.exists(file_path):
        print("No ride data found.")
        return

    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Corrupted data file.")
            return

    name = user_data["name"]
    if name not in data or not data[name]["ride_history"]:
        print("No rides found for this user.")
        return

    found = False
    for ride in data[name]["ride_history"]:
        if ride["token"] == token:
            ride["is_cancled"] = True
            found = True
            print(
                f"Ride from {ride['from']} to {ride['to']} has been cancelled successfully.")
            break

    if not found:
        print("No ride matched with this token.")

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    input("Press Enter to continue...")


def ride_history():
    clear_screen()
    data = get_data(user_data["name"])
    if not data['ride_history']:
        input("No rides booked yet.")
        return

    print("\nRide History:")
    for i, ride in enumerate(data['ride_history'], start=1):
        situation = "Cancelled ❌" if ride.get('is_cancled') else "Booked ✅"
        print(
            f"\nSituation: {situation}\nRide {i}.\nToken Number: {ride['token']} \nFrom: {ride['from']} \nTo: {ride['to']} \nVehicle: {ride['vehicle']} \nFare: ₹{ride['fare']:.2f}")
    input("\nPress Enter to continue...")


def create_profile():
    global user_data
    global login
    name = input("Enter your name: ").strip().capitalize()
    username = get_data(name)
    if not username:
        global data_save
        data_save = False
        try:
            age = int(input("Enter your age: ").strip())
            phone = int(input("Enter your phone number: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            main()
            return
        age = int(age)
        if age >= 18:
            adult = True
        else:
            adult = False

        fill_data(name, age, phone, adult)
        user_data.update(get_data(name))
        if data_save == True:
            input("Profile created successfully.")
        else:
            input("There are some Error..")
        global login
        login = True
        co_main()
        return user_data
    else:
        user_data.update(username)
        login = True
        # print(user_data)
        co_main()
        return None


def edit_profile():
    clear_screen()
    print("Edit Profile (leave blank to keep unchanged):")
    name = input(f"New Name ({user_data.get('name')}): ").strip()
    age = input(f"New Age ({user_data.get('age')}): ").strip()
    phone = input(f"New Phone ({user_data.get('phone_num')}): ").strip()

    old_name = user_data['name']

    # Load full data
    with open(file_path, 'r') as f:
        try:
            all_data = json.load(f)
        except json.JSONDecodeError:
            all_data = {}

    if old_name not in all_data:
        print("User not found.")
        return

    if name:
        new_name = name
    else:
        new_name = old_name

    all_data[new_name] = all_data.pop(old_name)

    if age:
        all_data[new_name]['age'] = int(age)
    if phone:
        all_data[new_name]['phone_num'] = int(phone)
    if name:
        all_data[new_name]['name'] = new_name

    user_data['name'] = new_name
    if age:
        user_data['age'] = int(age)
    if phone:
        user_data['phone_num'] = int(phone)

    with open(file_path, 'w') as f:
        json.dump(all_data, f, indent=4)

    input("Profile updated successfully.")



def show_profile():
    clear_screen()
    if not user_profile:
        print("No profile to show.")
    else:
        print("\nProfile Information:")
        for key, value in user_profile.items():
            print(f"{key.capitalize()}: {value}")
            input("Press Enter to continue...")


def co_main():
    global login
    global user_data
    while login == True:
        clear_screen()
        print(f"\nHello {user_data['name']} Welcome to Uber")
        print("1. Open Map")
        print("2. Book a Ride")
        print("3. Description of Ride")
        print("4. Cancel Last Ride")
        print("5. View Ride History")
        print("6. Edit Profile")
        print("7. Show Profile")
        print("8. LogOut")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            open_map()
        elif choice == 2:
            book_ride()
        elif choice == 3:
            ride_desc()
        elif choice == 4:
            cancel_ride()
        elif choice == 5:
            ride_history()
        elif choice == 6:
            edit_profile()
        elif choice == 7:
            show_profile()
        elif choice == 8:
            login = False
            print("Logged out successfully.")
            break
        elif choice == 9:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    while login == False:
        clear_screen()
        print("Welcome to Uber")
        print("1.Login Or Register")
        print("2.View Map")
        print("3.Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if choice == 1:
            create_profile()
        elif choice == 2:
            open_map()
        elif choice == 3:
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please try again.")


# {% comment % } { % if result is not none % }
#         <h2 > Result: < /h2 >
#         <p > {{n1}} + {{n2}} = <strong > {{result}} < /strong > </p >
#     {% endif %} {% endcomment %}

if __name__ == "__main__":
    main()
