# Map is linear
import json 
map = {"Kolkata": 10, "Delhi": 50, "Bangalore": 100, "Mumbai": 140, "Darjeeling": 210, "Pune": 350}
map_keys = list(map.keys())
map_distance = list(map.values())
vehicles = {"Bike": 0.75, "Auto": 1, "Car": 1.25}

def load_data():
    try:
        with open('uber.txt', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return[]
    
def save_data_helper(rides):
    with open('uber.txt', 'w') as file:
        json.dump(rides, file)

def list_all_rides(rides):
     print("\n")
     print("*" * 100)
     for index, rides in enumerate(rides, start=1):
        print(f"{index}.{rides['current_location']}, Destination: {rides['destination']},Distance: {rides['distance']}, Vehicle: {rides['vehicle']}, Fare: {rides['fare']}")
        print("*" * 100)


def open_map():
    print(map_keys)

def book_ride(map, rides):
    print("Let's book your ride: ")
    from_where = input("From where: ")
    where_to = input("Where to: ")
    map_distance = abs(map[where_to] - map[from_where]) 
    vehicle = input("What type of vehicle would you like: ")
    base_fare = map_distance * 10
    final_fare = base_fare * vehicles[vehicle]
    print(f"Your ride from {from_where} to {where_to} with a distance of {map_distance} will cost you {final_fare}rs")
    confirmation = input("Do you want to confirm your ride?: (yes/no) ")
    confirmation_lower = confirmation.lower()
    if confirmation_lower == "yes":
        print(f"Your ride to {where_to} has been confirmed")
        rides.append({'current_location': from_where, 'destination': where_to, 'distance': map_distance, 'vehicle':vehicle, 'fare':final_fare})
        save_data_helper(rides)
    elif confirmation_lower == "no":
        print("Your ride has not been placed")

    else: print("Invalid input")


def cancel_ride(rides):
    list_all_rides(rides)
    cancel = int(input("Which ride do you want to cancel? "))
    ride = rides[cancel-1]

    if 1 <= cancel <= len(rides):
        del rides[cancel-1]
        save_data_helper(rides)
        print(f"{cancel}. {ride['current_location']} to {ride['destination']}, distance covered {ride['distance']}kms, for rupees {ride['fare']}, in a {ride['vehicle']} has been cancelled")
    else: 
        print("Invalid ride selected")

def history_rides():
    pass

def create_profile():
    pass

def update_profile():
    pass

def delete_profile():
    pass

def open_profile():
    pass


def main():
    rides = load_data()

    while(True):
        print("Uber App")
        print("Type 1 to look at the map")
        print("Type 2 to book a ride")
        print("Type 3 to cancel a ride")
        print("Type 4 to look at history")
        print("Type 5 to create a profile")
        print("Type 6 to update a profile")
        print("Type 7 to delete a profile")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            open_map()

        elif choice == 2:
            book_ride(map, rides)

        elif choice == 3:
            cancel_ride(rides)
        
        elif choice == 4:
            list_all_rides(rides)


if __name__ == "__main__":
    main()




