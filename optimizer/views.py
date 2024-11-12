from django.http import JsonResponse
from django.shortcuts import render

# optimize_route_view:

# Loads a specific CSV file containing route data.
# Calls the optimize_routes function to generate optimized Google Maps links for each route.
# Returns these map links as a JSON response, allowing you to see all routes in Google Maps format via an API endpoint.


# data_source_table_view:

# Loads the same CSV file to display the raw data in a web template.
# If the file is missing, it shows an error message in the template.
# Passes the data to a template as a table, enabling you to view and verify the dataset used for route optimization.

import os

def optimize_route_view(request):

    map_links =""

    return JsonResponse({
        "map_links": map_links
    })


def data_source_table_view(request):
    file_path = os.path.join('data', 'customer-requests-testingLondon36.csv')
    context = ""
    
    return render(request, 'optimizer/data_source.html', context)