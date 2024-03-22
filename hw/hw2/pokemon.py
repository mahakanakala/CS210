import csv
from collections import defaultdict, Counter

# Task 1 Find out what percentage of "fire" type pokemons are at or above the "level" 40. (This is percentage over fire pokemons only, not all pokemons)
def calculate_fire_type_percentage(filename):
    total_fire_pokemons = 0
    fire_pokemons_above_level_40 = 0
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['type'] == 'fire':
                total_fire_pokemons += 1
                if float(row['level']) >= 40:
                    fire_pokemons_above_level_40 += 1
    
    percentage = (fire_pokemons_above_level_40 / total_fire_pokemons) * 100 if total_fire_pokemons > 0 else 0
    return round(percentage)

# Task 2: Fill in the missing "type" column values (given by NaN) by mapping them from the corresponding "weakness" values.
def fill_missing_types(filename):
    weakness_to_type_mapping = defaultdict(dict)  # Create a mapping for storing most common types for each weakness
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    for row in data:
        if row['weakness'] not in weakness_to_type_mapping:
            weakness_to_type_mapping[row['weakness']] = {}
        if row['type'] not in ['NaN', ''] and row['weakness'] != 'NaN':
            weakness_to_type_mapping[row['weakness']][row['type']] = weakness_to_type_mapping[row['weakness']].get(row['type'], 0) + 1

    for row in data:
        if row['type'] == 'NaN' and row['weakness'] != 'NaN':
            type_counts = weakness_to_type_mapping[row['weakness']]
            common_type = max(type_counts, key=type_counts.get)  # Get the most common type
            row['type'] = common_type

    return data

# Task 3: Fill in the missing (NaN) values in the Attack ("atk"), Defense ("def") and Hit Points ("hp") columns.
def fill_missing_values(data):
    atk_sum_over_40 = 0
    def_sum_over_40 = 0
    hp_sum_over_40 = 0
    atk_count_over_40 = 0
    def_count_over_40 = 0
    hp_count_over_40 = 0
    atk_sum_below_40 = 0
    def_sum_below_40 = 0
    hp_sum_below_40 = 0
    atk_count_below_40 = 0
    def_count_below_40 = 0
    hp_count_below_40 = 0
    
    for row in data:
        if row['atk'] != 'NaN':
            if float(row['level']) > 40:
                atk_sum_over_40 += float(row['atk'])
                atk_count_over_40 += 1
            else:
                atk_sum_below_40 += float(row['atk'])
                atk_count_below_40 += 1
        
        if row['def'] != 'NaN':
            if float(row['level']) > 40:
                def_sum_over_40 += float(row['def'])
                def_count_over_40 += 1
            else:
                def_sum_below_40 += float(row['def'])
                def_count_below_40 += 1
        
        if row['hp'] != 'NaN':
            if float(row['level']) > 40:
                hp_sum_over_40 += float(row['hp'])
                hp_count_over_40 += 1
            else:
                hp_sum_below_40 += float(row['hp'])
                hp_count_below_40 += 1
    
    avg_atk_over_40 = round(atk_sum_over_40 / atk_count_over_40, 1) if atk_count_over_40 > 0 else 0
    avg_def_over_40 = round(def_sum_over_40 / def_count_over_40, 1) if def_count_over_40 > 0 else 0
    avg_hp_over_40 = round(hp_sum_over_40 / hp_count_over_40, 1) if hp_count_over_40 > 0 else 0
    avg_atk_below_40 = round(atk_sum_below_40 / atk_count_below_40, 1) if atk_count_below_40 > 0 else 0
    avg_def_below_40 = round(def_sum_below_40 / def_count_below_40, 1) if def_count_below_40 > 0 else 0
    avg_hp_below_40 = round(hp_sum_below_40 / hp_count_below_40, 1) if hp_count_below_40 > 0 else 0
    
    for row in data:
        if row['atk'] == 'NaN':
            if float(row['level']) > 40:
                row['atk'] = str(avg_atk_over_40)
            else:
                row['atk'] = str(avg_atk_below_40)
        
        if row['def'] == 'NaN':
            if float(row['level']) > 40:
                row['def'] = str(avg_def_over_40)
            else:
                row['def'] = str(avg_def_below_40)
        
        if row['hp'] == 'NaN':
            if float(row['level']) > 40:
                row['hp'] = str(avg_hp_over_40)
            else:
                row['hp'] = str(avg_hp_below_40)
    
    return data

# Task 4: Create a dictionary that maps pokemon types to their personalities.
def create_pokemon_personality_mapping(filename):
    type_to_personality = defaultdict(set)
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    for row in data:
        type_to_personality[row['type']].add(row['personality'])

    for type, personalities in type_to_personality.items():
        type_to_personality[type] = sorted(personalities)

    return type_to_personality

# Task 5: Find out the average Hit Points ("hp") for pokemons of stage 3.0.
def calculate_average_hit_points(filename):
    total_hit_points = 0
    count_stage_3 = 0
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if float(row['stage']) == 3.0:
                count_stage_3 += 1
                total_hit_points += float(row['hp'])
    
    average_hp = round(total_hit_points / count_stage_3) if count_stage_3 > 0 else 0
    
    with open('pokemon5.txt', 'w') as file:
        file.write(f"Average hit point for Pokemons of stage 3.0 = {average_hp}")
    
    return average_hp

# Write to csv file
def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as output_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# ----------------------------------------------------------------
 
# Calling all functions
filename = '../data/pokemonTrain.csv'
# 1
percentage = calculate_fire_type_percentage('../data/pokemonTrain.csv')

with open('pokemon1.txt', 'w') as output_file:
    output_file.write(f"Percentage of fire type Pokemons at or above level 40 = {percentage}")
# 2
data = fill_missing_types(filename)
# 3
modified_data = fill_missing_values(data)
# Create csv from 2 & 3
write_to_csv(modified_data, '../data/pokemonResult.csv')
# 4
pokemon_personalities = create_pokemon_personality_mapping("../data/pokemonResult.csv")
with open('pokemon4.txt', 'w') as file:
  file.write("Pokemon type to personality mapping:\n\n")
  for type, personalities in sorted(pokemon_personalities.items()):
    file.write(f"{type}: {', '.join(personalities)}\n")
# 5
calculate_average_hit_points('../data/pokemonResult.csv')