import requests
import csv
import json

api_url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(api_url)
api_data = response.json()

csv_file_name = "api_D.csv"
with open(csv_file_name, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['json_data'])  # Write a header for the CSV file
    
    # Convert each JSON object to a string and write it to the CSV file
    for item in api_data:
        json_string = json.dumps(item)
        writer.writerow([json_string])

print("Data loaded and saved into '{}' as JSON format in CSV file successfully.".format(csv_file_name))
