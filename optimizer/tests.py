from django.test import TestCase

# Create your tests here.
import os
from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
import csv


class OptimizeRouteViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.file_path = os.path.join('data', 'customer-requests-testingLondon36.csv')
        self.url = reverse('optimize_route')

        # Create a sample CSV file for testing
        os.makedirs('data', exist_ok=True)
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['pickup_lat', 'pickup_lng', 'dropoff_lat', 'dropoff_lng'])
            writer.writerow(['51.5181999', '-0.083709061', '51.5171675', '-0.1043089'])
            writer.writerow(['51.5171675', '-0.1043089', '51.5181999', '-0.083709061'])

    def tearDown(self):
        # Remove the sample CSV file after tests
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_optimize_route_view_with_valid_file(self):
        response = self.client.get(self.url, {'file_path': self.file_path, 'max_distance': 50})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertIn('map_links', response.json())

    def test_optimize_route_view_with_invalid_file(self):
        response = self.client.get(self.url, {'file_path': 'invalid/path.csv', 'max_distance': 50})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode(), "CSV file not found.")


import os
from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
import csv


class DataSourceTableViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.file_path = os.path.join('data', 'customer-requests-testingLondon36.csv')
        self.url = reverse('data_source')

        # Create a sample CSV file for testing
        os.makedirs('data', exist_ok=True)
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['pickup_lat', 'pickup_lng', 'dropoff_lat', 'dropoff_lng'])
            writer.writerow(['51.5181999', '-0.083709061', '51.5171675', '-0.1043089'])
            writer.writerow(['51.5171675', '-0.1043089', '51.5181999', '-0.083709061'])

    def tearDown(self):
        # Remove the sample CSV file after tests
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_data_source_table_view_with_valid_file(self):
        response = self.client.get(self.url, {'file_path': self.file_path})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertIn('data', response.json())

    def test_data_source_table_view_with_invalid_file(self):
        response = self.client.get(self.url, {'file_path': 'invalid/path.csv'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode(), "CSV file not found.")
