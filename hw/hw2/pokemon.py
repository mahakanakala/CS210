import csv
from collections import Counter

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
    
def get_most_common_type(weakness):
    types = []
    for w in weakness.split(','):
        types.append(w.strip())
    type_counts = Counter(types)
    most_common_type = min(type_counts, key=lambda k: (-type_counts[k], k))
    return most_common_type


def fill_missing_types(filename):
    filled_data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['type'] == 'NaN':
                most_common_type = get_most_common_type(row['weakness'])
                row['type'] = most_common_type
            filled_data.append(row)
    return filled_data

def create_pokemon_personality_mapping(data_file):
    pokemon_personality_mapping = {}

    with open(data_file, 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            pokemon_type = parts[4]
            personality = parts[3]

            if pokemon_type in pokemon_personality_mapping:
                pokemon_personality_mapping[pokemon_type].append(personality)

            else:
                pokemon_personality_mapping[pokemon_type] = [personality]

    sorted_mapping = dict(sorted(pokemon_personality_mapping.items()))

    for pokemon_type in sorted_mapping:
        sorted_mapping[pokemon_type].sort()

    
    with open("pokemon4.txt", 'w') as output_file:
        print("Pokemon type to personality mapping: \n", file=output_file)
        for pokemon_type, personalities in sorted_mapping.items():
            print(f"{pokemon_type}: {', '.join(personalities)}", file=output_file)
            # print(f"{pokemon_type}: {', '.join(personalities)}")

# create_pokemon_personality_mapping("../data/pokemonResult.csv")

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
create_pokemon_personality_mapping("../data/pokemonResult.csv")
# 5
calculate_average_hit_points('../data/pokemonResult.csv')