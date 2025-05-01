Creating an eco-footprint analyzer involves designing a program that collects data on various activities related to carbon emissions, calculates the carbon footprint, and provides some form of visualization to help users understand their impact. Below is a sample Python program that performs these tasks. The program focuses on simplicity and clarity, and includes error handling and comments for guidance.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Constants for emission factors
EMISSION_FACTORS = {
    'electricity': 0.233,  # kg CO2 per kWh
    'natural_gas': 2.20462,  # kg CO2 per Therm
    'car_mileage': 0.404,  # kg CO2 per mile
    'flights': 192.0,  # kg CO2 per hour of flight
    'meat_consumption': 10.0,  # kg CO2 per kg of meat consumed
}

def get_input(prompt, cast_type=float, minimum=0):
    """
    Helper function to get a user input with error handling.
    """
    while True:
        try:
            value = cast_type(input(prompt))
            if value < minimum:
                raise ValueError("Value must be equal to or greater than {}.".format(minimum))
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def calculate_carbon_footprint(data):
    """
    Calculate the carbon footprint based on user provided data and emission factors.
    """
    total_footprint = 0.0
    breakdown = {}
    
    for activity, value in data.items():
        footprint = value * EMISSION_FACTORS.get(activity, 0)
        breakdown[activity] = footprint
        total_footprint += footprint
    
    return total_footprint, breakdown

def visualize_footprint(breakdown):
    """
    Create a pie chart to visualize the carbon footprint breakdown.
    """
    activities = list(breakdown.keys())
    emissions = list(breakdown.values())
    
    plt.figure(figsize=(10, 7))
    plt.pie(emissions, labels=activities, autopct='%1.1f%%', startangle=140)
    plt.title('Carbon Footprint Breakdown')
    plt.show()

def main():
    print("Welcome to the Eco-Footprint Analyzer!\nPlease enter your activity data:")

    # Collecting activity data from the user
    data = {
        'electricity': get_input("Enter electricity usage (kWh): "),
        'natural_gas': get_input("Enter natural gas usage (Therms): "),
        'car_mileage': get_input("Enter car mileage (miles): "),
        'flights': get_input("Enter flight hours: "),
        'meat_consumption': get_input("Enter meat consumption (kg): ")
    }

    # Calculate and display the carbon footprint
    total_footprint, breakdown = calculate_carbon_footprint(data)
    print(f"\nYour total carbon footprint is: {total_footprint:.2f} kg CO2")

    # Visualize the carbon footprint breakdown
    visualize_footprint(breakdown)

if __name__ == "__main__":
    main()
```

This program:

1. **Collects data** from the user about their electricity usage, natural gas usage, car mileage, flight hours, and meat consumption.
2. **Calculates the carbon footprint** using predefined emission factors (assumed for simplicity).
3. **Visualizes the carbon footprint** with a pie chart to illustrate which activities contribute the most.
4. **Includes error handling** to manage invalid input gracefully.

You can extend this program by adding more activities, customizing emission factors, or integrating more sophisticated data input methods. Remember, this is a simplified model and real-world applications might require more parameters and different assumptions based on local emission factors.