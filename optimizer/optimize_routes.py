# Calculate Distances: Use the Haversine formula to calculate the distance between two geographic points (latitude and longitude). This will help in finding the nearest stop for each leg of the route.

# Estimate Travel Time: Calculate travel time dynamically based on distance, using a lower speed for short distances and a higher speed for longer distances. This ensures more accurate travel time estimates.

# Generate Google Maps Links: Create a Google Maps link that plots the optimized route on a map. Ensure that each stop in the route is unique to avoid duplicate waypoints.

# Optimize Route: Implement a point-to-point optimization by choosing the nearest unvisited location at each step. Organize pickups and drop-offs so that each route segment has a maximum number of stops, making the routes efficient and manageable.

# Load and Process Data: Load the data from a CSV file, preprocess it by setting default values where necessary, and convert it into a format suitable for optimization.

# Save and Export Results: Export each optimized route segment to a CSV file, including total distance, total duration, and a link to the Google Maps route. Return all Google Maps links for easy access.

# Run the Program: Execute the main function to load data, optimize the routes, and generate CSV files and map links for each route.