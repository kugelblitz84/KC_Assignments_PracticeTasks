# Practice Tasks

## Run the exercises

Install Git and Python 3.10 or newer. Open a terminal and clone the repository:

```sh
git clone https://github.com/kugelblitz84/KC_Assignments_PracticeTasks.git
cd KC_Assignments_PracticeTasks
```

Create and activate a virtual environment. On Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependency used by the login and student profile exercises:

```sh
python -m pip install bcrypt
```

Stay in the cloned folder containing `day1`, `day2`, and `day3`. Run the command under any exercise below. For interactive exercises, enter your answers in the terminal when prompted.

## Day 1

### [Display a username and age](day1/Take_username_and_age_and_display.py)

Read the username as text and the age as an integer, then print both values.

```sh
python -m day1.Take_username_and_age_and_display
```

### [Check whether a number is even or odd](day1/Even_odd.py)

Use `n & 1` to check whether the number is odd, then print the result.

```sh
python -m day1.Even_odd
```

### [Perform arithmetic on two numbers](day1/Perform_addtion_sub_mul_div_on2nums.py)

Read two integers and calculate their sum, product, difference, and quotient. Subtract the smaller number from the larger for the difference.

```sh
python -m day1.Perform_addtion_sub_mul_div_on2nums
```

### [Find the area of a rectangle](day1/area_of_rect.py)

Read length and breadth as integers, then multiply them. Handle invalid input with `ValueError`.

```sh
python -m day1.area_of_rect
```

### [Average subject marks](day1/avg_of_three_sub_marks.py)

Convert the entered marks to integers, add them, and divide by the number of marks entered.

```sh
python -m day1.avg_of_three_sub_marks
```

### [Convert between Celsius and Fahrenheit](day1/Convert_celsius_to_fahrentheit.py)

Choose a conversion from the menu, read the temperature, and apply the corresponding formula.

```sh
python -m day1.Convert_celsius_to_fahrentheit
```

### [Break an amount into notes](day1/breaking_money.py)

Work from the largest note to the smallest. Use division to count each note and the remainder for the amount left.

```sh
python -m day1.breaking_money
```

## Day 2

### [Check the sign of a number](day2/check_number_sign.py)

Classify an integer as positive, negative, or zero.

```sh
python -m day2.check_number_sign
```

### [Calculate subject grades](day2/Calculate_grades.py)

Enter a mark from 0 to 100 for each subject to see its letter grade.

```sh
python -m day2.Calculate_grades
```

### [Find the largest number](day2/find_the_largest_numebr.py)

Use `max()` to find the largest of the space-separated integers.

```sh
python -m day2.find_the_largest_numebr
```

### [Print even numbers](day2/prnt_even_nums.py)

Count from 2 to 100 in steps of two.

```sh
python -m day2.prnt_even_nums
```

### [Generate a multiplication table](day2/generate_multiplication_table.py)

Print the products of the entered integer and the numbers 1 through 10.

```sh
python -m day2.generate_multiplication_table
```

### [Sum the integers from 1 to N](day2/sum_of_1_to_N.py)

Calculate the total with the formula `N * (N + 1) // 2`.

```sh
python -m day2.sum_of_1_to_N
```

### [Count digits](day2/count_digits.py)

Count the digits in a positive integer by repeatedly dividing it by 10 and discarding the remainder.

```sh
python -m day2.count_digits
```

### [Use a menu-driven calculator](day2/calculator.py)

Choose addition, subtraction, multiplication, or division, then enter two integers. The menu lets you repeat the calculation with new inputs.

```sh
python -m day2.calculator
```

### [Register and log in](day2/password_verif_and_login.py)

Create a user or verify a password against its stored hash in `day2/db.json`.

```sh
python -m day2.password_verif_and_login
```

## Day 3

### [Sum a list of numbers](day3/calculate_sum.py)

Enter space-separated integers and use `sum()` to total them.

```sh
python -m day3.calculate_sum
```

### [Find the smallest and largest numbers](day3/largest_smallest_number_in_list.py)

Start with the first integer and update the minimum and maximum while scanning the list.

```sh
python -m day3.largest_smallest_number_in_list
```

### [Search for an item in a list](day3/search_item_in_list.py)

Enter a list of integers and a number to search for. Print every zero-based index where the number appears.

```sh
python -m day3.search_item_in_list
```

### [Remove duplicates](day3/remove_duplicates.py)

Convert the entered integers to a set and print the distinct values.

```sh
python -m day3.remove_duplicates
```

### [Convert text to lowercase](day3/user_inputs_to_lowercase.py)

Apply `lower()` to the input and print the resulting string.

```sh
python -m day3.user_inputs_to_lowercase
```

### [Count words in a sentence](day3/count_words.py)

Split the sentence on whitespace and print the total number of words.

```sh
python -m day3.count_words
```

### [Count word frequencies](day3/count_frequency.py)

Split the sentence on whitespace and count each word in a dictionary. The counts preserve capitalization and punctuation, so `Hi`, `hi`, and `hi!` each have their own entry.

```sh
python -m day3.count_frequency
```

### [Update a student profile](day3/update_student_profile.py)

Create an account or log in, then view or update your name, age, class, and roll number. This exercise shares `day2/db.json` with the login exercise.

```sh
python -m day3.update_student_profile
```

## Project: Smart Knowledge System

The Smart Knowledge System is a terminal app for maintaining and searching a categorized FAQ. You can add, browse, edit, and delete entries. When you search, the app compares your keywords with stored questions and answers and displays the best match. The history screen lists recorded actions, and the statistics screen shows the number of knowledge items, total recorded actions, actions per user, and keyword frequencies.

### Run the project

From the repository root, activate the virtual environment described above and install the project dependencies.

```sh
python -m pip install bcrypt PyJWT
```

Set `JWT_SECRET` in the terminal you will use to run the app. Login uses this key to sign a session token that expires after two hours.

**Windows (PowerShell)**

```powershell
$env:JWT_SECRET = python -c "import secrets; print(secrets.token_hex(32))"
```

**macOS or Linux**

```sh
export JWT_SECRET="$(python -c 'import secrets; print(secrets.token_hex(32))')"
```

Start the app from the directory containing the `project` folder.

```sh
python -m project.main
```

On your first run, choose **2. Sign up**, create an account, then choose **1. Log in**. To try the included FAQ, select **2. Search Knowledge** and enter `Where is the JWT secret key stored?`.

### Project data

| File | Contents |
| --- | --- |
| `project/db.json` | User accounts and bcrypt password hashes |
| `project/knowldge_base.json` | FAQ entries grouped by category, each with an ID, question, and answer |
| `project/history.json` | Timestamped actions with usernames and search keywords, used by the history and statistics screens |
