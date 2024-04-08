import csv  

with open('./mycovidResullt.csv') as f:   
    reader = csv.DictReader(f)   
    lines1 = list(reader)  
    with open('./covidResult.csv') as f:   
        reader = csv.DictReader(f)    
        lines2 = list(reader)  
        for i, row in enumerate(lines1):   
            if row['city'] != lines2[i]['city']:     
                print(f"Row {i+1} in mycovidResult.csv:\n{row}")
                print(f"Corresponding row in covidResult.csv:\n{lines2[i]}\n")