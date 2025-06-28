# Map is linear
import json 
map = {"Kolkata": 10, "Delhi": 50, "Bangalore": 100, "Mumbai": 140, "Darjeeling": 210, "Pune": 350}
map_keys = list(map.keys())
map_distance = list(map.values())
vehicles = {"Bike": 0.75, "Auto": 1, "Car": 1.25}
p_rides_booked = 0
money_spent = 0

class Profile:
    def __init__(self, name, age, rating, rides_booked, money_spent):
        self.name = name
        self.age = age
        self.rating = rating
        self.rides_booked = rides_booked
        self.money_spent = money_spent
    def __str__(self):
     return f"Profile(name={self.name}, age={self.age}, ratings={self.rating}, rides booked={self.rides_booked}, money spent ={self.money_spent})"

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

def load_data_profile():
    try:
        with open('profile.txt', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return[]
    
def save_profile_helper(profile):
    with open('profile.txt', 'w') as file:
        json.dump(profile, file)

def list_all_rides(rides):
     print("\n")
     print("*" * 100)
     for index, rides in enumerate(rides, start=1):
        print(f"{index}.{rides['current_location']}, Destination: {rides['destination']},Distance: {rides['distance']}, Vehicle: {rides['vehicle']}, Fare: {rides['fare']}")
        print("*" * 100)

def open_map():
    print(map_keys)

def book_ride(map, rides):
    global money_spent
    print("Let's book your ride: ")
    
    from_where = input("From where: ")
    where_to = input("Where to: ")
    
    map_distance = abs(map[where_to] - map[from_where]) 
    vehicle = input("What type of vehicle would you like: ")
    base_fare = map_distance * 10
    final_fare = base_fare * vehicles[vehicle]
    
    print(f"Your ride from {from_where} to {where_to} with a distance of {map_distance}km will cost you {final_fare}rs")
    confirmation = input("Do you want to confirm your ride?: (yes/no) ")
    confirmation_lower = confirmation.lower()
    
    if confirmation_lower == "yes":
        print(f"Your ride to {where_to} has been confirmed")
        rides.append({'current_location': from_where, 'destination': where_to, 'distance': map_distance, 'vehicle':vehicle, 'fare':final_fare})
        save_data_helper(rides)
        money_spent += final_fare
    
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

def history_rides(rides):
    print("Here is the history of all of your past rides: ")
    list_all_rides(rides)

def create_profile(rides,profile, p_rides_booked):
    
    p_name = input("What is your name? ")
    p_age = input("What is your age? ")
    p_ratings = input("What is your rating? ")
    p_rides_booked = len(rides)
    p_money_spent = sum(ride['fare'] for ride in rides)
    profile.append({'Name': p_name, 
                    'Age': p_age, 
                    'Rating': p_ratings, 
                    'Rides_Booked':p_rides_booked, 
                    'Money_Spent': p_money_spent})
    save_profile_helper(profile)

def update_profile(profile):
    print(profile)
    id = int(input("Enter your profile id to update: "))
    if 1 <= id <= len(profile):
     profiles = profile[id-1]
     name = input("Enter your new name ")
     age = input("Enter your new age ")
     rating = input("Enter your new rating ")
     p_rides_booked = profiles['Rides_Booked']
     money_spent = profiles['Money_Spent']
     profile[id - 1] = {'Name': name, 'Age': age, 'Rating': rating, 'Rides_Booked': p_rides_booked, 'Money_Spent': money_spent} 
     save_profile_helper(profile)
    else:
        print("Invalid id selected")

def delete_profile():
    pass

def open_profile():
    pass

def main():
    rides = load_data()
    profile = load_data_profile()

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
            history_rides(rides)
        
        elif choice == 5:
            create_profile(rides,profile, p_rides_booked)
        
        elif choice == 6:
            update_profile(profile)

if __name__ == "__main__":
    main()




