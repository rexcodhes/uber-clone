# Uber App Simulation

This is a simple Python application that simulates some basic functionalities of a ride-hailing service like Uber. Users can view available locations, book rides, cancel rides, view their ride history, and manage their profiles.

## Features

* **View Map:** See a list of predefined cities and their "distances" (represented by numerical values).
* **Book a Ride:**
    * Select a starting location and destination.
    * Choose a vehicle type (Bike, Auto, Car).
    * Calculates the fare based on distance and vehicle type.
    * Confirms ride booking and saves it to history.
* **Cancel a Ride:** Cancel a previously booked ride from your history.
* **Ride History:** View a list of all your past rides, including details like location, destination, distance, vehicle, and fare.
* **User Profiles:**
    * Create a new user profile with name, age, and rating.
    * Automatically tracks rides booked and money spent for each profile.
    * Update existing profile details.
    * Delete a profile.
    * Open and view specific profile details.

## How to Run

1.  **Save the code:** Save the provided Python code as `uber.py` in a directory.
2.  **Run from terminal:** Open your terminal or command prompt, navigate to the directory where you saved `uber.py`, and run the script using:
    ```bash
    python uber.py
    ```

## Data Storage

The application uses plain text files (`uber.txt` for ride data and `profile.txt` for profile data) to store information in JSON format. These files will be created automatically in the same directory as `uber.py` when you first interact with the ride booking or profile creation features.

## Project Structure

* `uber.py`: The main Python script containing all the application logic.
* `uber.txt`: (Generated after first ride booking) Stores a list of dictionaries, each representing a booked ride.
* `profile.txt`: (Generated after first profile creation) Stores a list of dictionaries, each representing a user profile.

## Code Overview

### `map` and `vehicles` Dictionaries

The `map` dictionary defines cities and their linear "distances." The `vehicles` dictionary stores vehicle types and their respective fare multipliers.

```python
map = {"Kolkata": 10, "Delhi": 50, "Bangalore": 100, "Mumbai": 140, "Darjeeling": 210, "Pune": 350}
vehicles = {"Bike": 0.75, "Auto": 1, "Car": 1.25}