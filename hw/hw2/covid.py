import csv
from collections import defaultdict, Counter

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
    
    return updated_rows

def preprocess_covid_data(input_file):
    # Read input CSV file
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # Task 1: Replace age ranges with rounded average
    for row in data:
        if '-' in row['age']:
            age_range = row['age'].split('-')
            avg_age = round((int(age_range[0]) + int(age_range[1])) / 2)
            row['age'] = str(avg_age)

    # Task 2: Change date format for date columns
    for row in data:
        date_columns = ['date_onset_symptoms', 'date_admission_hospital', 'date_confirmation']
        for col in date_columns:
            if row[col]:
                parts = row[col].split('.')
                row[col] = parts[1] + '.' + parts[0] + '.' + parts[2]

    # Task 3: Fill missing latitude and longitude values by province average
    province_latitudes = defaultdict(list)
    province_longitudes = defaultdict(list)
    for row in data:
        if row['latitude'] and row['longitude']:
            province_latitudes[row['province']].append(float(row['latitude']))
            province_longitudes[row['province']].append(float(row['longitude']))

    for row in data:
        if not row['latitude'] or not row['longitude']:
            province = row['province']
            if province in province_latitudes:
                avg_lat = round(sum(province_latitudes[province]) / len(province_latitudes[province]), 2)
                avg_lon = round(sum(province_longitudes[province]) / len(province_longitudes[province]), 2)
                row['latitude'] = str(avg_lat)
                row['longitude'] = str(avg_lon)

    # Task 4: Fill missing city values by most occurring city in province
    # province_cities = defaultdict(list)
    # for row in data:
    #     if row['city']:
    #         province_cities[row['province']].append(row['city'])

    # for row in data:
    #     if not row['city']:
    #         province = row['province']
    #         if province in province_cities and province_cities[province]:
    #             mode_city = max(set(province_cities[province]), key=province_cities[province].count)
    #             row['city'] = mode_city
    updated_rows = fill_missing_city_values(input_file)

    # Task 5: Fill missing symptom values by most frequent symptom in province
    province_symptoms = defaultdict(list)
    for row in data:
        if row['symptoms']:
            province_symptoms[row['province']].extend(row['symptoms'].split(';'))

    for row in data:
        if not row['symptoms']:
            province = row['province']
            if province in province_symptoms:
                mode_symptom = max(set(province_symptoms[province]), key=province_symptoms[province].count)
                row['symptoms'] = mode_symptom

    # Write result to output CSV file
    with open('covidResult.csv', 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Test the function with the provided sample file
preprocess_covid_data('../data/covidTrain.csv')
