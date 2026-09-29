# SQL Data Analyzer

A Python and SQLite project designed to clean, process, and analyze preference data from CSV files and manage storage in a relational database.

## Overview

This project reads preference data (such as programming languages and problem types) from a CSV file. It normalizes text data by removing leading/trailing whitespace and converting strings to lowercase, calculates frequency counts, and sorts results. It also includes database integration for querying and inserting records directly using SQLite.

## Key Features

- **Data Cleaning**: Standardized text input using `strip()` and `lower()`.
- **Frequency Analysis**: Key-value counting with custom sorting via `sorted()` and `lambda` functions.
- **Database Management**: Table creation, data insertion, and querying in SQLite.

## Project Structure

```text
.
├── fav.csv         # Raw CSV dataset
└── sql.py          # Initial data reading script
```
#USAGE

Run the data analysis script:
python sql.py
