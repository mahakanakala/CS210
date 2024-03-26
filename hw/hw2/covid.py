import csv
from collections import defaultdict, Counter

def preprocess_covid_data(input_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # Task 1: Replace age ranges with rounded average
    for row in data:
        if '-' in row['age']:
            age_range = row['age'].split('-')
            avg_age = round((int(age_range[0]) + int(age_range[1])) / 2)
            row['age'] = str(avg_age)

    # Task 2: Change date format for the date columns
    for row in data:
        date_columns = ['date_onset_symptoms', 'date_admission_hospital', 'date_confirmation']
        for col in date_columns:
            if row[col]:
                parts = row[col].split('.')
                row[col] = parts[1] + '.' + parts[0] + '.' + parts[2]

    # Task 3: Fill missing latitude and longitude values by province average
    province_coordinates = defaultdict(list)
    for row in data:
        if row['latitude'] != 'NaN' and row['longitude'] != 'NaN':
            province_coordinates[row['province']].append((float(row['latitude']), float(row['longitude'])))

    for row in data:
        if row['latitude'] == 'NaN' or row['longitude'] == 'NaN':
            province = row['province']
            if province_coordinates[province]:
                avg_lat = sum(coord[0] for coord in province_coordinates[province]) / len(province_coordinates[province])
                avg_long = sum(coord[1] for coord in province_coordinates[province]) / len(province_coordinates[province])
                # Only round latitude and longitude if they were NaN
                if row['latitude'] == 'NaN':
                    row['latitude'] = round(avg_lat, 2)
                    # row['latitude'] = avg_lat
                if row['longitude'] == 'NaN':
                    row['longitude'] = round(avg_long, 2)
                    # row['longitude'] = avg_long

    # Task 4: Fill missing city values by most occurring city in province
    province_cities = defaultdict(Counter)
    for row in data:
        if row['city'] != 'NaN':
            province_cities[row['province']].update([row['city']])
    
    for row in data:
        if row['city'] == 'NaN':
            province = row['province']
            most_common_city = province_cities[province].most_common(1)
            if most_common_city:
                row['city'] = most_common_city[0][0]

    # Task 5: Fill missing symptom values by most frequent symptom in province
    province_symptoms = defaultdict(Counter)
    for row in data:
        if row['symptoms'] != 'NaN':
            for symptom in row['symptoms'].split('; '):
                province_symptoms[row['province']].update([symptom])
    
    for row in data:
        if row['symptoms'] == 'NaN':
            province = row['province']
            most_common_symptom = province_symptoms[province].most_common(1)
            if most_common_symptom:
                row['symptoms'] = most_common_symptom[0][0]

    # Write result to output CSV file
    with open('covidResult.csv', 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Test the function with the provided sample file
preprocess_covid_data('../data/covidTrain.csv')
