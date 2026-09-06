# 🔐 Password Strength Analyzer

#### Video Demo: https://youtu.be/0KVOqrRXAzw

#### Description:

**Password Strength Analyzer** is a Python command-line application that evaluates the strength and predictability of a password.

The goal of this project is to go beyond simply checking whether a password contains uppercase letters, numbers, or symbols. The analyzer also looks for common weaknesses that can make passwords easier to guess, such as sequential characters, repeated characters, repeated patterns, keyboard patterns, and commonly used passwords.

## Features

The program analyzes a password based on several characteristics:

* **Password length**
* **Uppercase letters**
* **Lowercase letters**
* **Numbers**
* **Special characters**
* **Common passwords**
* **Sequential patterns**, such as `1234` or `abcd`
* **Reverse sequences**, such as `4321` or `dcba`
* **Repeated characters**, such as `aaaa`
* **Repeated chunks**, such as `abcabc`
* **Keyboard patterns**, such as `qwerty` and `asdf`

After analyzing these characteristics, the program generates a **security score from 0 to 100**.

The score is then classified into one of five categories:

| Score  | Strength    |
| ------ | ----------- |
| 0–19   | VERY WEAK   |
| 20–39  | WEAK        |
| 40–59  | MODERATE    |
| 60–79  | STRONG      |
| 80–100 | VERY STRONG |

The program also provides recommendations based on the weaknesses it identifies.

## How It Works

The application follows a simple analysis pipeline:

```text
User enters password
        ↓
analyze_password()
        ↓
detect_patterns()
        ↓
check_common_password()
        ↓
calculate_score()
        ↓
classify_strength()
        ↓
generate_recommendations()
        ↓
display_report()
```

The `main()` function controls the overall flow of the program, while each individual function is responsible for one specific task.

### `analyze_password()`

Performs the main password analysis and returns the results in a dictionary.

### `detect_patterns()`

Searches for predictable patterns, including sequences, repeated characters, repeated chunks, and keyboard patterns.

### `check_common_password()`

Checks whether the password matches a password in the program's built-in list of commonly used passwords. The comparison is case-insensitive.

### `calculate_score()`

Calculates a score between 0 and 100. Password length and character diversity increase the score, while common passwords and predictable patterns reduce it.

### `classify_strength()`

Converts the numerical score into a strength category.

### `generate_recommendations()`

Uses the analysis results to provide suggestions for improving the password.

### `display_report()`

Displays the final analysis, score, strength classification, and recommendations without displaying the actual password.

## Security Considerations

The project is designed so that the password itself is not displayed in the final report.

The program uses Python's `getpass` module to accept the password without showing the characters on the terminal.

The actual password is not:

* Printed in the report
* Stored in a file
* Included in the score
* Included in recommendations
* Written to logs

The project is intended as an educational password-analysis tool and should not be considered a replacement for professional password auditing or password-cracking tools.

## Testing

The project includes `test_project.py`, which uses **pytest** to test the main functions.

The tests cover:

* Password analysis
* Pattern detection
* Common password detection
* Score calculation
* Strength classification
* Recommendation generation

Tests can be run with:

```bash
pytest
```

## Installation

Clone or download the project and navigate to the project directory.

Install the required testing dependency:

```bash
pip install -r requirements.txt
```

## Usage

Run the program with:

```bash
python project.py
```

The program will ask for a password securely and then display the analysis.

Example:

```text
PASSWORD ANALYSIS
------------------------------
Length: 16
Uppercase: True
Lowercase: True
Numbers: True
Symbols: True
Common password: False
Patterns: []

Score: 100 /100
Strength: VERY STRONG

Recommendations:
- Excellent password length.
- Good character diversity.
- No obvious predictable patterns.
- Password does not appear to be common.
```

## Project Structure

```text
password-strength-analyzer/
│
├── project.py
├── test_project.py
├── requirements.txt
└── README.md
```

## Technologies Used

* **Python**
* `getpass`
* `re`
* `pytest`

The main application uses Python's standard library, while `pytest` is used for automated testing.

## CS50P Concepts Demonstrated

This project applies several concepts learned throughout CS50P, including:

* Variables
* Functions
* Conditionals
* Loops
* Strings
* Lists
* Dictionaries
* Sets
* Regular expressions
* Exception handling
* Standard library modules
* Testing with pytest
* Command-line programs

## Future Improvements

Possible improvements for future versions include:

* Using a larger common-password dataset
* Adding a password entropy calculation
* Detecting additional predictable patterns
* Improving the scoring algorithm
* Adding a graphical interface
* Adding more comprehensive automated tests
* Supporting configurable password policies

---

**Password Strength Analyzer**
*A CS50P Final Project*