# Moodle grades cleaner

Project for cleaning the data on the grades exported from moodle. Currently grades have the students names separated into first name and surname, while other moodle docs such as activity logs show them as full names. This script returns the grades with one complete name field.

Another feature of this script is the removal of irrelevant columns for our current project. Column names are in portuguese, so if you'd like to use this script for other languages we suggest you change the names on the script.

## Dependencies

This project relies on the `pandas` module being available, as well as the `openpyxl` module necessary for writing and reading `.xlsx` files, format used by moodle when exporting the list of students for a given course.

## Usage

You can run the script with python 3.9 passing the path to the grades to be cleaned and the path for the result to be saved to:

```bash
python grades_cleaner.py moodle_logs.csv student_list.csv cleaned_moodle_logs.csv
```

## Testing

The tests reside on the `grades_cleaner_test.py` file and use the `unittest` package, to run them execute:

```bash
python -m grades_cleaner_test
```
