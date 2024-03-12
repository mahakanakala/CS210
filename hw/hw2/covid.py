import re
import csv
from collections import defaultdict, Counter

def age_col(input_file):
    edited_data = []
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        header = next(reader)
        edited_data.append(header) 
        for row in reader:
            if '-' in row['age']:
                ages = row['age'].split('-')
                avg_age = (int(ages[0]) + int(ages[1])) / 2
                row['age'] = str(avg_age)
            edited_data.append(row)

    return edited_data

def date_col(input_file):
    edited_data = []
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        header = next(reader)
        edited_data.append(header)
        for row in reader:
            if '.' in row['date_onset_symptoms']:
                date = row['date_onset_symptoms'].split('.')
                day, month, year = date[0], date[1], date[2]
                row['date_onset_symptoms'] = month + "." + day + "."+ year
            edited_data.append(row)
    
    return edited_data

def replace_empty_vals(input_file):
    edited_data = []
    province_data = defaultdict(list)

    # Read the input CSV file and store data by province
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        header = next(reader)
        edited_data.append(header)  # Include header in the edited data
        for row in reader:
            province_data[row['province']].append(row)

    # Calculate the average latitude and longitude for each province
    for province, data in province_data.items():
        lat_sum = 0
        long_sum = 0
        count = 0
        for entry in data:
            if entry['latitude'].lower() != 'nan' and entry['longitude'].lower() != 'nan':
                lat_sum += float(entry['latitude'])
                long_sum += float(entry['longitude'])
                count += 1

        if count > 0:
            lat_avg = round(lat_sum / count, 2)
            long_avg = round(long_sum / count, 2)

            # Update missing latitude and longitude values with the average
            for entry in data:
                if entry['latitude'].lower() == 'nan' or entry['longitude'].lower() == 'nan':
                    entry['latitude'] = str(lat_avg)
                    entry['longitude'] = str(long_avg)

            edited_data.extend(data) 

    return edited_data

def fill_missing_city_values(file_path):
    province_city_counts = defaultdict(Counter)
    updated_rows = []
    
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row['city'].strip().lower()
            province = row['province'].strip().lower()
            if city != 'nan':
                province_city_counts[province][city] += 1
    
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row['city'].strip().lower()
            province = row['province'].strip().lower()
            if city == 'nan':
                if province in province_city_counts:
                    most_common_cities = province_city_counts[province].most_common()
                    if most_common_cities:
                        # Sort by city name alphabetically in case of a tie
                        most_common_cities.sort(key=lambda x: (x[1], x[0]))
                        row['city'] = most_common_cities[0][0]
                else:
                    # If no data for the province, fill with 'Unknown'
                    row['city'] = 'Unknown'
            updated_rows.append(row)
            # print(updated_rows)
    
    return updated_rows

def fill_missing_symptoms_values(input_file):
    province_symptoms_counts = {}

    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            symptoms = row['symptoms'].strip().lower()
            province = row['province'].strip().lower()
            if symptoms != 'nan':
                if province not in province_symptoms_counts:
                    province_symptoms_counts[province] = Counter()
                province_symptoms_counts[province][symptoms] += 1

    updated_rows = []
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            symptoms = row['symptoms'].strip().lower()
            province = row['province'].strip().lower()
            if symptoms == 'nan':
                if province in province_symptoms_counts:
                    most_common_symptoms = province_symptoms_counts[province].most_common()
                    if most_common_symptoms:
                        most_common_symptoms.sort(key=lambda x: (x[1], x[0]))
                        row['symptoms'] = most_common_symptoms[0][0]
                else:
                    row['symptoms'] = 'Unknown'
            updated_rows.append(row)

    return updated_rows

def covid_file_name(input_file, output_file='covidResult.csv'):
    age_col_csv = age_col(input_file)
    date_col_csv = date_col(input_file)
    replace_empty_vals_csv = replace_empty_vals(input_file)
    fill_missing_symptoms_values_csv = fill_missing_symptoms_values(input_file)
    
    # Merge data from all processing steps
    merged_data = []
    for rows in zip(age_col_csv, date_col_csv, replace_empty_vals_csv, fill_missing_symptoms_values_csv):
        merged_row = {}
        for row in rows:
            merged_row.update(row)
        merged_data.append(merged_row)
    
    # Write merged data to output CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=merged_data[0].keys())
        writer.writeheader()
        writer.writerows(merged_data)

covid_file_name('../data/covidTrain.csv')