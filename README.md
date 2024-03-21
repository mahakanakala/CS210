# CS210
## HW2
- [ ] [pokemon.py](hw/hw2/pokemon.py)
  - [ ] task 4: [10 pts] Create a dictionary that maps pokemon types to their personalities. This dictionary would map a string to a list of strings. For example:
     {"fire": ["docile", "modest", ...], "normal": ["mild", "relaxed", ...],  ...} Your dictionary should have the keys ordered alphabetically, and also items ordered alphabetically in the values list, as shown in the example above.
     Print the dictionary in the following format:
     Pokemon type to personality mapping:

      normal: mild, relaxed, ...
      fire: docile, modest, ...
      ...
  - [ ] task 4.1: create the csv
- [ ] [covid.py](hw/hw2/covid.py)
  - [ ] task 3: [7 pts] Fill in the missing (NaN) "latitude" and "longitude" values by the average of the latitude and longitude values for the province where the case was recorded. Round the average to 2 decimal places. (not clculating correctly)
  - [X] task 4: [7 pts] Fill in the missing “city” values by the most occurring city value in that province. In case of a tie, use the city that appears first in alphabetical order.
  - [X] task 5: [10 pts] Fill in the missing "symptom" values by the single most frequent symptom in the province where the case was recorded. In case of a tie, use the symptom that appears first in alphabetical order.
- [ ] [tfidf.py](hw/hw2/tfidf.py)

## Problems I don't fully understand:
- [PS2 Problem 3](recitation/ps2.ipynb)
- [PS3 Problem 1, 3, 4.4, 4.5, 4.6, 5](recitation/ps3.ipynb)
- [PS Problem 1.4](recitation/ps5.ipynb)

## Problems I need to do:
- [PS2 Problem 4 and 5](recitation/ps2.ipynb)
- [PS4 Problem 2](recitation/ps4.ipynb)

## Topics I need to go over:

### Basic Python Syntax and Functions
- [ ] `lambda` function
  - [ ] can be used in sorting for `key= lambda x: x/2 == 0`
- [ ] single line iterator function
  - [ ] list: `list =[n for n in range(0, 101) if n/2 == 0]`
    - [ ] makes a list of the even numbers from 0 to 100 inclusive
  - [ ] tuple: `tup = ()`
  - [ ] dict = `dictionary = {}`
- [ ] `try`, `except`, `catch` function
  - [ ] wrap the logic in between the `try` and `catch`
- [ ] matrix operations