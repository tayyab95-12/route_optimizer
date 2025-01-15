from django.http import JsonResponse
from django.http import HttpResponse
import csv
from django.shortcuts import render

# optimize_route_view:

# Loads a specific CSV file containing route data.
# Calls the optimize_routes function to generate optimized Google Maps links for each route.
# Returns these map links as a JSON response, allowing you to see all routes in Google Maps format via an API endpoint.


# data_source_table_view:

# Loads the same CSV file to display the raw data in a web template.
# If the file is missing, it shows an error message in the template.
# Passes the data to a template as a table, enabling you to view and verify the dataset used for route optimization.
from django.views.decorators.http import require_http_methods

import os

from math import radians, cos, sin, sqrt, atan2


def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


def optimize_routes(data, max_distance):
    pickup_points = []
    dropoff_points = []
    routes = []

    # Separate pickup and dropoff points
    for entry in data:
        pickup_points.append((float(entry['pickup_lat']), float(entry['pickup_lng'])))
        dropoff_points.append((float(entry['dropoff_lat']), float(entry['dropoff_lng'])))

    # Optimize pickup points
    pickup_route = [pickup_points.pop(0)]
    while pickup_points:
        last_point = pickup_route[-1]
        nearest_point = min(pickup_points,
                            key=lambda point: haversine(last_point[0], last_point[1], point[0], point[1]))
        if haversine(last_point[0], last_point[1], nearest_point[0], nearest_point[1]) <= max_distance:
            pickup_route.append(nearest_point)
            pickup_points.remove(nearest_point)
        else:
            break

    # Optimize dropoff points
    dropoff_route = [dropoff_points.pop(0)]
    while dropoff_points:
        last_point = dropoff_route[-1]
        nearest_point = min(dropoff_points,
                            key=lambda point: haversine(last_point[0], last_point[1], point[0], point[1]))
        if haversine(last_point[0], last_point[1], nearest_point[0], nearest_point[1]) <= max_distance:
            dropoff_route.append(nearest_point)
            dropoff_points.remove(nearest_point)
        else:
            break

    # Generate Google Maps links for pickup and dropoff routes
    pickup_link = "https://www.google.com/maps/dir/" + "/".join([f"{lat},{lng}" for lat, lng in pickup_route])
    dropoff_link = "https://www.google.com/maps/dir/" + "/".join([f"{lat},{lng}" for lat, lng in dropoff_route])
    routes.append(pickup_link)
    routes.append(dropoff_link)

    return routes


@require_http_methods(["GET"])
def optimize_route_view(request):
    file_path = os.path.join('data', 'customer-requests-testingLondon36.csv')
    max_distance = float(request.GET.get('max_distance', 1))  # Default max distance is 1 km
    data = []

    if os.path.exists(file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    else:
        return HttpResponse("CSV file not found.", status=404)

    map_links = optimize_routes(data, max_distance)
    return JsonResponse({
        "map_links": map_links
    })


@require_http_methods(["GET"])
def data_source_table_view(request):
    file_path = os.path.join('data', 'customer-requests-testingLondon36.csv')
    data = []

    if os.path.exists(file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    else:
        return HttpResponse("CSV file not found.", status=404)

    context = {'data': data}
    return render(request, 'optimizer/data_source.html', context)
