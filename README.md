# CS210

## Problems I don't fully understand:
- [PS2 Problem 3](recitation/ps2.ipynb)
- [PS3 Problem 1, 3, 4.4, 4.5, 4.6, 5](recitation/ps3.ipynb)
- [PS Problem 1.4](recitation/ps5.ipynb)
*Exam 2*
- [Lecture Feb 8 Metacharacter ?](lecture\feb8_notes.ipynb)
- [Lecture Feb 12 Example 1, Special Characters, Greedy/Non-greedy](lecture\feb12_notes.ipynb)
- [Lecture Feb 15 word boundary](lecture\feb15_notes.ipynb)
- [Lecture Feb 12 printing row less than](lecture\feb12_notes.ipynb)
  ```python
    reader = csv.DictReader(open('./data/Auto MPG Original.csv'))
    for index,row in enumerate(reader):
      print(row)
    if index > 3:
        break
      ```
      

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